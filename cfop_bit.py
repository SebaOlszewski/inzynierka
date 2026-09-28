# cfop_bit.py
import copy
from collections import deque
import lbl_bit
import oll_bit
import f2l_bit

CROSS_EDGES = [8, 9, 10, 11]

ALL_MOVES = [
    "U", "U'", "U2",
    "D", "D'", "D2",
    "R", "R'", "R2",
    "L", "L'", "L2",
    "F", "F'", "F2",
    "B", "B'", "B2"
]


def _apply(cube, seq, log):
    if not seq:
        return
    for m in seq.split():
        cube.apply_move(m)
        log.append(m)


# =========================================================================
# KROK 1: DIRECT WHITE CROSS (BFS DRZEWIASTY PER-KRAWĘDŹ)
# =========================================================================
def is_edge_in_place(cube, edge_idx):
    p, o = cube.get_edge(edge_idx)
    return p == edge_idx and o == 0


def is_corner_in_place(cube, corner_idx):
    p, o = cube.get_corner(corner_idx)
    return p == corner_idx and o == 0


def is_cross_solved(cube):
    return all(is_edge_in_place(cube, e) for e in CROSS_EDGES)


def _get_cross_subset_key(cube, tracked_edges):
    """
    Zwraca 60-bitowy klucz stanu uwzględniający wyłącznie sloty i orientacje
    krawędzi z listy tracked_edges (ignoruje szum pozostałych krawędzi).
    """
    key = 0
    edges_val = cube.edges
    for s in range(12):
        val = (edges_val >> (5 * s)) & 0x1F
        if (val >> 1) in tracked_edges:
            key |= (val << (5 * s))
    return key


def solve_cross_edge_tree(cube, target_edge, solved_edges, log):
    if is_edge_in_place(cube, target_edge):
        return

    tracked_edges = set(solved_edges)
    tracked_edges.add(target_edge)

    queue = deque([(copy.deepcopy(cube), [])])
    visited = set()
    best_seq = None

    while queue:
        curr_c, path = queue.popleft()

        state_key = _get_cross_subset_key(curr_c, tracked_edges)
        if state_key in visited:
            continue
        visited.add(state_key)

        if is_edge_in_place(curr_c, target_edge) and all(is_edge_in_place(curr_c, e) for e in solved_edges):
            best_seq = " ".join(path)
            break

        if len(path) >= 5:
            continue

        for m in ALL_MOVES:
            if path and path[-1][0] == m[0]:
                continue

            next_c = copy.deepcopy(curr_c)
            next_c.apply_move(m)
            queue.append((next_c, path + [m]))

    if best_seq:
        _apply(cube, best_seq, log)


def solve_cross(cube, log):
    placed = []
    for edge in CROSS_EDGES:
        solve_cross_edge_tree(cube, edge, placed, log)
        placed.append(edge)


# =========================================================================
# KROK 2: PEŁNY F2L (PAROWANIE NAROŻNIK + KRAWĘDŹ NA BITACH W O(1))
# =========================================================================
def solve_f2l(cube, log):
    f2l_bit.solve_full_f2l(cube, log)


# =========================================================================
# KROK 3: OLL Z WYKORZYSTANIEM OLL_BIT (12-BITOWY KLUCZ ORIENTACJI)
# =========================================================================
def is_u_face_done(cube):
    """Sprawdza bitowo w czasie O(1), czy cała warstwa U jest zorientowana."""
    return oll_bit.get_oll_key(cube) == 0


def solve_oll(cube, log):
    if is_u_face_done(cube):
        return

    # 1. Próba 1-Look OLL z tablicy bitowej oll_bit.py
    oll_seq = oll_bit.solve_oll(cube)
    if oll_seq:
        log.extend(oll_seq.split())
        if is_u_face_done(cube):
            return

    # 2. Fallback 2-Look OLL (Orientacja krawędzi + Sune/Antisune na bitach)
    lbl_bit.step5_yellow_cross(cube, log)
    if is_u_face_done(cube):
        return

    # Ponowne sprawdzenie w tablicy OLL po ułożeniu żółtego krzyża (7 przypadków OCLL)
    oll_seq = oll_bit.solve_oll(cube)
    if oll_seq:
        log.extend(oll_seq.split())
        if is_u_face_done(cube):
            return

    # Awaryjne domknięcie orientacji narożników, jeśli nietypowy przypadek
    lbl_bit.step8_orient_corners(cube, log)


