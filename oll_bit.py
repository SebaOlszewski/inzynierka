# oll_bit.py
import copy

# =========================================================================
# 1. GENEROWANIE BITOWEGO KLUCZA ORIENTACJI DLA WARSTWY U (12 BITÓW)
# =========================================================================
def get_oll_key(cube):
    """
    Zwraca 12-bitową liczbę całkowitą (0..4095) reprezentującą orientację
    4 narożników (2 bity każdy: 0, 1, 2) oraz 4 krawędzi (1 bit każdy: 0, 1) na warstwie U.
    Klucz == 0 oznacza pełne zorientowanie żółtej ścianki (OLL Skip).
    """
    # Narożniki UBL, UBR, UFR, UFL (sloty 0, 1, 2, 3)
    c0 = cube.get_corner(0)[1]
    c1 = cube.get_corner(1)[1]
    c2 = cube.get_corner(2)[1]
    c3 = cube.get_corner(3)[1]

    # Krawędzie UB, UR, UF, UL (sloty 0, 1, 2, 3)
    e0 = cube.get_edge(0)[1]
    e1 = cube.get_edge(1)[1]
    e2 = cube.get_edge(2)[1]
    e3 = cube.get_edge(3)[1]

    return (c0 << 10) | (c1 << 8) | (c2 << 6) | (c3 << 4) | (e0 << 3) | (e1 << 2) | (e2 << 1) | e3


# =========================================================================
# 2. BAZA WSZYSTKICH TWOICH 57 ALGORYTMÓW OLL (PRZEPISANA Z OLL.PY)
# =========================================================================
OLL_ALGS = [
    # Kropki (Dots)
    ("dot_1", "R U2 R2 F R F' U2 R' F R F'"),
    ("dot_2", "M R U M' R' U2 M R U2 R' U2 R U' M' R'"),
    ("dot_3", "M' R' R2 U R' U M R U2 M' R' U M"),
    ("dot_4", "M' U' M R U2 M' R' U' R U' R' M"),
    ("dot_5", "F R' F' R2 M' R' U R U' R' U' M"),
    ("dot_6", "R M U R' U R U2 R2 M2 U' R U' R' U2 R M"),
    ("dot_7", "M' R' R U R U R' U' M R' F R F'"),
    ("dot_8", "R M U R' U' M2 U R U' R' U' M"),

    # Kwadraty (Squares)
    ("square_1", "L' M U2 L U L' U L M'"),
    ("square_2", "M R U2 R' U' R U' M' R'"),

    # Błyskawice małe (Small Bolts)
    ("small_bolt_1", "M R U R' U R U2 M' R'"),
    ("small_bolt_2", "L' M U' L U' L' U2 L M'"),
    ("small_bolt_3", "M R U R' U R' F R F' R U2 M' R'"),
    ("small_bolt_4", "M R' U' R U' R' U2 R U' R M' R'"),

    # Rybki (Fishes)
    ("fish_1", "R U R' U' R' F R2 U R' U' F'"),
    ("fish_2", "R U R' U R' F R F' R U2 R'"),
    ("fish_3", "R U2 R2 F R F' R U2 R'"),
    ("fish_4", "F R' F' R U R U' R'"),

    # Ruchy skoczka (Knights)
    ("knight_move1", "F U R U' R2 F' R U R U' R'"),
    ("knight_move2", "R' F R U R' F' R F U' F'"),
    ("knight_move3", "L' M U' L M' L' U' L U L' M U L M'"),
    ("knight_move4", "M R U M' R' R U R' U' M R U' M' R'"),

    # Krzyże (Crosses)
    ("cross_1", "R U2 R' U' R U R' U' R U' R'"),
    ("cross_2", "R U2 R2 U' R2 U' R2 U2 R"),
    ("cross_3", "R2 D' R U2 R' D R U2 R"),
    ("cross_4", "M R U R' U' M' R' F R F'"),
    ("cross_5", "F' M R U R' U' R' M' F R"),
    ("cross_6", "R U2 R' U' R U' R'"),
    ("cross_7", "R U R' U R U2 R'"),

    # Orientacje narożników
    ("corners_oriented_1", "M R U R' U' M' R' R U R U' R'"),
    ("corners_oriented_2", "R U R' U' M U R U' M' R'"),

    # Kształty Awkward
    ("awkward_shape_1", "R U R' U' R U' R' F' U' F R U R'"),
    ("awkward_shape_2", "F R' F R2 U' R' U' R U R' F2"),
    ("awkward_shape_3", "R U R' U R U2 R' F R U R' U' F'"),
    ("awkward_shape_4", "R' U' R U' R' U2 R F R U R' U' F'"),

    # Kształty P
    ("p_shape_1", "R' U' F U R U' R' F' R"),
    ("p_shape_2", "L U F' U' L' U L F L'"),
    ("p_shape_3", "F' U' L' U L F"),
    ("p_shape_4", "F U R U' R' F'"),

    # Kształty T
    ("t_shape_1", "R U R' U' R' F R F'"),
    ("t_shape_2", "F R U R' U' F'"),

    # Kształty C
    ("c_shape_1", "R U R2 U' R' F R U R U' F'"),
    ("c_shape_2", "R' U' R' F R F' U R"),

    # Kształty W
    ("w_shape_1", "L' U' L U' L' U L U L F' L' F"),
    ("w_shape_2", "R U R' U R U' R' U' R' F R F'"),

    # Błyskawice duże (Big Lightnings)
    ("big_lightning_1", "L F' L' U' L U F U' L'"),
    ("big_lightning_2", "R' F R U R' U' F' U R"),

    # Kształty L
    ("l_shape_1", "R' U' R' F R F' R' F R F' U R"),
    ("l_shape_2", "F R U R' U' R U R' U' F'"),
    ("l_shape_3", "M R U' M2 R2 U M2 R2 U M2 R2 U' M R"),
    ("l_shape_4", "M' R' U M2 R2 U' M2 R2 U' M2 R2 U M' R'"),
    ("l_shape_5", "L' M U2 L U L' U' L U L' U L M'"),
    ("l_shape_6", "R M U2 R' U' R U R' U' R U' R' M'"),

    # Kształty I
    ("I_shape_1", "F U R U' R' U R U' R' F'"),
    ("I_shape_2", "R U R' U R U' B U' B' R'"),
    ("I_shape_3", "R' F R U R' U' R2 F' R2 U' R' U R U R'"),
    ("I_shape_4", "R' M' U' R M U' R' U R U' R' U R R' M' U R M"),
]


