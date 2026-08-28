# lbl_bit.py
import copy
from collections import deque

EDGE_NAMES = {
    4: "FR (Zielono-Pomaranczowa)",
    5: "FL (Zielono-Czerwona)",
    6: "BL (Niebiesko-Czerwona)",
    7: "BR (Niebiesko-Pomaranczowa)"
}

SLOT_NAMES = {
    0: "UB", 1: "UR", 2: "UF", 3: "UL",
    4: "FR", 5: "FL", 6: "BL", 7: "BR",
    8: "DF", 9: "DR", 10: "DB", 11: "DL"
}

WHITE_EDGES = [8, 9, 10, 11]  # DF, DR, DB, DL (krawedzie z bialym kolorem)

def _apply(cube, seq, log):
    if not seq:
        return
    for m in seq.split():
        cube.apply_move(m)
        log.append(m)

def _find_edge(cube, target_idx):
    for s in range(12):
        p, o = cube.get_edge(s)
        if p == target_idx:
            return s, o
    return None, None

def _find_corner(cube, target_idx):
    for s in range(8):
        p, o = cube.get_corner(s)
        if p == target_idx:
            return s, o
    return None, None

def is_first_layer_intact(cube):
    """Sprawdza czy cala dolna biala warstwa (krzyz + narozniki) jest nienaruszona."""
    for e in [8, 9, 10, 11]:
        p, o = cube.get_edge(e)
        if p != e or o != 0:
            return False
    for c in [4, 5, 6, 7]:
        p, o = cube.get_corner(c)
        if p != c or o != 0:
            return False
    return True

# =========================================================================
# KROK 1: KWIATEK (DAISY) - PODKROKI 1.1, 1.2, 1.3, 1.4
# =========================================================================
def is_white_up(cube, slot):
    """Sprawdza bezblednie na bitboardzie czy slot 0..3 ma biala krawedz z ori == 0."""
    p, o = cube.get_edge(slot)
    return (p in WHITE_EDGES) and (o == 0)

def count_white_petals(cube):
    """Zwraca liczbe prawidlowo ulozonych bialych krawedzi na warstwie U."""
    return sum(1 for s in range(4) if is_white_up(cube, s))

def solve_single_daisy_petal(cube, target_count, log):
    """
    Wstawia kolejny bialy platek metoda BFS do 4 ruchow.
    Gwarantuje najkrotsza sciezke bez niszczenia wczesniejszych platkow.
    """
    initial_count = count_white_petals(cube)
    if initial_count >= target_count:
        return

    ALLOWED_MOVES = [
        "U", "U'", "U2",
        "D", "D'", "D2",
        "R", "R'", "R2",
        "L", "L'", "L2",
        "F", "F'", "F2",
        "B", "B'", "B2"
    ]

    queue = deque([(copy.deepcopy(cube), [])])
    visited_states = set()
    best_seq = None

    while queue:
        curr_c, path = queue.popleft()
        
        state_key = (curr_c.edges, curr_c.corners)
        if state_key in visited_states:
            continue
        visited_states.add(state_key)

        current_count = count_white_petals(curr_c)
        if current_count >= target_count:
            best_seq = " ".join(path)
            break

        if len(path) >= 4:
            continue

        for m in ALLOWED_MOVES:
            if path:
                last_base = path[-1][0]
                curr_base = m[0]
                if last_base == curr_base:
                    continue

            next_c = copy.deepcopy(curr_c)
            next_c.apply_move(m)
            queue.append((next_c, path + [m]))

    if best_seq:
        _apply(cube, best_seq, log)

def step1_daisy(cube, log):
    """Calosc etapu 1 (wszystkie 4 platki po kolei)."""
    for target in range(1, 5):
        solve_single_daisy_petal(cube, target, log)

# =========================================================================
# KROK 2: BIAŁY KRZYŻ
# =========================================================================
def step2_white_cross(cube, log):
    target_to_top = {8: 2, 9: 1, 10: 0, 11: 3}
    target_move = {8: "F2", 9: "R2", 10: "B2", 11: "L2"}
    for target, needed_top in target_to_top.items():
        for _ in range(4):
            if _find_edge(cube, target)[0] == needed_top:
                break
            _apply(cube, "U", log)
        _apply(cube, target_move[target], log)