# =========================================================================
# KROK 4: PLL (PERMUTACJA WARSTWY U BEZ PSUCIA ORIENTACJI OLL)
# =========================================================================
T_PERM = "R U R' U' R' F R2 U' R' U' R U R' F'"
Y_PERM = "F R U' R' U' R U R' F' R U R' U' R' F R F'"
UA_PERM = "R U' R U R U R U' R' U' R2"
UB_PERM = "R2 U R U R' U' R' U' R' U R'"


def _are_u_corners_permuted(cube):
    """Sprawdza na bitach, czy 4 narożniki U są względem siebie w poprawnej kolejności."""
    c0 = cube.get_corner(0)[0]
    for shift in range(4):
        if all(cube.get_corner(s)[0] == (c0 + s) % 4 for s in range(4)):
            return True
    return False


def _solve_pll_corners(cube, log):
    """Układa narożniki warstwy U za pomocą T-perm / Y-perm (zachowuje OLL)."""
    if _are_u_corners_permuted(cube):
        return

    for auf in ["", "U", "U2", "U'"]:
        for alg in [T_PERM, Y_PERM]:
            tc = copy.deepcopy(cube)
            seq = f"{auf} {alg}".strip()
            for m in seq.split():
                tc.apply_move(m)
            if _are_u_corners_permuted(tc):
                _apply(cube, seq, log)
                return

    # Jeśli żaden pojedynczy T/Y nie wystarcza (rzadki przypadek), wykonaj Y-perm + T-perm
    _apply(cube, Y_PERM, log)
    for auf in ["", "U", "U2", "U'"]:
        tc = copy.deepcopy(cube)
        seq = f"{auf} {T_PERM}".strip()
        for m in seq.split():
            tc.apply_move(m)
        if _are_u_corners_permuted(tc):
            _apply(cube, seq, log)
            return


def _is_u_layer_solved(cube):
    """Sprawdza na bitach, czy wszystkie 4 narożniki i 4 krawędzie U są na swoich miejscach."""
    return (
        all(cube.get_corner(s) == (s, 0) for s in range(4))
        and all(cube.get_edge(s) == (s, 0) for s in range(4))
    )


def _solve_pll_edges(cube, log):
    """Układa krawędzie warstwy U za pomocą Ua-perm / Ub-perm i dopasowuje AUF (U)."""
    # Wyrównaj narożniki U do ich docelowych slotów (0, 1, 2, 3)
    for _ in range(4):
        if cube.get_corner(0)[0] == 0:
            break
        _apply(cube, "U", log)

    if _is_u_layer_solved(cube):
        return

    # BFS po algorytmach krawędziowych PLL (Ua, Ub) i obrotach U (max 2 algorytmy dla H/Z perm)
    moves_pool = ["U", "U'", "U2", UA_PERM, UB_PERM]
    queue = deque([(copy.deepcopy(cube), [])])
    visited = set()

    while queue:
        curr_c, path = queue.popleft()
        state_key = (curr_c.edges, curr_c.corners)
        if state_key in visited:
            continue
        visited.add(state_key)

        if _is_u_layer_solved(curr_c):
            _apply(cube, " ".join(path), log)
            return

        if len(path) >= 5:
            continue

        for m in moves_pool:
            if path and m.startswith("U") and path[-1].startswith("U"):
                continue
            next_c = copy.deepcopy(curr_c)
            for single_m in m.split():
                next_c.apply_move(single_m)
            queue.append((next_c, path + [m]))


def solve_pll(cube, log):
    if not is_u_face_done(cube):
        solve_oll(cube, log)

    _solve_pll_corners(cube, log)
    _solve_pll_edges(cube, log)


# =========================================================================
# INTERFEJS DLA MAIN.PY
# =========================================================================
CFOP_STEPS = {
    1: ("1. Cross (Bialy Krzyz na dole)", solve_cross),
    2: ("2. F2L (Pierwsze dwie warstwy)", solve_f2l),
    3: ("3. OLL (Zolta scianka - oll_bit)", solve_oll),
    4: ("4. PLL (Permutacja warstwy U)", solve_pll),
}


def solve_step(cube, step_id):
    if step_id not in CFOP_STEPS:
        return "", "Nieznany krok"
    name, func = CFOP_STEPS[step_id]
    log = []
    func(cube, log)
    return " ".join(log), name