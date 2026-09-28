# blind_bit.py
from cube_bitboard import BitCube

# =========================================================================
# STAŁE BITOWE STANU UŁOŻONEGO (60 BITÓW KRAWĘDZI, 40 BITÓW NAROŻNIKÓW)
# =========================================================================
SOLVED_EDGES = 0
for _i in range(12):
    SOLVED_EDGES |= (_i << 1) << (5 * _i)

SOLVED_CORNERS = 0
for _i in range(8):
    SOLVED_CORNERS |= (_i << 2) << (5 * _i)

EDGE_BUFFER_SLOT = 1    # 1: UR (litery B / M)
CORNER_BUFFER_SLOT = 0  # 0: UBL (litery A / E / S)


def _apply(cube, seq, move_list):
    """Aplikuje ciąg ruchów na obiekcie BitCube i dopisuje je do listy ruchów."""
    if not seq:
        return move_list
    for m in seq.split():
        cube.apply_move(m)
        move_list.append(m)
    return move_list


def _invert_alg(alg_str):
    """Zwraca odwrotność sekwencji ruchów (undo setup)."""
    if not alg_str:
        return ""
    inv = []
    for m in reversed(alg_str.split()):
        if m.endswith("2"):
            inv.append(m)
        elif m.endswith("'"):
            inv.append(m[:-1])
        else:
            inv.append(m + "'")
    return " ".join(inv)


# =========================================================================
# ALGORYTMY BAZOWE OLD POCHMANN (ODPOWIEDNIK BLIND_moves.py)
# =========================================================================
T_PERM_SEQ = "R U R' U' R' F R2 U' R' U' R U R' F'"
SWAP_CORNERS_SEQ = "R U' R' U' R U R' F' R U R' U' R' F R"


def T_perm(cube, move_list):
    return _apply(cube, T_PERM_SEQ, move_list)


def swap_corners(cube, move_list):
    return _apply(cube, SWAP_CORNERS_SEQ, move_list)


def _exec_edge_setup(cube, move_list, setup):
    move_list = _apply(cube, setup, move_list)
    move_list = T_perm(cube, move_list)
    move_list = _apply(cube, _invert_alg(setup), move_list)
    return move_list


def _exec_corner_setup(cube, move_list, setup):
    move_list = _apply(cube, setup, move_list)
    move_list = swap_corners(cube, move_list)
    move_list = _apply(cube, _invert_alg(setup), move_list)
    return move_list


# =========================================================================
# RUCHY DLA KRAWĘDZI (A - Z)
# =========================================================================
def edge_A(cube, move_list): return _exec_edge_setup(cube, move_list, "R2 U' R2")
def edge_B(cube, move_list): return move_list  # Bufor UR (U)
def edge_C(cube, move_list): return _exec_edge_setup(cube, move_list, "R2 U R2")
def edge_D(cube, move_list): return _exec_edge_setup(cube, move_list, "")
def edge_E(cube, move_list): return _exec_edge_setup(cube, move_list, "L2 D R F L' R'")
def edge_F(cube, move_list): return _exec_edge_setup(cube, move_list, "L D R F L' R'")
def edge_G(cube, move_list): return _exec_edge_setup(cube, move_list, "D R F L' R'")
def edge_H(cube, move_list): return _exec_edge_setup(cube, move_list, "L' D R F L' R'")
def edge_I(cube, move_list): return _exec_edge_setup(cube, move_list, "R F' L' R'")
def edge_J(cube, move_list): return _exec_edge_setup(cube, move_list, "U' F2 U L'")
def edge_K(cube, move_list): return _exec_edge_setup(cube, move_list, "R F L' R'")
def edge_L(cube, move_list): return _exec_edge_setup(cube, move_list, "L'")
def edge_M(cube, move_list): return move_list  # Bufor UR (R)
def edge_N(cube, move_list): return _exec_edge_setup(cube, move_list, "U B U'")
def edge_O(cube, move_list): return _exec_edge_setup(cube, move_list, "D' R F L' R'")
def edge_P(cube, move_list): return _exec_edge_setup(cube, move_list, "U' F' U")
def edge_R(cube, move_list): return _exec_edge_setup(cube, move_list, "R' B L R")
def edge_S(cube, move_list): return _exec_edge_setup(cube, move_list, "L")
def edge_T(cube, move_list): return _exec_edge_setup(cube, move_list, "R' B' L R")
def edge_U(cube, move_list): return _exec_edge_setup(cube, move_list, "U B2 U' L")
def edge_W(cube, move_list): return _exec_edge_setup(cube, move_list, "D' L2")
def edge_X(cube, move_list): return _exec_edge_setup(cube, move_list, "D2 L2")
def edge_Y(cube, move_list): return _exec_edge_setup(cube, move_list, "D L2")
def edge_Z(cube, move_list): return _exec_edge_setup(cube, move_list, "L2")