# =========================================================================
# KROK 3: NAROŻNIKI PIERWSZEJ WARSTWY
# =========================================================================
def step3_first_layer(cube, log):
    targets = [4, 5, 6, 7]
    top_slots = {4: 3, 5: 2, 6: 1, 7: 0}
    for target in targets:
        for _ in range(16):
            slot, ori = _find_corner(cube, target)
            if slot == target and ori == 0:
                break
            if slot == 5:
                _apply(cube, "R U R' U'", log)
            elif slot == 4:
                _apply(cube, "F U F' U'", log)
            elif slot == 6:
                _apply(cube, "B U B' U'", log)
            elif slot == 7:
                _apply(cube, "L U L' U'", log)
            elif slot in [0, 1, 2, 3]:
                needed = top_slots[target]
                for _ in range(4):
                    if _find_corner(cube, target)[0] == needed:
                        break
                    _apply(cube, "U", log)
                for _ in range(6):
                    c_p, c_o = cube.get_corner(target)
                    if c_p == target and c_o == 0:
                        break
                    if target == 5:
                        _apply(cube, "R U R' U'", log)
                    elif target == 4:
                        _apply(cube, "F U F' U'", log)
                    elif target == 6:
                        _apply(cube, "B U B' U'", log)
                    elif target == 7:
                        _apply(cube, "L U L' U'", log)
                break

# =========================================================================
# KROK 4: DRUGA WARSTWA
# =========================================================================
def solve_single_middle_edge(cube, target, log):
    """
    Uklada jedna krawedz srodkowa.
    Dla przednich (4, 5) uzywa algorytmow F, dla tylnych (6, 7) sekwencji z E2.
    """
    FRONT_ALGS = [
        "U R U' R' U' F' U F",       # w prawo do FR
        "U' F' U F U R U' R'",       # w prawo do FR (z prawej)
        "U' L' U L U F U' F'",       # w lewo do FL
        "U F U' F' U' L' U L",       # w lewo do FL (z lewej)
    ]

    for attempt in range(8):
        slot, ori = _find_edge(cube, target)

        # 1. Krawedz na swoim miejscu
        if slot == target and ori == 0:
            break

        # 2. Wypchniecie ze srodka
        if slot in [4, 5, 6, 7]:
            if slot in [4, 5]:
                eject_alg = "U R U' R' U' F' U F" if slot == 4 else "U' L' U L U F U' F'"
            else:
                front_alg = "U R U' R' U' F' U F" if slot == 6 else "U' L' U L U F U' F'"
                eject_alg = f"E2 {front_alg} E2"
            _apply(cube, eject_alg, log)
            continue

        # 3. Wstawienie z gory (0..3)
        elif slot in [0, 1, 2, 3]:
            best_seq = None
            setup = "E2" if target in [6, 7] else ""
            teardown = "E2" if target in [6, 7] else ""

            for u_turns in range(4):
                auf_seq = " ".join(["U"] * u_turns)
                for cand_alg in FRONT_ALGS:
                    test_cube = copy.deepcopy(cube)
                    seq_parts = [setup, auf_seq, cand_alg, teardown]
                    full_cand = " ".join([p for p in seq_parts if p]).strip()

                    for m in full_cand.split():
                        test_cube.apply_move(m)

                    p, o = test_cube.get_edge(target)
                    if p == target and o == 0 and is_first_layer_intact(test_cube):
                        best_seq = full_cand
                        break
                if best_seq is not None:
                    break

            if best_seq is not None:
                _apply(cube, best_seq, log)
            break

def step4_second_layer(cube, log):
    """Caly etap 4."""
    for t in [4, 5, 6, 7]:
        solve_single_middle_edge(cube, t, log)

# =========================================================================
# KROK 5: ŻÓŁTY KRZYŻ (YELLOW CROSS)
# =========================================================================
def get_yellow_cross_state(cube):
    """
    Zwraca tuple (sloty zorientowane zolto do gory, nazwa_stanu).
    Gorne sloty krawedzi: 0:UB, 1:UR, 2:UF, 3:UL.
    """
    oriented = [s for s in range(4) if cube.get_edge(s)[1] == 0]
    count = len(oriented)
    
    if count == 4:
        return oriented, "Krzyz"
    elif count == 2:
        if set(oriented) in [{1, 3}, {0, 2}]:
            return oriented, "Linia"
        else:
            return oriented, "Kat L"
    else:
        return oriented, "Kropka"

