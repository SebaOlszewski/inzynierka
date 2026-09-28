# f2l_bit.py
from cube_bitboard import BitCube

# Definicja 4 slotów F2L: (id_slotu, corner_slot, edge_slot, wypychacz_narożnika, wypychacz_krawędzi)
F2L_SLOTS = [
    (0, 5, 4, "R U R'", "R U' R' U' F' U F"),  # FR (DFR=5, FR=4)
    (1, 4, 5, "F U F'", "F U' F' U' L' U L"),  # FL (DFL=4, FL=5)
    (2, 7, 6, "L U L'", "L U' L' U' B' U B"),  # BL (DBL=7, BL=6)
    (3, 6, 7, "B U B'", "B U' B' U' R' U R"),  # BR (DBR=6, BR=7)
]

# Mapa obrotu ścian o 90 stopni wokół osi U-D (FR -> FL -> BL -> BR)
ROTATE_FACE_MAP = {
    "R": "F", "F": "L", "L": "B", "B": "R",
    "U": "U", "D": "D"
}

# =========================================================================
# BAZA 41 KANONICZNYCH ALGORYTMÓW F2L DLA SLOTU FR (CORNER 5, EDGE 4)
# =========================================================================
F2L_FR_ALGS = [
    # 1-4: Podstawowe wstawienia (Basic Inserts)
    "U R U' R'",
    "U' F' U F",
    "F' U' F",
    "R U R'",

    # 5-12: Rozdzielone pary w warstwie U - biały na boku
    "U' R U R' U2 R U' R'",
    "U F' U' F U2 F' U F",
    "U' R U2 R' U2 R U' R'",
    "U F' U2 F U2 F' U F",
    "U' R U' R' U F' U' F",
    "U F' U F U' R U R'",
    "U' R U2 R' U F' U' F",
    "U F' U2 F U' R U R'",

    # 13-16: Połączone pary w warstwie U - biały na boku
    "U F' U F U' F' U' F",
    "U' R U' R' U R U R'",
    "R U' R' U2 F' U' F",
    "F' U F U2 R U R'",

    # 17-24: Narożnik w warstwie U - biały skierowany do góry (U)
    "R U2 R' U' R U R'",
    "F' U2 F U F' U' F",
    "U R U2 R' U R U' R'",
    "U' F' U2 F U' F' U F",
    "U2 R U R' U R U' R'",
    "U2 F' U' F U' F' U F",
    "R U R' U2 R U R' U' R U R'",
    "F' U' F U2 F' U' F U F' U' F",

    # 25-30: Narożnik w slocie DFR (5), krawędź w warstwie U
    "U' F' U F U R U' R'",
    "U R U' R' U' F' U F",
    "R U' R' U R U' R'",
    "F' U F U' F' U F",
    "F' U' F U F' U' F",
    "R U R' U' R U R'",

    # 31-36: Narożnik w warstwie U, krawędź w slocie FR (4)
    "R U' R' U F' U F",
    "R U R' U' R U R' U' R U R'",
    "U' R U' R' U2 R U' R'",
    "U R U R' U2 R U R'",
    "U' R U R' U F' U' F",
    "U F' U' F U' R U R'",

    # 37-41: Oba elementy w slocie FR (5 i 4), ale źle zorientowane
    "R U' R' U' R U R' U2 F' U' F",
    "R U' R' U' R U R' U' R U2 R'",
    "R U' R' U R U2 R' U R U' R'",
    "R U R' U' R U' R' U2 F' U' F",
    "R U2 R' U' R U R' U' R U' R'",
]


def _rotate_alg(alg_str, times):
    """Transponuje algorytm ze slotu FR na inny slot poprzez obrót ścian bocznych."""
    res = []
    for m in alg_str.split():
        base = m[0]
        mod = m[1:]
        for _ in range(times):
            base = ROTATE_FACE_MAP[base]
        res.append(base + mod)
    return " ".join(res)


def _invert_move(m):
    if m.endswith("2"):
        return m
    if m.endswith("'"):
        return m[:-1]
    return m + "'"


def _invert_alg(alg_str):
    return " ".join([_invert_move(m) for m in reversed(alg_str.split())])


