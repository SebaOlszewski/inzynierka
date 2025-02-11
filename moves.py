import numpy as np

def move(grid_pattern, move):
    if move == 'U':
        m = [grid_pattern[0][3],grid_pattern[0][4],grid_pattern[0][5],
             grid_pattern[1][3],grid_pattern[1][4],grid_pattern[1][5],
             grid_pattern[2][3],grid_pattern[2][4],grid_pattern[2][5]]


        grid_pattern[0][3] = m[6]
        grid_pattern[0][4] = m[3]
        grid_pattern[0][5] = m[0]
        grid_pattern[1][3] = m[7]
        grid_pattern[1][4] = m[4]
        grid_pattern[1][5] = m[1]
        grid_pattern[2][3] = m[8]
        grid_pattern[2][4] = m[5]
        grid_pattern[2][5] = m[2]

        grid_pattern[3][:] = grid_pattern[3][+3:] + grid_pattern[3][:+3]
        return grid_pattern
    elif move == "D":
        m = [grid_pattern[6][3],grid_pattern[6][4],grid_pattern[6][5],
             grid_pattern[7][3],grid_pattern[7][4],grid_pattern[7][5],
             grid_pattern[8][3],grid_pattern[8][4],grid_pattern[8][5]]

        

        grid_pattern[6][3] = m[6]
        grid_pattern[6][4] = m[3]
        grid_pattern[6][5] = m[0]

        grid_pattern[7][3] = m[7]
        grid_pattern[7][4] = m[4]
        grid_pattern[7][5] = m[1]

        grid_pattern[8][3] = m[8]
        grid_pattern[8][4] = m[5]
        grid_pattern[8][5] = m[2]

        grid_pattern[5][:] = grid_pattern[5][-3:] + grid_pattern[5][:-3]

        return grid_pattern
    
    elif move == "L":
        m = [
        [grid_pattern[3][0], grid_pattern[4][0], grid_pattern[5][0]],
        [grid_pattern[3][1], grid_pattern[4][1], grid_pattern[5][1]],
        [grid_pattern[3][2], grid_pattern[4][2], grid_pattern[5][2]]
        ]
        m = np.rot90(m, 1)  # Rotate 90 degrees clockwise
        grid_pattern[3][0] = m[0][0]
        grid_pattern[4][0] = m[0][1]
        grid_pattern[5][0] = m[0][2]
        grid_pattern[3][1] = m[1][0]
        grid_pattern[4][1] = m[1][1]
        grid_pattern[5][1] = m[1][2]
        grid_pattern[3][2] = m[2][0]
        grid_pattern[4][2] = m[2][1]
        grid_pattern[5][2] = m[2][2]
        # Rotate the adjacent faces
        temp_top = [grid_pattern[0][3], grid_pattern[1][3], grid_pattern[2][3]]
        temp_front = [grid_pattern[3][3], grid_pattern[4][3], grid_pattern[5][3]]
        temp_bottom = [grid_pattern[6][3], grid_pattern[7][3], grid_pattern[8][3]]
        temp_back = [grid_pattern[5][11], grid_pattern[4][11], grid_pattern[3][11]]
        grid_pattern[0][3] = temp_back[0]
        grid_pattern[1][3] = temp_back[1]
        grid_pattern[2][3] = temp_back[2]
        grid_pattern[3][3] = temp_top[0]
        grid_pattern[4][3] = temp_top[1]
        grid_pattern[5][3] = temp_top[2]
        grid_pattern[6][3] = temp_front[0]
        grid_pattern[7][3] = temp_front[1]
        grid_pattern[8][3] = temp_front[2]
        grid_pattern[5][11] = temp_bottom[0]
        grid_pattern[4][11] = temp_bottom[1]
        grid_pattern[3][11] = temp_bottom[2]

        return grid_pattern
    
    elif move == "R":
        m = [
        [grid_pattern[3][6], grid_pattern[4][6], grid_pattern[5][6]],
        [grid_pattern[3][7], grid_pattern[4][7], grid_pattern[5][7]],
        [grid_pattern[3][8], grid_pattern[4][8], grid_pattern[5][8]]
        ]

        m = np.rot90(m, 1)  # Rotate 90 degrees clockwise

        grid_pattern[3][6] = m[0][0]
        grid_pattern[4][6] = m[0][1]
        grid_pattern[5][6] = m[0][2]
        grid_pattern[3][7] = m[1][0]
        grid_pattern[4][7] = m[1][1]
        grid_pattern[5][7] = m[1][2]
        grid_pattern[3][8] = m[2][0]
        grid_pattern[4][8] = m[2][1]
        grid_pattern[5][8] = m[2][2]
    
        # Rotate the adjacent faces
        temp_top = [grid_pattern[0][5], grid_pattern[1][5], grid_pattern[2][5]]
        temp_front = [grid_pattern[3][5], grid_pattern[4][5], grid_pattern[5][5]]
        temp_bottom = [grid_pattern[6][5], grid_pattern[7][5], grid_pattern[8][5]]
        temp_back = [grid_pattern[5][9], grid_pattern[4][9], grid_pattern[3][9]]


        grid_pattern[0][5] = temp_front[0]
        grid_pattern[1][5] = temp_front[1]
        grid_pattern[2][5] = temp_front[2]

        grid_pattern[3][5] = temp_bottom[0]
        grid_pattern[4][5] = temp_bottom[1]
        grid_pattern[5][5] = temp_bottom[2]

        grid_pattern[6][5] = temp_back[0]
        grid_pattern[7][5] = temp_back[1]
        grid_pattern[8][5] = temp_back[2]

        grid_pattern[5][9] = temp_top[0]
        grid_pattern[4][9] = temp_top[1]
        grid_pattern[3][9] = temp_top[2]

        return grid_pattern
    
    elif move == 'M':

       
        temp_top = [grid_pattern[0][4], grid_pattern[1][4], grid_pattern[2][4]]
        temp_front = [grid_pattern[3][4], grid_pattern[4][4], grid_pattern[5][4]]
        temp_bottom = [grid_pattern[6][4], grid_pattern[7][4], grid_pattern[8][4]]
        temp_back = [grid_pattern[5][10], grid_pattern[4][10], grid_pattern[3][10]]


        grid_pattern[0][4] = temp_front[0]
        grid_pattern[1][4] = temp_front[1]
        grid_pattern[2][4] = temp_front[2]

        grid_pattern[3][4] = temp_bottom[0]
        grid_pattern[4][4] = temp_bottom[1]
        grid_pattern[5][4] = temp_bottom[2]

        grid_pattern[6][4] = temp_back[0]
        grid_pattern[7][4] = temp_back[1]
        grid_pattern[8][4] = temp_back[2]

        grid_pattern[5][10] = temp_top[0]
        grid_pattern[4][10] = temp_top[1]
        grid_pattern[3][10] = temp_top[2]

        return grid_pattern
    
    elif move == 'F':
        
        temp_front = [[grid_pattern[3][3],grid_pattern[3][4],grid_pattern[3][5]],
                      [grid_pattern[4][3],grid_pattern[4][4],grid_pattern[4][5]],
                      [grid_pattern[5][3],grid_pattern[5][4],grid_pattern[5][5]]]
        temp_top = [grid_pattern[2][3],grid_pattern[2][4],grid_pattern[2][5]]
        temp_right = [grid_pattern[3][6],grid_pattern[4][6],grid_pattern[5][6]]
        temp_bottom = [grid_pattern[6][3],grid_pattern[6][4],grid_pattern[6][5]]
        temp_left = [grid_pattern[5][2],grid_pattern[4][2],grid_pattern[3][2]]
        grid_pattern[3][3] = temp_front[2][0]
        grid_pattern[3][4] = temp_front[1][0]
        grid_pattern[3][5] = temp_front[0][0]
        grid_pattern[4][3] = temp_front[2][1]
        grid_pattern[4][4] = temp_front[1][1]
        grid_pattern[4][5] = temp_front[0][1]
        grid_pattern[5][3] = temp_front[2][2]   
        grid_pattern[5][4] = temp_front[1][2]
        grid_pattern[5][5] = temp_front[0][2]


        grid_pattern[2][3] = temp_left[0]
        grid_pattern[2][4] = temp_left[1]
        grid_pattern[2][5] = temp_left[2]
        grid_pattern[3][6] = temp_top[0]
        grid_pattern[4][6] = temp_top[1]
        grid_pattern[5][6] = temp_top[2]
        grid_pattern[6][5] = temp_right[0]
        grid_pattern[6][4] = temp_right[1]
        grid_pattern[6][3] = temp_right[2]
        grid_pattern[5][2] = temp_bottom[2]
        grid_pattern[4][2] = temp_bottom[1]
        grid_pattern[3][2] = temp_bottom[0]

        return grid_pattern
    
    elif move == 'B':
        temp_back = [grid_pattern[3][9], grid_pattern[3][10], grid_pattern[3][11],
                    grid_pattern[4][9], grid_pattern[4][10], grid_pattern[4][11],
                    grid_pattern[5][9], grid_pattern[5][10], grid_pattern[5][11]]

        temp_top = [grid_pattern[0][3], grid_pattern[0][4], grid_pattern[0][5]]
        temp_right = [grid_pattern[3][0], grid_pattern[4][0], grid_pattern[5][0]]
        temp_bottom = [grid_pattern[8][3], grid_pattern[8][4], grid_pattern[8][5]]
        temp_left = [grid_pattern[3][8], grid_pattern[4][8], grid_pattern[5][8]]

        grid_pattern[3][9] = temp_back[6]
        grid_pattern[3][10] = temp_back[3]
        grid_pattern[3][11] = temp_back[0]
        grid_pattern[4][9] = temp_back[7]
        grid_pattern[4][10] = temp_back[4]
        grid_pattern[4][11] = temp_back[1]
        grid_pattern[5][9] = temp_back[8]
        grid_pattern[5][10] = temp_back[5]
        grid_pattern[5][11] = temp_back[2]

        # yellow_side
        grid_pattern[0][3] = temp_left[0]
        grid_pattern[0][4] = temp_left[1]
        grid_pattern[0][5] = temp_left[2]

        # red_side
        grid_pattern[3][0] = temp_top[2]
        grid_pattern[4][0] = temp_top[1]
        grid_pattern[5][0] = temp_top[0]

        # white_side
        grid_pattern[8][3] = temp_right[0]
        grid_pattern[8][4] = temp_right[1]
        grid_pattern[8][5] = temp_right[2]

        # orange_side
        grid_pattern[3][8] = temp_bottom[2]
        grid_pattern[4][8] = temp_bottom[1]
        grid_pattern[5][8] = temp_bottom[0]

        return grid_pattern
    
    elif move == 'Z':

        temp_middle_row = grid_pattern[4]
        temp_middle_row = temp_middle_row[3:] + temp_middle_row[:3]
        grid_pattern[4] = temp_middle_row
        return grid_pattern
    
    elif move == 'C':
        grid_pattern = [
            [0, 0, 0, 'Y', 'Y', 'Y', 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 'Y', 'Y', 'Y', 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 'Y', 'Y', 'Y', 0, 0, 0, 0, 0, 0],
            ['R', 'R', 'R', 'G', 'G', 'G', 'O', 'O', 'O', 'B', 'B', 'B'],
            ['R', 'R', 'R', 'G', 'G', 'G', 'O', 'O', 'O', 'B', 'B', 'B'],
            ['R', 'R', 'R', 'G', 'G', 'G', 'O', 'O', 'O', 'B', 'B', 'B'],
            [0, 0, 0, 'W', 'W', 'W', 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 'W', 'W', 'W', 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 'W', 'W', 'W', 0, 0, 0, 0, 0, 0]
        ]

        return grid_pattern
    
