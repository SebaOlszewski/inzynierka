# lbl_bit.py

def _apply(cube, seq, log):
    if not seq:
        return
    moves = seq.split()
    for m in moves:
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

# =========================================================================
# 1. BIAŁY KRZYŻ
# =========================================================================
def solve_white_cross(cube, log):
    # Krawędzie białego krzyża: 8 (DF), 9 (DR), 10 (DB), 11 (DL)
    targets = [8, 9, 10, 11]
    top_slots = {8: 2, 9: 1, 10: 0, 11: 3}

    for target in targets:
        for _ in range(12):
            slot, ori = _find_edge(cube, target)
            if slot == target and ori == 0:
                break

            # Jeśli na dolnej warstwie
            if slot == 8: _apply(cube, "F2", log)
            elif slot == 9: _apply(cube, "R2", log)
            elif slot == 10: _apply(cube, "B2", log)
            elif slot == 11: _apply(cube, "L2", log)

            # Jeśli na środkowej warstwie
            elif slot == 4: _apply(cube, "R U R'", log)
            elif slot == 5: _apply(cube, "L' U' L", log)
            elif slot == 6: _apply(cube, "L U L'", log)
            elif slot == 7: _apply(cube, "R' U' R", log)

            # Jeśli na górnej warstwie (0..3)
            elif slot in [0, 1, 2, 3]:
                needed = top_slots[target]
                while slot != needed:
                    _apply(cube, "U", log)
                    slot, ori = _find_edge(cube, target)

                if target == 8:
                    _apply(cube, "F2" if ori == 0 else "U' R' F R", log)
                elif target == 9:
                    _apply(cube, "R2" if ori == 0 else "U' B' R B", log)
                elif target == 10:
                    _apply(cube, "B2" if ori == 0 else "U' L' B L", log)
                elif target == 11:
                    _apply(cube, "L2" if ori == 0 else "U' F' L F", log)
                break

# =========================================================================
# 2. NAROŻNIKI 1. WARSTWY
# =========================================================================
def solve_first_layer_corners(cube, log):
    # Narożniki: 4 (DFL), 5 (DFR), 6 (DBR), 7 (DBL)
    targets = [4, 5, 6, 7]
    top_slots = {4: 3, 5: 2, 6: 1, 7: 0}

    for target in targets:
        for _ in range(16):
            slot, ori = _find_corner(cube, target)
            if slot == target and ori == 0:
                break

            if slot == 5: _apply(cube, "R U R' U'", log)
            elif slot == 4: _apply(cube, "F U F' U'", log)
            elif slot == 6: _apply(cube, "B U B' U'", log)
            elif slot == 7: _apply(cube, "L U L' U'", log)

            elif slot in [0, 1, 2, 3]:
                needed = top_slots[target]
                while slot != needed:
                    _apply(cube, "U", log)
                    slot, ori = _find_corner(cube, target)

                while not (cube.get_corner(target)[0] == target and cube.get_corner(target)[1] == 0):
                    if target == 5: _apply(cube, "R U R' U'", log)
                    elif target == 4: _apply(cube, "F U F' U'", log)
                    elif target == 6: _apply(cube, "B U B' U'", log)
                    elif target == 7: _apply(cube, "L U L' U'", log)
                break