def step5_yellow_cross(cube, log):
    ALG = "F R U R' U' F'"

    for _ in range(6):
        oriented, state = get_yellow_cross_state(cube)
        if state == "Krzyz":
            break

        if state == "Linia":
            if set(oriented) == {0, 2}:  # Linia pionowa -> obroc do poziomu
                _apply(cube, "U", log)
            _apply(cube, ALG, log)

        elif state == "Kat L":
            u_turns = 0
            while set([s for s in range(4) if cube.get_edge(s)[1] == 0]) != {0, 3}:
                _apply(cube, "U", log)
                u_turns += 1
                if u_turns > 4:
                    break
            _apply(cube, ALG, log)

        elif state == "Kropka":
            _apply(cube, ALG, log)

# lbl_bit.py

# lbl_bit.py

# lbl_bit.py

# =========================================================================
# KROK 6: DOPASOWANIE KRAWĘDZI ŻÓŁTEGO KRZYŻA (SUNE)
# =========================================================================
# lbl_bit.py

def step6_permute_edges(cube, log):
    """
    Krok 6: Dopasowanie ramion zoltego krzyza do centrow (Permutacja krawedzi U).
    Uzywa wylacznie algorytmu Sune i obrotow U, znajdujac najkrotsza,
    bebledna sekwencje (max 1-2 wykonania Sune).
    """
    SUNE = "R U R' U R U2 R'"

    # Sprawdz czy krawedzie juz pasuja (byc moze wystarczy sam obrot U)
    for u_turns in range(4):
        test_c = copy.deepcopy(cube)
        for _ in range(u_turns):
            test_c.apply_move("U")
        if all(test_c.get_edge(s)[0] == s for s in range(4)):
            for _ in range(u_turns):
                _apply(cube, "U", log)
            return

    # BFS szukajacy poprawnej sekwencji U i Sune
    # Dozwolone ruchy w fazie Sune
    MOVES = ["U", "U'", "U2", SUNE]
    queue = deque([(copy.deepcopy(cube), [])])
    visited = set()
    best_seq = None

    while queue:
        curr_c, path = queue.popleft()

        # Stan krawedzi gornych
        state_key = tuple(curr_c.get_edge(s) for s in range(4))
        if state_key in visited:
            continue
        visited.add(state_key)

        # Sprawdz czy wszystkie 4 krawedzie pasuja do swoich slotow
        if all(curr_c.get_edge(s)[0] == s for s in range(4)):
            best_seq = " ".join(path)
            break

        # Sune wykonuje sie maksymalnie 2-3 razy z obrotami U
        if len([p for p in path if p == SUNE]) >= 3:
            continue
        if len(path) >= 6:
            continue

        for m in MOVES:
            # Unikaj dwoch ruchow U pod rzad
            if path and m.startswith("U") and path[-1].startswith("U"):
                continue

            next_c = copy.deepcopy(curr_c)
            for single_m in m.split():
                next_c.apply_move(single_m)
            queue.append((next_c, path + [m]))

    if best_seq:
        _apply(cube, best_seq, log)


# =========================================================================
# KROK 7: ROZMIESZCZENIE NAROŻNIKÓW NA WŁAŚCIWYCH MIEJSCACH (NIKLAS)
# =========================================================================
def step7_permute_corners(cube, log):
    """Krok 7: Wrzuca narozniki na wlasciwe pozycje (p == s), bez zmiany ich obrotu."""
    RIGHT_NIKLAS = "U R U' L' U R' U' L"
    LEFT_NIKLAS  = "U' L' U R U' L U R'"

    for _ in range(8):
        correct = [s for s in range(4) if cube.get_corner(s)[0] == s]
        if len(correct) == 4:
            break

        if len(correct) == 1:
            c = correct[0]
            if c == 2:   # UFR (prawy przedni) -> prawy Niklas
                _apply(cube, RIGHT_NIKLAS, log)
            elif c == 3: # UFL (lewy przedni) -> lewy Niklas
                _apply(cube, LEFT_NIKLAS, log)
            elif c == 1: # UBR (prawy tylny) -> obrot o 180 (U2) i lewy Niklas
                _apply(cube, "U2 " + LEFT_NIKLAS + " U2", log)
            elif c == 0: # UBL (lewy tylny) -> obrot o 180 (U2) i prawy Niklas
                _apply(cube, "U2 " + RIGHT_NIKLAS + " U2", log)
        else:
            # Zaden naroznik nie pasuje -> wykonaj raz prawy Niklas
            _apply(cube, RIGHT_NIKLAS, log)