def move_U(grid_pattern, move_list):
    move(grid_pattern, "U")
    return str(move_list) + "U"

def move_Up(grid_pattern, move_list):
    move(grid_pattern, "U")
    move(grid_pattern, "U")
    move(grid_pattern, "U")
    return str(move_list) + "UUU"

def move_D(grid_pattern, move_list):
    move(grid_pattern, "D")
    return str(move_list) + "D"

def move_Dp(grid_pattern, move_list):
    move(grid_pattern, "D")
    move(grid_pattern, "D")
    move(grid_pattern, "D")
    return str(move_list) + "DDD"

def move_F(grid_pattern, move_list):
    move(grid_pattern, "F")
    return str(move_list) + "F"

def move_Fp(grid_pattern, move_list):
    move(grid_pattern, "F")
    move(grid_pattern, "F")
    move(grid_pattern, "F")
    return str(move_list) + "FFF"

def move_B(grid_pattern, move_list):
    move(grid_pattern, "B")
    return str(move_list) + "B"

def move_Bp(grid_pattern, move_list):
    move(grid_pattern, "B")
    move(grid_pattern, "B")
    move(grid_pattern, "B")
    return str(move_list) + "BBB"

def move_L(grid_pattern, move_list):
    move(grid_pattern, "L")
    return str(move_list) + "L"

def move_Lp(grid_pattern, move_list):
    move(grid_pattern, "L")
    move(grid_pattern, "L")
    move(grid_pattern, "L")
    return str(move_list) + "LLL"

def move_R(grid_pattern, move_list):
    move(grid_pattern, "R")
    return str(move_list) + "R"

def move_Rp(grid_pattern, move_list):
    move(grid_pattern, "R")
    move(grid_pattern, "R")
    move(grid_pattern, "R")
    return str(move_list) + "RRR"

def move_Z(grid_pattern, move_list):
    move(grid_pattern, "Z")
    return str(move_list) + "Z"

def move_Zp(grid_pattern, move_list):
    move(grid_pattern, "Z")
    move(grid_pattern, "Z")
    move(grid_pattern, "Z")
    return str(move_list) + "ZZZ"

def move_M(grid_pattern, move_list):
    move(grid_pattern, "M")
    return str(move_list) + "M"

def move_Mp(grid_pattern, move_list):
    move(grid_pattern, "M")
    move(grid_pattern, "M")
    move(grid_pattern, "M")
    return str(move_list) + "MMM"