def get_f2l_pair_key(cube, target_corner, target_edge):
    """
    Zwraca 10-bitowy klucz określający położenie i orientację szukanej pary (narożnik + krawędź):
    bity 9..7: aktualny slot narożnika (0..7)
    bity 6..5: orientacja narożnika (0..2)
    bity 4..1: aktualny slot krawędzi (0..11)
    bit  0   : orientacja krawędzi (0..1)
    """
    c_slot, c_ori = 0, 0
    for s in range(8):
        p, o = cube.get_corner(s)
        if p == target_corner:
            c_slot, c_ori = s, o
            break

    e_slot, e_ori = 0, 0
    for s in range(12):
        p, o = cube.get_edge(s)
        if p == target_edge:
            e_slot, e_ori = s, o
            break

    return (c_slot << 7) | (c_ori << 5) | (e_slot << 1) | e_ori


def _is_cross_and_other_slots_intact(cube, active_c, active_e):
    """Sprawdza na bitach, czy krzyż oraz pozostałe 3 sloty F2L są nienaruszone."""
    for e in (8, 9, 10, 11):
        if cube.get_edge(e) != (e, 0):
            return False
    for _, c_idx, e_idx, _, _ in F2L_SLOTS:
        if c_idx != active_c and cube.get_corner(c_idx) != (c_idx, 0):
            return False
        if e_idx != active_e and cube.get_edge(e_idx) != (e_idx, 0):
            return False
    return True


# Słownik tablic przeglądowych dla każdego z 4 slotów: F2L_LOOKUP[slot_id][10_bit_key] = alg_str
F2L_LOOKUP = {0: {}, 1: {}, 2: {}, 3: {}}


def _initialize_f2l_tables():
    auf_Check = ["", "U", "U2", "U'"]
    for slot_id, c_idx, e_idx, _, _ in F2L_SLOTS:
        solved_key = (c_idx << 7) | (0 << 5) | (e_idx << 1) | 0
        F2L_LOOKUP[slot_id][solved_key] = ""

        for base_alg in F2L_FR_ALGS:
            rotated_alg = _rotate_alg(base_alg, slot_id)
            for auf in auf_Check:
                full_alg = f"{auf} {rotated_alg}".strip()
                inv_alg = _invert_alg(full_alg)

                tc = BitCube()
                for m in inv_alg.split():
                    tc.apply_move(m)

                if not _is_cross_and_other_slots_intact(tc, c_idx, e_idx):
                    continue

                key = get_f2l_pair_key(tc, c_idx, e_idx)
                # Zapisz najkrótszy algorytm dla danego klucza bitowego
                if key not in F2L_LOOKUP[slot_id] or len(full_alg.split()) < len(F2L_LOOKUP[slot_id][key].split()):
                    F2L_LOOKUP[slot_id][key] = full_alg


_initialize_f2l_tables()


def _apply_seq(cube, seq, log):
    if not seq:
        return
    for m in seq.split():
        cube.apply_move(m)
        log.append(m)


def solve_f2l_pair(cube, slot_id, log):
    """Układa pojedynczą parę F2L używając 10-bitowej tablicy haszującej."""
    _, c_idx, e_idx, c_eject, _ = F2L_SLOTS[slot_id]
    solved_key = (c_idx << 7) | (0 << 5) | (e_idx << 1) | 0

    for _ in range(4):
        key = get_f2l_pair_key(cube, c_idx, e_idx)
        if key == solved_key:
            return

        # 1. Jeśli para jest w warstwie U lub we własnym slocie -> O(1) lookup!
        if key in F2L_LOOKUP[slot_id]:
            _apply_seq(cube, F2L_LOOKUP[slot_id][key], log)
            return

        # 2. Jeśli narożnik lub krawędź utknęły w INNYM slocie F2L -> wypchnij na warstwę U
        c_slot = (key >> 7) & 0x07
        e_slot = (key >> 1) & 0x0F

        if c_slot in (4, 5, 6, 7) and c_slot != c_idx:
            # Znajdź wypychacz dla obcego slotu narożnika
            for _, other_c, _, other_c_eject, _ in F2L_SLOTS:
                if other_c == c_slot:
                    _apply_seq(cube, other_c_eject, log)
                    break
            continue

        if e_slot in (4, 5, 6, 7) and e_slot != e_idx:
            # Krawędź jest w obcym slocie środkowym -> wypchnij ją 3 ruchami (np. R U R')
            for _, _, other_e, other_c_eject, _ in F2L_SLOTS:
                if other_e == e_slot:
                    _apply_seq(cube, other_c_eject, log)
                    break
            continue

        # 3. Jeśli oba są we własnym slocie w rzadkiej konfiguracji, wypchnij na górę
        _apply_seq(cube, c_eject, log)


def solve_full_f2l(cube, log):
    """Układa wszystkie 4 pary F2L (FR, FL, BL, BR) bezpośrednio z tablic bitowych."""
    for slot_id in range(4):
        solve_f2l_pair(cube, slot_id, log)