# =========================================================================
# RUCHY DLA NAROŻNIKÓW (A - Z)
# =========================================================================
def corner_A(cube, move_list): return move_list  # Bufor UBL (U)
def corner_B(cube, move_list): return _exec_corner_setup(cube, move_list, "R2")
def corner_C(cube, move_list): return _exec_corner_setup(cube, move_list, "F2 D")
def corner_D(cube, move_list): return _exec_corner_setup(cube, move_list, "F2")
def corner_E(cube, move_list): return move_list  # Bufor UBL (L)
def corner_F(cube, move_list): return _exec_corner_setup(cube, move_list, "F' D")
def corner_G(cube, move_list): return _exec_corner_setup(cube, move_list, "F'")
def corner_H(cube, move_list): return _exec_corner_setup(cube, move_list, "D' R")
def corner_I(cube, move_list): return _exec_corner_setup(cube, move_list, "F R'")
def corner_J(cube, move_list): return _exec_corner_setup(cube, move_list, "R'")
def corner_K(cube, move_list): return _exec_corner_setup(cube, move_list, "R' D'")
def corner_L(cube, move_list): return _exec_corner_setup(cube, move_list, "D2 R")
def corner_M(cube, move_list): return _exec_corner_setup(cube, move_list, "F")
def corner_N(cube, move_list): return _exec_corner_setup(cube, move_list, "R' F")
def corner_O(cube, move_list): return _exec_corner_setup(cube, move_list, "D' R' D'")
def corner_P(cube, move_list): return _exec_corner_setup(cube, move_list, "F D")
def corner_R(cube, move_list): return _exec_corner_setup(cube, move_list, "R D'")
def corner_S(cube, move_list): return move_list  # Bufor UBL (B)
def corner_T(cube, move_list): return _exec_corner_setup(cube, move_list, "D F'")
def corner_U(cube, move_list): return _exec_corner_setup(cube, move_list, "R")
def corner_W(cube, move_list): return _exec_corner_setup(cube, move_list, "D")
def corner_X(cube, move_list): return _exec_corner_setup(cube, move_list, "")
def corner_Y(cube, move_list): return _exec_corner_setup(cube, move_list, "D'")
def corner_Z(cube, move_list): return _exec_corner_setup(cube, move_list, "D2")


EDGE_FUNCS = {
    "A": edge_A, "B": edge_B, "C": edge_C, "D": edge_D,
    "E": edge_E, "F": edge_F, "G": edge_G, "H": edge_H,
    "I": edge_I, "J": edge_J, "K": edge_K, "L": edge_L,
    "M": edge_M, "N": edge_N, "O": edge_O, "P": edge_P,
    "R": edge_R, "S": edge_S, "T": edge_T, "U": edge_U,
    "W": edge_W, "X": edge_X, "Y": edge_Y, "Z": edge_Z,
}

CORNER_FUNCS = {
    "A": corner_A, "B": corner_B, "C": corner_C, "D": corner_D,
    "E": corner_E, "F": corner_F, "G": corner_G, "H": corner_H,
    "I": corner_I, "J": corner_J, "K": corner_K, "L": corner_L,
    "M": corner_M, "N": corner_N, "O": corner_O, "P": corner_P,
    "R": corner_R, "S": corner_S, "T": corner_T, "U": corner_U,
    "W": corner_W, "X": corner_X, "Y": corner_Y, "Z": corner_Z,
}


# =========================================================================
# TABLICE MAPOWANIA BITOWEGO (5-BITOWY KOD SLOTU -> LITERA)
# =========================================================================
# Mapuje 5-bitową wartość z bufora ((perm << 1) | ori dla krawędzi,
# (perm << 2) | ori dla narożników) bezpośrednio na odpowiadającą jej literę.
EDGE_BIT_TO_LETTER = {}
CORNER_BIT_TO_LETTER = {}