# =========================================================================
# 3. DRUGA WARSTWA (MIDDLE LAYER)
# =========================================================================
def solve_middle_layer(cube, log):
    # Krawędzie: 4 (FR), 5 (FL), 6 (BL), 7 (BR)
    targets = [4, 5, 6, 7]

    for target in targets:
        for _ in range(16):
            slot, ori = _find_edge(cube, target)
            if slot == target and ori == 0:
                break

            # Wypchnięcie jeśli tkwi w złym slocie środkowym
            if slot == 4: _apply(cube, "U R U' R' U' F' U F", log)
            elif slot == 5: _apply(cube, "U' L' U L U F U' F'", log)
            elif slot == 6: _apply(cube, "U' L' U L U B U' B'", log)
            elif slot == 7: _apply(cube, "U R U' R' U' B' U B", log)

            elif slot in [0, 1, 2, 3]:
                if target == 4:  # FR
                    if ori == 0:
                        while _find_edge(cube, target)[0] != 2: _apply(cube, "U", log)
                        _apply(cube, "U R U' R' U' F' U F", log)
                    else:
                        while _find_edge(cube, target)[0] != 1: _apply(cube, "U", log)
                        _apply(cube, "U' F' U F U R U' R'", log)
                elif target == 5:  # FL
                    if ori == 0:
                        while _find_edge(cube, target)[0] != 2: _apply(cube, "U", log)
                        _apply(cube, "U' L' U L U F U' F'", log)
                    else:
                        while _find_edge(cube, target)[0] != 3: _apply(cube, "U", log)
                        _apply(cube, "U F U' F' U' L' U L", log)
                elif target == 6:  # BL
                    if ori == 0:
                        while _find_edge(cube, target)[0] != 0: _apply(cube, "U", log)
                        _apply(cube, "U' L' U L U B U' B'", log)
                    else:
                        while _find_edge(cube, target)[0] != 3: _apply(cube, "U", log)
                        _apply(cube, "U B U' B' U' L' U L", log)
                elif target == 7:  # BR
                    if ori == 0:
                        while _find_edge(cube, target)[0] != 0: _apply(cube, "U", log)
                        _apply(cube, "U R U' R' U' B' U B", log)
                    else:
                        while _find_edge(cube, target)[0] != 1: _apply(cube, "U", log)
                        _apply(cube, "U' B' U B U R U' R'", log)
                break

# =========================================================================
# 4. OSTATNIA WARSTWA LBL
# =========================================================================
def solve_last_layer_lbl(cube, log):
    # 4.1 Orientacja krawędzi (Żółty Krzyż)
    for _ in range(6):
        oris = [cube.get_edge(s)[1] for s in range(4)]
        if sum(oris) == 0:
            break
        if oris[0] == 1 and oris[2] == 1 and oris[1] == 0 and oris[3] == 0:
            _apply(cube, "U", log)
        elif oris[0] == 1 and oris[3] == 1:
            _apply(cube, "U", log)
        _apply(cube, "F R U R' U' F'", log)

    # 4.2 Orientacja narożników (Sune)
    for _ in range(8):
        c_oris = [cube.get_corner(s)[1] for s in range(4)]
        if sum(c_oris) == 0:
            break
        # Ustaw narożnik z orientacją != 0 na lewy przód (slot 3)
        if cube.get_corner(3)[1] == 0:
            _apply(cube, "U", log)
        else:
            _apply(cube, "R U R' U R U2 R'", log)

    # 4.3 Permutacja narożników (A-Perm / T-Perm)
    for _ in range(6):
        # Sprawdzanie świateł (headlights)
        p0, p1 = cube.get_corner(0)[0], cube.get_corner(1)[0]
        p2, p3 = cube.get_corner(2)[0], cube.get_corner(3)[0]
        if (p0 in [0, 1] and p1 in [0, 1]) or (p2 in [2, 3] and p3 in [2, 3]):
            _apply(cube, "R' F R' B2 R F' R' B2 R2", log)
            break
        _apply(cube, "U", log)
    else:
        _apply(cube, "R' F R' B2 R F' R' B2 R2", log)

    # 4.4 Permutacja krawędzi (U-Perm)
    for _ in range(8):
        if all(cube.get_edge(s)[0] == s for s in range(4)):
            break
        _apply(cube, "R U' R U R U R U' R' U' R2", log)
        if all(cube.get_edge(s)[0] == s for s in range(4)):
            break
        _apply(cube, "U", log)

    # Końcowy obrót U
    for _ in range(4):
        if cube.get_corner(2)[0] == 2:
            break
        _apply(cube, "U", log)

# =========================================================================
# GŁÓWNY INTERFEJS
# =========================================================================
def LBL_FULL(cube, move_list=""):
    log = []
    solve_white_cross(cube, log)
    solve_first_layer_corners(cube, log)
    solve_middle_layer(cube, log)
    solve_last_layer_lbl(cube, log)
    
    res = " ".join(log)
    return f"{move_list} {res}".strip() if move_list else res