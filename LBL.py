import numpy as np
import moves
import algs

def first_layer(grid_pattern, move_list):
    move_list = solve_cross(grid_pattern, move_list)
    move_list = corners_to_top(grid_pattern, move_list)
    while not(grid_pattern[6][3] == grid_pattern[6][5] == grid_pattern[8][3] == grid_pattern[8][5] == "W"):
        move_list = finish_corners(grid_pattern, move_list)
    
    return move_list

def solve_cross(grid_pattern, move_list):
    while not is_white_cross_on_top(grid_pattern):
        move_list = bring_white_edges_to_top(grid_pattern, move_list)
    move_list = bring_white_edges_to_bottom(grid_pattern, move_list)
    
    move_list = algs.center_cube(grid_pattern, move_list)
    return move_list

def bring_white_edges_to_top(grid_pattern, move_list):
    #elements are on white side
    while  grid_pattern[6][4] == "W" or grid_pattern[7][3] == "W" or grid_pattern[7][5] == "W" or grid_pattern[8][4] == "W":
        while grid_pattern[2][4] == "W":
            move_list = moves.move_U(grid_pattern, move_list)
        while grid_pattern[6][4] != "W":
            move_list = moves.move_D(grid_pattern, move_list)
        move_list = moves.move_F(grid_pattern, move_list)
        move_list = moves.move_F(grid_pattern, move_list)
        
    #elements are on first layer
    while grid_pattern[5][1] == "W" or grid_pattern[5][4] == "W" or grid_pattern[5][7] == "W" or grid_pattern[5][10] == "W":
        while grid_pattern[2][1] == "W":
            move_list = moves.move_U(grid_pattern, move_list)
        while grid_pattern[5][4] != "W":
            move_list = moves.move_D(grid_pattern, move_list)
        move_list = moves.move_F(grid_pattern, move_list)
        move_list = moves.move_L(grid_pattern, move_list)
        move_list = moves.move_F(grid_pattern, move_list)
        move_list = moves.move_F(grid_pattern, move_list)
    #elements are on second layer
    while grid_pattern[4][0] == "W" or grid_pattern[4][2] == "W" or grid_pattern[4][3] == "W" or grid_pattern[4][5] == "W" or grid_pattern[4][6] == "W"\
          or grid_pattern[4][8] == "W" or grid_pattern[4][9] == "W" or grid_pattern[4][11] == "W":
        
        if grid_pattern[4][3] == "W":
            while grid_pattern[1][3] == "W":
                move_list = moves.move_U(grid_pattern, move_list)
            move_list = moves.move_Lp(grid_pattern, move_list)
            
        elif grid_pattern[4][5] == "W":
            while grid_pattern[1][5] == "W":
                move_list = moves.move_U(grid_pattern, move_list)
            move_list = moves.move_R(grid_pattern, move_list)
            
        else:
            move_list = moves.move_Z(grid_pattern, move_list)
            
    
    #elements are on third layer
    while grid_pattern[3][1] == "W" or grid_pattern[3][4] == "W" or grid_pattern[3][7] == "W" or grid_pattern[3][10] == "W":
        while grid_pattern[3][4] != "W":
            move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_F(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_R(grid_pattern, move_list)
        
    return move_list

def bring_white_edges_to_bottom(grid_pattern, move_list):
    while grid_pattern[0][4] == "W" or grid_pattern[1][3] == "W" or grid_pattern[1][5] == "W" or grid_pattern[2][4] == "W":
        #blue
        while grid_pattern[2][4] != "W":
            move_list = moves.move_U(grid_pattern, move_list)
        while grid_pattern[3][4] != grid_pattern[4][4]:
            move_list = moves.move_Zp(grid_pattern, move_list)
            move_list = moves.move_D(grid_pattern, move_list)
        move_list = moves.move_F(grid_pattern, move_list)
        move_list = moves.move_F(grid_pattern, move_list)
        move_list = moves.move_Zp(grid_pattern, move_list)
        move_list = moves.move_D(grid_pattern, move_list)
    
    return move_list
        
def is_white_cross_on_top(grid_pattern):
    if grid_pattern[0][4] == "W" and grid_pattern[1][3] == "W" and grid_pattern[1][5] == "W" and grid_pattern[2][4] == "W":
        return True

def corners_to_top(grid_pattern, move_list):

    while ("W" in grid_pattern[5]) or grid_pattern[6][3] == "W" or grid_pattern[6][5] == "W"  or grid_pattern[8][3] == "W"  or grid_pattern[8][5] == "W":
        if grid_pattern[6][3] == "W" or grid_pattern[5][2] == "W" or grid_pattern[5][3] == "W" or \
            grid_pattern[6][5] == "W" or grid_pattern[5][5] == "W" or grid_pattern[5][6] == "W" or \
            grid_pattern[8][3] == "W" or grid_pattern[5][11] == "W" or grid_pattern[5][0] == "W" or \
            grid_pattern[8][5] == "W" or grid_pattern[5][8] == "W" or grid_pattern[5][9] == "W":
            

            while grid_pattern[6][5] != "W" and grid_pattern[5][5] != "W" and grid_pattern[5][6] != "W":
                move_list = moves.move_D(grid_pattern, move_list)
            while grid_pattern[3][5] == "W" or grid_pattern[2][5] == "W" or grid_pattern[3][6] == "W":
                move_list = moves.move_U(grid_pattern, move_list)
            move_list = algs.ruru(grid_pattern, move_list)
            move_list = algs.ruru(grid_pattern, move_list)
            move_list = algs.ruru(grid_pattern, move_list)
    move_list = algs.center_cube(grid_pattern, move_list)
    
    return move_list 

def finish_corners(grid_pattern, move_list):
        algs.center_cube(grid_pattern, move_list)
        corner = []
        if not (grid_pattern[6][3] == "W" and grid_pattern[6][5] == "W"and grid_pattern[8][3] == "W" and grid_pattern[8][5] == "W"):
            
            if grid_pattern[3][5] == "W" or grid_pattern[3][6] == "W" or grid_pattern[2][5] == "W":
                corner.append(str(grid_pattern[3][5]))
                corner.append(str(grid_pattern[3][6]))
                corner.append(str(grid_pattern[2][5]))
                if "G" in corner and "O" in corner :
                    while not (grid_pattern[6][5] == "W" and grid_pattern[5][5] == "G" and grid_pattern[5][6] == "O"):
                        move_list = algs.ruru(grid_pattern, move_list)

                elif "G" in corner and "R" in corner:
                    move_list = moves.move_D(grid_pattern, move_list)
                    while not (grid_pattern[6][5] == "W" and grid_pattern[5][5] == "R" and grid_pattern[5][6] == "G"):
                        move_list = algs.ruru(grid_pattern, move_list)
                    move_list = moves.move_Dp(grid_pattern, move_list)

                elif "R" in corner and "B" in corner:
                    move_list = moves.move_D(grid_pattern, move_list)
                    move_list = moves.move_D(grid_pattern, move_list)
                    while not (grid_pattern[6][5] == "W" and grid_pattern[5][5] == "B" and grid_pattern[5][6] == "R"):
                        move_list = algs.ruru(grid_pattern, move_list)
                    move_list = moves.move_D(grid_pattern, move_list)
                    move_list = moves.move_D(grid_pattern, move_list)

                elif "O" in corner and "B" in corner :
                    move_list = moves.move_D(grid_pattern, move_list)
                    move_list = moves.move_D(grid_pattern, move_list)
                    move_list = moves.move_D(grid_pattern, move_list)
                    while not (grid_pattern[6][5] == "W" and grid_pattern[5][5] == "O" and grid_pattern[5][6] == "B"):
                        move_list = algs.ruru(grid_pattern, move_list)
                    move_list = moves.move_D(grid_pattern, move_list)
                
                move_list = moves.move_U(grid_pattern, move_list)
            else:
                move_list = moves.move_U(grid_pattern, move_list)
        else:
            return move_list 
        
def yellow_to_2nd(grid_pattern, move_list):
    while "Y" in grid_pattern[3][1] or "Y" in grid_pattern[3][4] or "Y" in grid_pattern[3][7] or "Y" in grid_pattern[3][10] or \
        "Y" in grid_pattern[0][4] or "Y" in grid_pattern[1][3] or "Y" in grid_pattern[1][5] or"Y" in grid_pattern[2][4]:
        
        #is yellow in the middle
        if grid_pattern[2][4] == "Y" or  grid_pattern[3][4] == "Y":
            #if element on the left doesnt heve yellow, move it to the left
            if grid_pattern[4][2] != "Y" and grid_pattern[4][3] != "Y":
                move_list = algs.edge_to_left(grid_pattern, move_list)
            #if element on the right doenst have yellow, move it to the right
            elif grid_pattern[4][6] != "Y" and grid_pattern[4][6] != "Y":
                move_list = algs.edge_to_right(grid_pattern, move_list)
            else:
                #if both are unavailable, move middle row
                move_list = moves.move_Z(grid_pattern, move_list)

        else:
            #move to another block
            move_list = moves.move_U(grid_pattern, move_list)
    
    move_list = algs.center_cube(grid_pattern, move_list) 
    return move_list

def solve_2nd(grid_pattern, move_list):
    while "Y" in grid_pattern[4]:
        while grid_pattern[3][4] != "Y" and grid_pattern[2][4] != "Y":
            if grid_pattern[4][4] != grid_pattern[3][4]:
                move_list = moves.move_Z(grid_pattern, move_list)
            else:
                if grid_pattern[2][4] == grid_pattern[4][1]:
                    move_list = algs.edge_to_left(grid_pattern, move_list)
                elif grid_pattern[2][4] == grid_pattern[4][7]:
                    move_list = algs.edge_to_right(grid_pattern, move_list)
        else:
            move_list = moves.move_U(grid_pattern, move_list)
    move_list = algs.center_cube(grid_pattern, move_list)   
    return move_list

def cross_on_top(grid_pattern, move_list):
    while not (grid_pattern[0][4] == "Y" and grid_pattern[1][3] == "Y" and grid_pattern[1][5] == "Y" and grid_pattern[2][4] == "Y"): 
        if grid_pattern[0][4] == grid_pattern[1][3] == "Y":
            move_list = moves.move_F(grid_pattern, move_list)
            move_list = algs.ruru(grid_pattern, move_list)
            move_list = moves.move_Fp(grid_pattern, move_list)
        else:
            move_list = moves.move_F(grid_pattern, move_list)
            move_list = algs.ruru(grid_pattern, move_list)
            move_list = moves.move_Fp(grid_pattern, move_list)
            move_list = moves.move_U(grid_pattern, move_list) 
    else:
        move_list = moves.move_U(grid_pattern, move_list)  
    
    return move_list

def solve_edged_on_top(grid_pattern, move_list):
    while not (grid_pattern[3][1] == "R" and grid_pattern[3][4] == "G" and grid_pattern[3][7] == "O" and grid_pattern[3][10] == "B"):

        while grid_pattern[3][4] != "G":
            move_list = moves.move_U(grid_pattern, move_list) 

        if grid_pattern[3][10] == "B":
                move_list = algs.swap_to_left(grid_pattern, move_list)
                move_list = algs.swap_to_right(grid_pattern, move_list)
                move_list = algs.swap_to_left(grid_pattern, move_list)
        elif grid_pattern[3][10] != "B":
            if grid_pattern[3][1] == "B":
                move_list = algs.swap_to_left(grid_pattern, move_list)
            else:
                move_list = algs.swap_to_right(grid_pattern, move_list)
    return move_list

def solve_corners(grid_pattern, move_list):
    correct_corner1 = ["Y", "R", "B"]
    correct_corner2 = ["Y", "O", "B"]
    correct_corner3 = ["Y", "G", "R"]
    correct_corner4 = ["Y", "G", "O"]

    while True:
        corner1 = [str(grid_pattern[0][3]), str(grid_pattern[3][0]), str(grid_pattern[3][11])]
        corner2 = [str(grid_pattern[0][5]), str(grid_pattern[3][8]), str(grid_pattern[3][9])]
        corner3 = [str(grid_pattern[3][3]), str(grid_pattern[3][2]), str(grid_pattern[2][3])]
        corner4 = [str(grid_pattern[3][5]), str(grid_pattern[3][6]), str(grid_pattern[2][5])]

        if set(correct_corner1) == set(corner1) and set(correct_corner2) == set(corner2) and \
           set(correct_corner3) == set(corner3) and set(correct_corner4) == set(corner4):
            break

        if not ("B" in corner1 and "R" in corner1) or not ("O" in corner2 and "B" in corner2) or \
           not ("R" in corner3 and "G" in corner3) or not ("G" in corner4 and "O" in corner4):
            if "G" in corner1 and "O" in corner1:
                move_list = moves.move_U(grid_pattern, move_list)
                move_list = algs.swap_corners(grid_pattern, move_list)
                move_list = algs.swap_corners(grid_pattern, move_list)
                move_list = moves.move_Up(grid_pattern, move_list)
            if "G" in corner2 and "O" in corner2:
                move_list = moves.move_Up(grid_pattern, move_list)
                move_list = algs.swap_corners(grid_pattern, move_list)
                move_list = algs.swap_corners(grid_pattern, move_list)
                move_list = moves.move_U(grid_pattern, move_list)
            if "G" in corner3 and "O" in corner3:
                move_list = moves.move_U(grid_pattern, move_list)
                move_list = algs.swap_corners(grid_pattern, move_list)
                move_list = moves.move_Up(grid_pattern, move_list)
            if "G" in corner4 and "O" in corner4:
                if not ("B" in corner1 and "R" in corner1):
                    move_list = algs.swap_corners(grid_pattern, move_list)
    return move_list

def permutate_yellow_corners(grid_pattern, move_list):
    while grid_pattern[0][3] != "Y" or grid_pattern[0][5] != "Y" or grid_pattern[2][3] != "Y" or grid_pattern[2][5] != "Y":
        if grid_pattern[2][3] != "Y":
            move_list = moves.move_L(grid_pattern, move_list)
            move_list = moves.move_D(grid_pattern, move_list)
            move_list = moves.move_Lp(grid_pattern, move_list)
            move_list = moves.move_Dp(grid_pattern, move_list)
        else:
            move_list = moves.move_U(grid_pattern, move_list)

    while grid_pattern[3][4] != "G":
        move_list = moves.move_U(grid_pattern, move_list)
    
    return move_list

def LBL_FULL(grid_pattern, move_list):
        move_list = first_layer(grid_pattern, move_list)
        move_list = yellow_to_2nd(grid_pattern, move_list)
        move_list = solve_2nd(grid_pattern, move_list)
        move_list = cross_on_top(grid_pattern, move_list)
        move_list = solve_edged_on_top(grid_pattern, move_list)
        move_list = solve_corners(grid_pattern, move_list)
        move_list = permutate_yellow_corners(grid_pattern, move_list)
        
        return move_list