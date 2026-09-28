# cube_bitboard.py

class BitCube:
    def __init__(self):
        # 8 narożników (sloty 0..7, każdy po 5 bitów): 
        # 0:UBL, 1:UBR, 2:UFR, 3:UFL, 4:DFL, 5:DFR, 6:DBR, 7:DBL
        self.corners = 0
        for i in range(8):
            self.corners |= ((i << 2) | 0) << (5 * i)
            
        # 12 krawędzi (sloty 0..11, każdy po 5 bitów): 
        # 0:UB, 1:UR, 2:UF, 3:UL, 4:FR, 5:FL, 6:BL, 7:BR, 8:DF, 9:DR, 10:DB, 11:DL
        self.edges = 0
        for i in range(12):
            self.edges |= ((i << 1) | 0) << (5 * i)

    # --- GETTERY I SETTERY BITOWE ---
    def get_corner(self, slot):
        val = (self.corners >> (5 * slot)) & 0x1F
        return (val >> 2), (val & 0x03)

    def set_corner(self, slot, perm, ori):
        mask = ~(0x1F << (5 * slot))
        val = ((perm << 2) | (ori % 3)) & 0x1F
        self.corners = (self.corners & mask) | (val << (5 * slot))

    def get_edge(self, slot):
        val = (self.edges >> (5 * slot)) & 0x1F
        return (val >> 1), (val & 0x01)

    def set_edge(self, slot, perm, ori):
        mask = ~(0x1F << (5 * slot))
        val = ((perm << 1) | (ori % 2)) & 0x1F
        self.edges = (self.edges & mask) | (val << (5 * slot))

    # --- OBSŁUGA RUCHÓW ---
    def apply_move(self, move_name):
        # Obsługa obrotów całej bryły wokół osi pionowej (y, y', y2)
        if move_name.lower().startswith('y'):
            times = 1
            if "'" in move_name:
                times = 3
            elif "2" in move_name:
                times = 2
            for _ in range(times):
                self._rotate_y()
            return

        base = move_name[0].upper()
        times = 1
        if "'" in move_name:
            times = 3
        elif "2" in move_name:
            times = 2
            
        for _ in range(times):
            self._apply_base_move(base)

    def _apply_base_move(self, m):
        if m == 'U':
            self._cycle_corners([0, 1, 2, 3], [0, 0, 0, 0])
            self._cycle_edges([0, 1, 2, 3], [0, 0, 0, 0])
        elif m == 'D':
            self._cycle_corners([4, 5, 6, 7], [0, 0, 0, 0])
            self._cycle_edges([8, 9, 10, 11], [0, 0, 0, 0])
        elif m == 'R':
            self._cycle_corners([1, 6, 5, 2], [2, 1, 2, 1])
            self._cycle_edges([1, 7, 9, 4], [0, 0, 0, 0])
        elif m == 'L':
            self._cycle_corners([0, 3, 4, 7], [1, 2, 1, 2])
            self._cycle_edges([3, 5, 11, 6], [0, 0, 0, 0])
        elif m == 'F':
            self._cycle_corners([3, 2, 5, 4], [1, 2, 1, 2])
            self._cycle_edges([2, 4, 8, 5], [1, 1, 1, 1])
        elif m == 'B':
            self._cycle_corners([1, 0, 7, 6], [2, 1, 2, 1])
            self._cycle_edges([0, 6, 10, 7], [1, 1, 1, 1])
        elif m == 'M':
            # Ruch M (warstwa środkowa w dół, w kierunku L)
            self._cycle_edges([0, 2, 8, 10], [1, 1, 1, 1])
        elif m == 'E':
            # Obrót poziomej warstwy środkowej (zgodnie z ruchem D)
            # Cykl krawędzi: FL(5) -> FR(4) -> BR(7) -> BL(6) -> FL(5)
            self._cycle_edges([5, 4, 7, 6], [0, 0, 0, 0])

    def _rotate_y(self):
        """Obrót całej kostki o 90 stopni w kierunku U."""
        self._cycle_corners([0, 1, 2, 3], [0, 0, 0, 0])
        self._cycle_edges([0, 1, 2, 3], [0, 0, 0, 0])
        self._cycle_corners([4, 7, 6, 5], [0, 0, 0, 0])
        self._cycle_edges([8, 11, 10, 9], [0, 0, 0, 0])
        self._cycle_edges([4, 7, 6, 5], [0, 0, 0, 0])

    def _cycle_corners(self, slots, ori_deltas):
        c = [self.get_corner(s) for s in slots]
        for i in range(4):
            src_perm, src_ori = c[(i - 1) % 4]
            self.set_corner(slots[i], src_perm, src_ori + ori_deltas[i])

    def _cycle_edges(self, slots, ori_deltas):
        e = [self.get_edge(s) for s in slots]
        for i in range(4):
            src_perm, src_ori = e[(i - 1) % 4]
            self.set_edge(slots[i], src_perm, src_ori + ori_deltas[i])

    def to_2d_grid(self):
        grid = [[0 for _ in range(12)] for _ in range(9)]
        
        # Centra
        grid[1][4] = 'Y'
        grid[7][4] = 'W'
        grid[4][1] = 'R'
        grid[4][4] = 'G'
        grid[4][7] = 'O'
        grid[4][10] = 'B'
        
        # Krawędzie
        edge_coords = [
            ((0, 4), (3, 10)),  # 0: UB
            ((1, 5), (3, 7)),   # 1: UR
            ((2, 4), (3, 4)),   # 2: UF
            ((1, 3), (3, 1)),   # 3: UL
            ((4, 5), (4, 6)),   # 4: FR
            ((4, 3), (4, 2)),   # 5: FL
            ((4, 11), (4, 0)),  # 6: BL
            ((4, 9), (4, 8)),   # 7: BR
            ((6, 4), (5, 4)),   # 8: DF
            ((7, 5), (5, 7)),   # 9: DR
            ((8, 4), (5, 10)),  # 10: DB
            ((7, 3), (5, 1))    # 11: DL
        ]
        edge_base_colors = [
            ('Y', 'B'), ('Y', 'O'), ('Y', 'G'), ('Y', 'R'),
            ('G', 'O'), ('G', 'R'), ('B', 'R'), ('B', 'O'),
            ('W', 'G'), ('W', 'O'), ('W', 'B'), ('W', 'R')
        ]
        
        for slot in range(12):
            perm, ori = self.get_edge(slot)
            c1, c2 = edge_base_colors[perm]
            if ori == 1:
                c1, c2 = c2, c1
            (r1, col1), (r2, col2) = edge_coords[slot]
            grid[r1][col1] = c1
            grid[r2][col2] = c2

        # Narożniki
        corner_coords = [
            ((0, 3), (3, 11), (3, 0)),  # 0: UBL (Y, B, R)
            ((0, 5), (3, 8), (3, 9)),   # 1: UBR (Y, O, B)
            ((2, 5), (3, 5), (3, 6)),   # 2: UFR (Y, G, O)
            ((2, 3), (3, 2), (3, 3)),   # 3: UFL (Y, R, G)
            ((6, 3), (5, 3), (5, 2)),   # 4: DFL (W, G, R)
            ((6, 5), (5, 6), (5, 5)),   # 5: DFR (W, O, G)
            ((8, 5), (5, 9), (5, 8)),   # 6: DBR (W, B, O)
            ((8, 3), (5, 0), (5, 11))   # 7: DBL (W, R, B)
        ]
        corner_base_colors = [
            ('Y', 'B', 'R'), ('Y', 'O', 'B'), ('Y', 'G', 'O'), ('Y', 'R', 'G'),
            ('W', 'G', 'R'), ('W', 'O', 'G'), ('W', 'B', 'O'), ('W', 'R', 'B')
        ]

        for slot in range(8):
            perm, ori = self.get_corner(slot)
            cols = corner_base_colors[perm]
            cols = cols[ori:] + cols[:ori]
            (r1, col1), (r2, col2), (r3, col3) = corner_coords[slot]
            grid[r1][col1] = cols[0]
            grid[r2][col2] = cols[1]
            grid[r3][col3] = cols[2]
            
        return grid

    def __deepcopy__(self, memo):
        new_cube = BitCube.__new__(BitCube)
        new_cube.corners = self.corners
        new_cube.edges = self.edges
        return new_cube