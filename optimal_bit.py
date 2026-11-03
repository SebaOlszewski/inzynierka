# optimal_bit.py
import gc
from collections import deque
from cube_bitboard import BitCube

ALL_MOVES = [
    "U", "U'", "U2", "D", "D'", "D2",
    "R", "R'", "R2", "L", "L'", "L2",
    "F", "F'", "F2", "B", "B'", "B2"
]

G1_MOVES = [
    "U", "U'", "U2", "D", "D'", "D2",
    "R2", "L2", "F2", "B2"
]

OPPOSITE_FACE = {"U": "D", "D": "U", "R": "L", "L": "R", "F": "B", "B": "F"}
CANONICAL_FIRST = {"U", "R", "F"}


def _invert_move(m):
    if m.endswith("2"):
        return m
    if m.endswith("'"):
        return m[:-1]
    return m + "'"


def _invert_path(path):
    return [_invert_move(m) for m in reversed(path)]


def _can_append_move(last_move, next_move):
    if not last_move:
        return True
    f1, f2 = last_move[0], next_move[0]
    if f1 == f2:
        return False
    if OPPOSITE_FACE.get(f1) == f2 and f1 not in CANONICAL_FIRST:
        return False
    return True


def _cancel_moves(moves_list):
    stack = []
    for m in moves_list:
        if not m:
            continue
        face = m[0]
        turns = 2 if m.endswith("2") else (3 if m.endswith("'") else 1)
        if stack and stack[-1][0] == face:
            prev_face, prev_turns = stack.pop()
            total = (prev_turns + turns) % 4
            if total != 0:
                stack.append((face, total))
        else:
            stack.append((face, turns))

    suffix = {1: "", 2: "2", 3: "'"}
    return [f"{face}{suffix[t]}" for face, t in stack]


def _apply_on_raw_state(edges, corners, move_str):
    tc = BitCube.__new__(BitCube)
    tc.edges = edges
    tc.corners = corners
    tc.apply_move(move_str)
    return tc.edges, tc.corners


# =========================================================================
# WSPÓŁRZĘDNE BITOWE DLA DRZEWA WSTECZNEGO (OD UŁOŻONEJ KOSTKI)
# =========================================================================
def _get_p1_subkeys(edges, corners):
    eo = 0
    slice_mask = 0
    for s in range(12):
        val = (edges >> (5 * s)) & 0x1F
        perm, ori = val >> 1, val & 1
        eo |= (ori << s)
        if 4 <= perm <= 7:
            slice_mask |= (1 << s)

    co = 0
    for s in range(8):
        ori = (corners >> (5 * s)) & 0x03
        co |= (ori << (2 * s))

    eo_slice = (slice_mask << 12) | eo
    co_slice = (slice_mask << 16) | co
    full_key = (slice_mask << 28) | (co << 12) | eo
    return eo_slice, co_slice, full_key


def _get_p2_subkeys(edges, corners):
    e_slice = (edges >> 20) & 0xFFFFF  
    c_key = (corners << 20) | e_slice
    ud_edges = (edges & 0xFFFFF) | ((edges >> 20) & ~0xFFFFF)
    return c_key, ud_edges


SOLVED_CUBE = BitCube()
SOLVED_STATE = (SOLVED_CUBE.edges, SOLVED_CUBE.corners)
SOLVED_EO_SLICE, SOLVED_CO_SLICE, SOLVED_G1_KEY = _get_p1_subkeys(SOLVED_CUBE.edges, SOLVED_CUBE.corners)
SOLVED_P2_C, SOLVED_P2_E = _get_p2_subkeys(SOLVED_CUBE.edges, SOLVED_CUBE.corners)

# Tablice inicjowane jako puste na starcie programu
G1_BACKWARD_TABLE = {}
PHASE2_BACKWARD_TABLE = {}
BWD_EO_DIST = {}
BWD_CO_DIST = {}
BWD_P2_C_DIST = {}
BWD_P2_E_DIST = {}