def _initialize_bit_tables():
    for letter, func in EDGE_FUNCS.items():
        if letter in ("B", "M"):
            continue
        tc = BitCube()
        func(tc, [])
        # Odczyt 5 bitów ze slotu bufora krawędzi (slot 1: UR)
        bit_val = (tc.edges >> (5 * EDGE_BUFFER_SLOT)) & 0x1F
        EDGE_BIT_TO_LETTER[bit_val] = letter

    for letter, func in CORNER_FUNCS.items():
        if letter in ("A", "E", "S"):
            continue
        tc = BitCube()
        func(tc, [])
        # Odczyt 5 bitów ze slotu bufora narożników (slot 0: UBL)
        bit_val = (tc.corners >> (5 * CORNER_BUFFER_SLOT)) & 0x1F
        CORNER_BIT_TO_LETTER[bit_val] = letter


_initialize_bit_tables()


def _find_unsolved_edge_letter(edges_bits):
    """Zwraca literę pierwszego nieułożonego slotu krawędzi (zrywanie cyklu)."""
    for slot in range(12):
        if slot == EDGE_BUFFER_SLOT:
            continue
        val = (edges_bits >> (5 * slot)) & 0x1F
        if val != (slot << 1):
            return EDGE_BIT_TO_LETTER[slot << 1]
    return None


def _find_unsolved_corner_letter(corners_bits):
    """Zwraca literę pierwszego nieułożonego slotu narożnika (zrywanie cyklu)."""
    for slot in range(1, 8):
        val = (corners_bits >> (5 * slot)) & 0x1F
        if val != (slot << 2):
            return CORNER_BIT_TO_LETTER[slot << 2]
    return None


# =========================================================================
# GŁÓWNE FUNKCJE UKŁADAJĄCE (ODPOWIEDNIK BLIND.py NA BITACH)
# =========================================================================
def solve_edges(cube, move_list, memo_edges=None):
    steps = 0
    while cube.edges != SOLVED_EDGES:
        if steps > 30:
            raise RuntimeError("Przekroczono limit kroków podczas układania krawędzi BLIND.")

        buf_val = (cube.edges >> (5 * EDGE_BUFFER_SLOT)) & 0x1F
        buf_perm = buf_val >> 1

        if buf_perm == EDGE_BUFFER_SLOT:
            current_letter = _find_unsolved_edge_letter(cube.edges)
            if current_letter is None:
                break
        else:
            current_letter = EDGE_BIT_TO_LETTER[buf_val]

        if memo_edges is not None:
            memo_edges.append(current_letter)

        move_list = EDGE_FUNCS[current_letter](cube, move_list)
        steps += 1

    return move_list


def solve_corners(cube, move_list, memo_corners=None):
    steps = 0
    while cube.corners != SOLVED_CORNERS:
        if steps > 30:
            raise RuntimeError("Przekroczono limit kroków podczas układania narożników BLIND.")

        buf_val = (cube.corners >> (5 * CORNER_BUFFER_SLOT)) & 0x1F
        buf_perm = buf_val >> 2

        if buf_perm == CORNER_BUFFER_SLOT:
            current_letter = _find_unsolved_corner_letter(cube.corners)
            if current_letter is None:
                break
        else:
            current_letter = CORNER_BIT_TO_LETTER[buf_val]

        if memo_corners is not None:
            memo_corners.append(current_letter)

        move_list = CORNER_FUNCS[current_letter](cube, move_list)
        steps += 1

    return move_list


def solve_blind(cube, move_list):
    move_list = solve_edges(cube, move_list)
    move_list = solve_corners(cube, move_list)
    return move_list


# =========================================================================
# KLASA INTERFEJSU WYMAGANA PRZEZ MAIN.PY
# =========================================================================
class OptimizedBlindSolver:
    def solve_edges_only(self, cube, log):
        memo_edges = []
        solve_edges(cube, log, memo_edges)
        return "".join(memo_edges)

    def solve_corners_only(self, cube, log):
        memo_corners = []
        solve_corners(cube, log, memo_corners)
        return "".join(memo_corners)

    def solve(self, cube, log):
        memo_edges = []
        memo_corners = []
        solve_edges(cube, log, memo_edges)
        solve_corners(cube, log, memo_corners)
        return {
            "edges": "".join(memo_edges),
            "corners": "".join(memo_corners),
        }