# =========================================================================
# 3. ODWRACANIE RUCHÓW DO AUTOMATYCZNEGO GENEROWANIA TABLICY HASZUJĄCEJ
# =========================================================================
def invert_move(m):
    """Zwraca odwrotność pojedynczego ruchu (np. R -> R', R' -> R, R2 -> R2)."""
    if m.endswith("2"):
        return m
    if m.endswith("'"):
        return m[:-1]
    return m + "'"

def invert_alg(alg_str):
    """Odwraca całą sekwencję algorytmu i kolejność ruchów."""
    moves = alg_str.split()
    return " ".join([invert_move(m) for m in reversed(moves)])


# =========================================================================
# 4. TABLICA OLL: KLUCZ BITOWY (12 BITÓW) -> NAZWA I SEKWENCJA RUCHÓW
# =========================================================================
OLL_LOOKUP_TABLE = {0x000: ("solved", "")}


def _initialize_oll_table():
    """
    Automatycznie mapuje każdy algorytm na jego unikalny 12-bitowy podpis stanu.
    Działa poprzez zaaplikowanie odwrotności algorytmu na ułożonej kostce.
    """
    from cube_bitboard import BitCube

    for name, alg in OLL_ALGS:
        inv_alg = invert_alg(alg)
        temp_cube = BitCube()
        
        # Wykonanie odwróconego algorytmu daje stan wejściowy dla OLL
        for m in inv_alg.split():
            temp_cube.apply_move(m)
            
        key = get_oll_key(temp_cube)
        if key not in OLL_LOOKUP_TABLE:
            OLL_LOOKUP_TABLE[key] = (name, alg)

# Budowanie słownika przy pierwszym imporcie modułu
_initialize_oll_table()


# =========================================================================
# 5. GŁÓWNA FUNKCJA SOLVERA OLL
# =========================================================================
def solve_oll(cube):
    """
    Rozpoznaje stan górnej warstwy, dobiera obrót AUF (U, U2, U') 
    i wykonuje poprawny algorytm OLL w BitCube.
    Zwraca ciąg wykonanych ruchów.
    """
    move_log = []

    for rotation_count in range(4):
        key = get_oll_key(cube)
        
        # OLL Skip – wszystko zorientowane
        if key == 0:
            return " ".join(move_log)

        if key in OLL_LOOKUP_TABLE:
            name, alg = OLL_LOOKUP_TABLE[key]
            if alg:
                for m in alg.split():
                    cube.apply_move(m)
                move_log.append(alg)
            return " ".join(move_log)

        # Dopasowanie kąta (AUF)
        cube.apply_move("U")
        move_log.append("U")

    return " ".join(move_log) + " [Nieznany układ OLL]"