# =========================================================================
# KROK 8: OBRÓCENIE NAROŻNIKÓW (R' D' R D) - ZAKOŃCZENIE KOSTKI
# =========================================================================
# lbl_bit.py

# lbl_bit.py

def is_ufr_corner_yellow_up(cube):
    """
    Sprawdza bezposrednio na siatce, czy w slocie 2 (UFR - prawy przedni rog)
    zolty kolor ('Y') jest skierowany scisle do gory.
    Wspolrzedne UFR na sciance U to wiersz 2, kolumna 5 w gridzie.
    """
    grid = cube.to_2d_grid()
    return grid[2][5] == 'Y'


def step8_orient_corners(cube, log):
    """
    Krok 8: Obrot naroznikow (Orientacja naroznikow U / Ulozona kostka).
    Dziala w slocie roboczym UFR (prawy przedni):
    1. Sprawdza czy na sciance U w prawym przednim rogu jest 'Y'.
    2. Jesli nie -> wykonuje R' D' R D az bedzie.
    3. Obraca U i powtarza dokladnie 4 razy dla kazdego rogu.
    4. Na koniec wyrownuje gore (U).
    """
    ALG = "R' D' R D"

    # Dokladnie 4 narozniki do obrobienia
    for _ in range(4):
        while not is_ufr_corner_yellow_up(cube):
            _apply(cube, ALG, log)
        
        # Podstawiamy nastepny naroznik pod slot UFR
        _apply(cube, "U", log)

    # Koncowe dopasowanie scianki U (AUF) do centrow bocznych
    for _ in range(4):
        # Sprawdzamy czy przednia krawedz i rog pasuja kolorem do przodu (F - zielony)
        grid = cube.to_2d_grid()
        if grid[3][4] == 'G' and grid[3][5] == 'G':
            break
        _apply(cube, "U", log)

# =========================================================================
# SŁOWNIK KROKÓW
# =========================================================================
STEPS = {
    1: ("1. Kwiatek (Daisy - Pelna)", step1_daisy),
    11: ("1.1 Pierwszy platek Daisy", lambda c, l: solve_single_daisy_petal(c, 1, l)),
    12: ("1.2 Drugi platek Daisy", lambda c, l: solve_single_daisy_petal(c, 2, l)),
    13: ("1.3 Trzeci platek Daisy", lambda c, l: solve_single_daisy_petal(c, 3, l)),
    14: ("1.4 Czwarty platek Daisy", lambda c, l: solve_single_daisy_petal(c, 4, l)),
    2: ("2. Bialy Krzyz (White Cross)", step2_white_cross),
    3: ("3. Pierwsza warstwa (Corners)", step3_first_layer),
    4: ("4. Druga warstwa (Pelna)", step4_second_layer),
    5: ("5. Zolty Krzyz (Yellow Cross)", step5_yellow_cross),
    6: ("6. Dopasowanie krawedzi U do centrow", step6_permute_edges),
    7: ("7. Pozycje naroznikow U (Permutacja)", step7_permute_corners),
    8: ("8. Obrot naroznikow (Kostka ulozona)", step8_orient_corners),
}

def solve_step(cube, step_id):
    if step_id not in STEPS:
        return "", "Nieznany krok"
    name, func = STEPS[step_id]
    log = []
    func(cube, log)
    return " ".join(log), name

def LBL_FULL(cube, move_list=""):
    log = []
    for step_id in [1, 2, 3, 4, 5, 6, 7, 8]:
        _, func = STEPS[step_id]
        func(cube, log)
    res = " ".join(log)
    return f"{move_list} {res}".strip() if move_list else res