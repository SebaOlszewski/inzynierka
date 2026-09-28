# oll_bit.py
from cube_bitboard import BitCube


def get_oll_key(cube):
    """
    Zwraca 12-bitową liczbę całkowitą (0..4095) reprezentującą orientację
    4 narożników (2 bity każdy: 0, 1, 2) oraz 4 krawędzi (1 bit każdy: 0, 1) na warstwie U.
    Klucz == 0 oznacza pełne zorientowanie żółtej ścianki (OLL Skip).
    """
    c0 = cube.get_corner(0)[1]
    c1 = cube.get_corner(1)[1]
    c2 = cube.get_corner(2)[1]
    c3 = cube.get_corner(3)[1]

    e0 = cube.get_edge(0)[1]
    e1 = cube.get_edge(1)[1]
    e2 = cube.get_edge(2)[1]
    e3 = cube.get_edge(3)[1]

    return (c0 << 10) | (c1 << 8) | (c2 << 6) | (c3 << 4) | (e0 << 3) | (e1 << 2) | (e2 << 1) | e3


OLL_ALGS = [
    # Czyste algorytmy 2-gen / 3-gen zachowujące F2L na BitCube (bez ruchów M)
    ("dot_1", "R U2 R2 F R F' U2 R' F R F'"),
    ("dot_2_clean", "F R U R' U' F' U2 F R U R' U' F'"),
    ("dot_3_clean", "F R U R' U' F' U F R U R' U' F'"),
    ("dot_4_clean", "F R U R' U' F' U2 R U2 R' U' R U' R'"),
    ("awkward_wave_5", "R U2 R' F R' F' R U2 R'"),
    ("antisune_back", "R' U2 R U R' U R"),
    ("collar", "R2 D' R U R' D R2 U' R U' R'"),
    ("antisune", "R U2 R' U' R U' R'"),
    ("small_bolt_9", "R U R' U R' F R F' U2 R' F R F'"),
    ("small_bolt_10", "R' U' R' F R F' U R U R' U' R"),
    ("l_shape_2", "F R U R' U' R U R' U' F'"),
    ("sune", "R U R' U R U2 R'"),
    ("knight_move1", "F U R U' R2 F' R U R U' R'"),
    ("knight_move2", "R' F R U R' F' R F U' F'"),
    ("c_shape_2", "R' U' R' F R F' U R"),
    ("small_l_15", "R' U2 R F R' F' U2 R"),
    ("ub_oll", "R2 U R U R' U' R' U' R' U R'"),
    ("cross_1", "R U2 R' U' R U R' U' R U' R'"),
    ("cross_2", "R U2 R2 U' R2 U' R2 U2 R"),
    ("cross_3", "R2 D' R U2 R' D R U2 R"),
    ("t_shape_1", "R U R' U' R' F R F'"),
    ("t_shape_2", "F R U R' U' F'"),
    ("p_shape_1", "R' U' F U R U' R' F' R"),
    ("p_shape_2", "L U F' U' L' U L F L'"),
    ("p_shape_3", "F' U' L' U L F"),
    ("p_shape_4", "F U R U' R' F'"),
    ("c_shape_1", "R U R2 U' R' F R U R U' F'"),
    ("fish_1", "R U R' U' R' F R2 U R' U' F'"),
    ("fish_2", "R U R' U R' F R F' R U2 R'"),
    ("fish_3", "R U2 R2 F R F' R U2 R'"),
    ("fish_4", "F R' F' R U R U' R'"),
    ("w_shape_1", "L' U' L U' L' U L U L F' L' F"),
    ("w_shape_2", "R U R' U R U' R' U' R' F R F'"),
    ("fish_37", "F R U' R' U' R U R' F'"),
    ("fish_38", "F R U R' U' R U R' F'"),
    ("big_lightning_1", "L F' L' U' L U F U' L'"),
    ("big_lightning_2", "R' F R U R' U' F' U R"),
    ("awkward_shape_1", "R U R' U' R U' R' F' U' F R U R'"),
    ("awkward_shape_2", "F R' F R2 U' R' U' R U R' F2"),
    ("awkward_shape_3", "R U R' U R U2 R' F R U R' U' F'"),
    ("awkward_shape_4", "R' U' R U' R' U2 R F R U R' U' F'"),
    ("l_shape_1", "R' U' R' F R F' R' F R F' U R"),
    ("l_shape_49", "R B' R' U' R U B U' R'"),
    ("I_shape_1", "F U R U' R' U R U' R' F'"),
    ("I_shape_2", "R U R' U R U' B U' B' R'"),
    ("I_shape_3", "R' F R U R' U' R2 F' R2 U' R' U R U R'"),
    ("I_shape_55", "R' F R U R U' R2 F' R2 U R' U' R' F R F'"),
    ("I_shape_56", "F R U R' U' R U R' U' R U R' U' F'"),
]


def invert_move(m):
    if m.endswith("2"):
        return m
    if m.endswith("'"):
        return m[:-1]
    return m + "'"


def invert_alg(alg_str):
    moves = alg_str.split()
    return " ".join([invert_move(m) for m in reversed(moves)])


def _is_f2l_intact(cube):
    """Sprawdza na bitach, czy dwie pierwsze warstwy (krawędzie 4..11 i narożniki 4..7) są nienaruszone."""
    for e in range(4, 12):
        if cube.get_edge(e) != (e, 0):
            return False
    for c in range(4, 8):
        if cube.get_corner(c) != (c, 0):
            return False
    return True


OLL_LOOKUP_TABLE = {0x000: ("solved", "")}


def _initialize_oll_table():
    for name, alg in OLL_ALGS:
        inv_alg = invert_alg(alg)
        temp_cube = BitCube()
        for m in inv_alg.split():
            temp_cube.apply_move(m)

        # Rejestrujemy wyłącznie algorytmy, które nie naruszają F2L i po wykonaniu dają klucz 0
        if not _is_f2l_intact(temp_cube):
            continue

        key = get_oll_key(temp_cube)
        verify_cube = BitCube()
        verify_cube.edges = temp_cube.edges
        verify_cube.corners = temp_cube.corners
        for m in alg.split():
            verify_cube.apply_move(m)

        if get_oll_key(verify_cube) == 0 and _is_f2l_intact(verify_cube):
            if key not in OLL_LOOKUP_TABLE:
                OLL_LOOKUP_TABLE[key] = (name, alg)


_initialize_oll_table()


def solve_oll(cube):
    """
    Rozpoznaje stan górnej warstwy po 12-bitowym kluczu, dobiera obrót U
    i wykonuje algorytm OLL z tablicy haszującej.
    Zwraca ciąg wykonanych ruchów (lub pusty ciąg, jeśli układ wymaga 2-Look OLL).
    """
    if get_oll_key(cube) == 0:
        return ""

    auf_moves = ["", "U", "U2", "U'"]
    for auf in auf_moves:
        test_cube = BitCube()
        test_cube.edges = cube.edges
        test_cube.corners = cube.corners
        if auf:
            test_cube.apply_move(auf)

        key = get_oll_key(test_cube)
        if key in OLL_LOOKUP_TABLE:
            _, alg = OLL_LOOKUP_TABLE[key]
            seq = f"{auf} {alg}".strip()
            for m in seq.split():
                cube.apply_move(m)
            return seq

    return ""