def _build_backward_trees():
    global G1_BACKWARD_TABLE, PHASE2_BACKWARD_TABLE, BWD_EO_DIST, BWD_CO_DIST, BWD_P2_C_DIST, BWD_P2_E_DIST
    
    # Jeśli tablica jest pełna, pomiń budowanie (zabezpieczenie na kolejne kostki)
    if G1_BACKWARD_TABLE:
        return

    G1_BACKWARD_TABLE[SOLVED_G1_KEY] = []
    PHASE2_BACKWARD_TABLE[SOLVED_STATE] = []
    BWD_EO_DIST[SOLVED_EO_SLICE] = 0
    BWD_CO_DIST[SOLVED_CO_SLICE] = 0
    BWD_P2_C_DIST[SOLVED_P2_C] = 0
    BWD_P2_E_DIST[SOLVED_P2_E] = 0

    # 1. Dokładne drzewo wsteczne dla Fazy 1 (głębokość 6)
    q_g1 = deque([(SOLVED_CUBE.edges, SOLVED_CUBE.corners, [])])
    while q_g1:
        e, c, path = q_g1.popleft()
        d = len(path)
        if d >= 6:
            continue
        last_m = path[-1] if path else None
        for m in ALL_MOVES:
            if not _can_append_move(last_m, m):
                continue
            ne, nc = _apply_on_raw_state(e, c, m)
            eo_s, co_s, fk = _get_p1_subkeys(ne, nc)
            new_path = path + [m]
            if fk not in G1_BACKWARD_TABLE:
                G1_BACKWARD_TABLE[fk] = new_path
                q_g1.append((ne, nc, new_path))
            if eo_s not in BWD_EO_DIST:
                BWD_EO_DIST[eo_s] = d + 1
            if co_s not in BWD_CO_DIST:
                BWD_CO_DIST[co_s] = d + 1

    # Rozszerzenie pomocniczych drzew wstecznych orientacji do głębokości 7
    q_eo = deque([(SOLVED_CUBE.edges, SOLVED_CUBE.corners, 0)])
    visited_eo = {SOLVED_EO_SLICE}
    while q_eo:
        e, c, d = q_eo.popleft()
        if d >= 7:
            continue
        for m in ALL_MOVES:
            ne, nc = _apply_on_raw_state(e, c, m)
            eo_s, _, _ = _get_p1_subkeys(ne, nc)
            if eo_s not in visited_eo:
                visited_eo.add(eo_s)
                BWD_EO_DIST[eo_s] = d + 1
                q_eo.append((ne, nc, d + 1))

    q_co = deque([(SOLVED_CUBE.edges, SOLVED_CUBE.corners, 0)])
    visited_co = {SOLVED_CO_SLICE}
    while q_co:
        e, c, d = q_co.popleft()
        if d >= 7:
            continue
        for m in ALL_MOVES:
            ne, nc = _apply_on_raw_state(e, c, m)
            _, co_s, _ = _get_p1_subkeys(ne, nc)
            if co_s not in visited_co:
                visited_co.add(co_s)
                BWD_CO_DIST[co_s] = d + 1
                q_co.append((ne, nc, d + 1))

    # 2. Drzewo wsteczne dla Fazy 2 (głębokość 8)
    q_p2 = deque([(SOLVED_CUBE.edges, SOLVED_CUBE.corners, [])])
    while q_p2:
        e, c, path = q_p2.popleft()
        d = len(path)
        if d >= 8:
            continue
        last_m = path[-1] if path else None
        for m in G1_MOVES:
            if not _can_append_move(last_m, m):
                continue
            ne, nc = _apply_on_raw_state(e, c, m)
            st = (ne, nc)
            ck, ek = _get_p2_subkeys(ne, nc)
            new_path = path + [m]
            if st not in PHASE2_BACKWARD_TABLE:
                PHASE2_BACKWARD_TABLE[st] = new_path
                q_p2.append((ne, nc, new_path))
            if ck not in BWD_P2_C_DIST:
                BWD_P2_C_DIST[ck] = d + 1
            if ek not in BWD_P2_E_DIST:
                BWD_P2_E_DIST[ek] = d + 1


def free_tables():
    """Zwalnia całą zarezerwowaną pamięć i wymusza usunięcie jej z RAM-u systemu."""
    G1_BACKWARD_TABLE.clear()
    PHASE2_BACKWARD_TABLE.clear()
    BWD_EO_DIST.clear()
    BWD_CO_DIST.clear()
    BWD_P2_C_DIST.clear()
    BWD_P2_E_DIST.clear()
    gc.collect()


# =========================================================================
# SZYBKIE SPOTKANIE DRZEW POŚRODKU (DWUKIERUNKOWY IDA* / MEET-IN-THE-MIDDLE)
# =========================================================================
def _search_p1_meet(e, c, depth_left, last_m, path):
    eo_s, co_s, fk = _get_p1_subkeys(e, c)
    if fk in G1_BACKWARD_TABLE:
        bwd_tail = G1_BACKWARD_TABLE[fk]
        if len(bwd_tail) <= depth_left:
            return _cancel_moves(path + _invert_path(bwd_tail))

    if depth_left == 0:
        return None

    h = max(BWD_EO_DIST.get(eo_s, 7), BWD_CO_DIST.get(co_s, 7))
    if h > depth_left:
        return None

    for m in ALL_MOVES:
        if not _can_append_move(last_m, m):
            continue
        ne, nc = _apply_on_raw_state(e, c, m)
        res = _search_p1_meet(ne, nc, depth_left - 1, m, path + [m])
        if res is not None:
            return res
    return None


def _search_p2_meet(e, c, depth_left, last_m, path):
    st = (e, c)
    if st in PHASE2_BACKWARD_TABLE:
        bwd_tail = PHASE2_BACKWARD_TABLE[st]
        if len(bwd_tail) <= depth_left:
            return _cancel_moves(path + _invert_path(bwd_tail))

    if depth_left == 0:
        return None

    ck, ek = _get_p2_subkeys(e, c)
    h = max(BWD_P2_C_DIST.get(ck, 7), BWD_P2_E_DIST.get(ek, 7))
    if h > depth_left:
        return None

    for m in G1_MOVES:
        if not _can_append_move(last_m, m):
            continue
        ne, nc = _apply_on_raw_state(e, c, m)
        res = _search_p2_meet(ne, nc, depth_left - 1, m, path + [m])
        if res is not None:
            return res
    return None


class BidirectionalOptimalSolver:
    def solve(self, cube, log):
        # Dynamicznie ładuje tablice tylko przy wejściu do układania
        _build_backward_trees()

        p1_moves = None
        for limit in range(13):
            p1_moves = _search_p1_meet(cube.edges, cube.corners, limit, None, [])
            if p1_moves is not None:
                break

        if p1_moves is None:
            raise RuntimeError("Faza 1 Bidirectional Search nie znalazła spotkania.")

        e_mid, c_mid = cube.edges, cube.corners
        for m in p1_moves:
            e_mid, c_mid = _apply_on_raw_state(e_mid, c_mid, m)

        p2_moves = None
        for limit in range(19):
            p2_moves = _search_p2_meet(e_mid, c_mid, limit, None, [])
            if p2_moves is not None:
                break

        if p2_moves is None:
            raise RuntimeError("Faza 2 Bidirectional Search nie znalazła spotkania.")

        full_solution = _cancel_moves(p1_moves + p2_moves)
        for m in full_solution:
            cube.apply_move(m)
            log.append(m)

        return full_solution