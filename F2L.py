import numpy as np
import moves
import algs
import LBL

def solve_2_layers(grid_pattern, move_list):
    move_list = LBL.solve_cross(grid_pattern, move_list)
    move_list = LBL.corners_to_top(grid_pattern, move_list)
    move_list = LBL.yellow_to_2nd(grid_pattern, move_list)
    while not(grid_pattern[6][3] == "W" and grid_pattern[6][5] == "W" and grid_pattern[8][3] == "W" and \
        grid_pattern[8][5] == "W"):

        corner = [grid_pattern[3][5], grid_pattern[3][6], grid_pattern[2][5]]
        

        #white, green, orange
        if "W" in corner and "G" in corner and "O" in corner:
            edge1 = [grid_pattern[0][4], grid_pattern[3][10]]
            edge2 = [grid_pattern[1][3], grid_pattern[3][1]]
            edge3 = [grid_pattern[1][5], grid_pattern[3][7]]
            edge4 = [grid_pattern[2][4], grid_pattern[3][4]]
            # print(edge1, edge2, edge3, edge4)

            #white on top
            if "W" in grid_pattern[2][5]:
                if "G" in grid_pattern[0][4] and "O" in grid_pattern[3][10]:
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "O" in grid_pattern[0][4] and "G" in grid_pattern[3][10]:

                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Lp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_L(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                
                if "G" in grid_pattern[1][3] and "O" in grid_pattern[3][1]:
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = algs.right_edge_insert_CFOP(grid_pattern, move_list)

                    
                elif "O" in grid_pattern[1][3] and "G" in grid_pattern[3][1]:
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = algs.left_edge_insert_CFOP(grid_pattern, move_list)

                if "G" in grid_pattern[1][5] and "O" in grid_pattern[3][7]:
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "O" in grid_pattern[1][5] and "G" in grid_pattern[3][7]:
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                if "G" in grid_pattern[2][4] and "O" in grid_pattern[3][4]:
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "O" in grid_pattern[2][4] and "G" in grid_pattern[3][4]:
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                
            #white on front
            elif "W" in grid_pattern[3][5]:
                if "G" in grid_pattern[0][4] and "O" in grid_pattern[3][10]:
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "O" in grid_pattern[0][4] and "G" in grid_pattern[3][10]:
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)

                if "G" in grid_pattern[1][3] and "O" in grid_pattern[3][1]:
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    
                elif "O" in grid_pattern[1][3] and "G" in grid_pattern[3][1]:
                    # print(WGO F2B")
                    move_list = algs.match_edge_to_corner_left(grid_pattern, move_list)

                if "G" in grid_pattern[1][5] and "O" in grid_pattern[3][7]:
                    # print(WGO F3T")
                    move_list = algs.right_edge_insert_CFOP(grid_pattern, move_list)

                elif "O" in grid_pattern[1][5] and "G" in grid_pattern[3][7]:
                    # print(WGO F3B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = algs.match_edge_to_corner_left(grid_pattern, move_list)
                    

                if "G" in grid_pattern[2][4] and "O" in grid_pattern[3][4]:
                    # print(WGO F4T")
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                elif "O" in grid_pattern[2][4] and "G" in grid_pattern[3][4]:
                    # print(WGO F4B")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = algs.match_edge_to_corner_left(grid_pattern, move_list)

            #white on right
            elif "W" in grid_pattern[3][6]:
                if "G" in grid_pattern[0][4] and "O" in grid_pattern[3][10]:
                    # print(R1T")
                    move_list = algs.match_edge_to_corner_right(grid_pattern, move_list)
                elif "O" in grid_pattern[0][4] and "G" in grid_pattern[3][10]:
                    # print(R1B")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)


                if "G" in grid_pattern[1][3] and "O" in grid_pattern[3][1]:
                    # print(R2T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                elif "O" in grid_pattern[1][3] and "G" in grid_pattern[3][1]:
                    # print(R2B")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)

                if "G" in grid_pattern[1][5] and "O" in grid_pattern[3][7]:
                    # print(R3T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                elif "O" in grid_pattern[1][5] and "G" in grid_pattern[3][7]:
                    # print(R3B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = algs.left_edge_insert_CFOP(grid_pattern, move_list)


                if "G" in grid_pattern[2][4] and "O" in grid_pattern[3][4]:
                    # print(R4T")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = algs.match_edge_to_corner_right(grid_pattern, move_list)

                elif "O" in grid_pattern[2][4] and "G" in grid_pattern[3][4]:
                    # print(R4B")
                    move_list = algs.left_edge_insert_CFOP(grid_pattern, move_list)
        
        #white, red, green
        elif "W" in corner and "R" in corner and "G" in corner:
            move_list = moves.move_Zp(grid_pattern, move_list)
            move_list = moves.move_D(grid_pattern, move_list)
            edge1 = [grid_pattern[0][4], grid_pattern[3][10]]
            edge2 = [grid_pattern[1][3], grid_pattern[3][1]]
            edge3 = [grid_pattern[1][5], grid_pattern[3][7]]
            edge4 = [grid_pattern[2][4], grid_pattern[3][4]]
            # print(edge1, edge2, edge3, edge4)

            #white on top
            if "W" in grid_pattern[2][5]:
                if "R" in grid_pattern[0][4] and "G" in grid_pattern[3][10]:
                    # print(WRG U1T")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "G" in grid_pattern[0][4] and "R" in grid_pattern[3][10]:
                    # print(WRG U1B")
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Lp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_L(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                
                if "R" in grid_pattern[1][3] and "G" in grid_pattern[3][1]:
                    # print(WRG U2T")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = algs.right_edge_insert_CFOP(grid_pattern, move_list)

                    
                elif "G" in grid_pattern[1][3] and "R" in grid_pattern[3][1]:
                    # print(WRG U2B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = algs.left_edge_insert_CFOP(grid_pattern, move_list)

                if "R" in grid_pattern[1][5] and "G" in grid_pattern[3][7]:
                    # print(WRG U3T")
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "G" in grid_pattern[1][5] and "R" in grid_pattern[3][7]:
                    # print(WRG U3B")
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                if "R" in grid_pattern[2][4] and "G" in grid_pattern[3][4]:
                    # print(WRG U4T")
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "G" in grid_pattern[2][4] and "R" in grid_pattern[3][4]:
                    # print(WRG U4B")
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                
            #white on front
            elif "W" in grid_pattern[3][5]:
                if "R" in grid_pattern[0][4] and "G" in grid_pattern[3][10]:
                    # print(WRG F1T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "G" in grid_pattern[0][4] and "R" in grid_pattern[3][10]:
                    # print(WRG F1B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)

                if "R" in grid_pattern[1][3] and "G" in grid_pattern[3][1]:
                    # print(WRG F2T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    
                elif "G" in grid_pattern[1][3] and "R" in grid_pattern[3][1]:
                    # print(WRG F2B")
                    move_list = algs.match_edge_to_corner_left(grid_pattern, move_list)

                if "R" in grid_pattern[1][5] and "G" in grid_pattern[3][7]:
                    # print(WRG F3T")
                    move_list = algs.right_edge_insert_CFOP(grid_pattern, move_list)

                elif "G" in grid_pattern[1][5] and "R" in grid_pattern[3][7]:
                    # print(WRG F3B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = algs.match_edge_to_corner_left(grid_pattern, move_list)
                    

                if "R" in grid_pattern[2][4] and "G" in grid_pattern[3][4]:
                    # print(WRG F4T")
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                elif "G" in grid_pattern[2][4] and "R" in grid_pattern[3][4]:
                    # print(WRG F4B")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = algs.match_edge_to_corner_left(grid_pattern, move_list)

            #white on right
            elif "W" in grid_pattern[3][6]:
                if "R" in grid_pattern[0][4] and "G" in grid_pattern[3][10]:
                    # print(WRG R1T")
                    move_list = algs.match_edge_to_corner_right(grid_pattern, move_list)
                elif "G" in grid_pattern[0][4] and "R" in grid_pattern[3][10]:
                    # print(WRG R1B")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)

                if "R" in grid_pattern[1][3] and "G" in grid_pattern[3][1]:
                    # print(WRG R2T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                elif "G" in grid_pattern[1][3] and "R" in grid_pattern[3][1]:
                    # print(WRG R2B")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)

                if "R" in grid_pattern[1][5] and "G" in grid_pattern[3][7]:
                    # print(WRG R3T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                elif "G" in grid_pattern[1][5] and "R" in grid_pattern[3][7]:
                    # print(WRG R3B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = algs.left_edge_insert_CFOP(grid_pattern, move_list)


                if "R" in grid_pattern[2][4] and "G" in grid_pattern[3][4]:
                    # print(WRG R4T")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = algs.match_edge_to_corner_right(grid_pattern, move_list)

                elif "G" in grid_pattern[2][4] and "R" in grid_pattern[3][4]:
                    # print(WRG R4B")
                    move_list = algs.left_edge_insert_CFOP(grid_pattern, move_list)
            move_list = moves.move_Z(grid_pattern, move_list)
            move_list = moves.move_Dp(grid_pattern, move_list)

        #white, blue, red
        elif "W" in corner and "B" in corner and "R" in corner:
            move_list = moves.move_Z(grid_pattern, move_list)
            move_list = moves.move_Z(grid_pattern, move_list)
            move_list = moves.move_D(grid_pattern, move_list)
            move_list = moves.move_D(grid_pattern, move_list)
            edge1 = [grid_pattern[0][4], grid_pattern[3][10]]
            edge2 = [grid_pattern[1][3], grid_pattern[3][1]]
            edge3 = [grid_pattern[1][5], grid_pattern[3][7]]
            edge4 = [grid_pattern[2][4], grid_pattern[3][4]]
            # print(edge1, edge2, edge3, edge4)

            #white on top
            if "W" in grid_pattern[2][5]:
                if "B" in grid_pattern[0][4] and "R" in grid_pattern[3][10]:
                    # print(WBR 1T")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "R" in grid_pattern[0][4] and "B" in grid_pattern[3][10]:
                    # print(WBR 1B")
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Lp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_L(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                
                if "B" in grid_pattern[1][3] and "R" in grid_pattern[3][1]:
                    # print(WBR 2T")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = algs.right_edge_insert_CFOP(grid_pattern, move_list)

                    
                elif "R" in grid_pattern[1][3] and "B" in grid_pattern[3][1]:
                    # print(WBR 2B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = algs.left_edge_insert_CFOP(grid_pattern, move_list)

                if "B" in grid_pattern[1][5] and "R" in grid_pattern[3][7]:
                    # print(WBR 3T")
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "R" in grid_pattern[1][5] and "B" in grid_pattern[3][7]:
                    # print(WBR 3B")
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                if "B" in grid_pattern[2][4] and "R" in grid_pattern[3][4]:
                    # print(WBR 4T")
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "R" in grid_pattern[2][4] and "B" in grid_pattern[3][4]:
                    # print(WBR 4B")
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                
            #white on front
            elif "W" in grid_pattern[3][5]:
                if "B" in grid_pattern[0][4] and "R" in grid_pattern[3][10]:
                    # print(WBR F1T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "R" in grid_pattern[0][4] and "B" in grid_pattern[3][10]:
                    # print(WBR F1B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)

                if "B" in grid_pattern[1][3] and "R" in grid_pattern[3][1]:
                    # print(WBR F2T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    
                elif "R" in grid_pattern[1][3] and "B" in grid_pattern[3][1]:
                    # print(WBR F2B")
                    move_list = algs.match_edge_to_corner_left(grid_pattern, move_list)

                if "B" in grid_pattern[1][5] and "R" in grid_pattern[3][7]:
                    # print(WBR F3T")
                    move_list = algs.right_edge_insert_CFOP(grid_pattern, move_list)

                elif "R" in grid_pattern[1][5] and "B" in grid_pattern[3][7]:
                    # print(WBR F3B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = algs.match_edge_to_corner_left(grid_pattern, move_list)
                    

                if "B" in grid_pattern[2][4] and "R" in grid_pattern[3][4]:
                    # print(WBR F4T")
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                elif "R" in grid_pattern[2][4] and "B" in grid_pattern[3][4]:
                    # print(WBR F4B")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = algs.match_edge_to_corner_left(grid_pattern, move_list)

            #white on right
            elif "W" in grid_pattern[3][6]:
                if "B" in grid_pattern[0][4] and "R" in grid_pattern[3][10]:
                    # print(WBR R1T")
                    move_list = algs.match_edge_to_corner_right(grid_pattern, move_list)
                elif "R" in grid_pattern[0][4] and "B" in grid_pattern[3][10]:
                    # print(WBR R1B")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)


                if "B" in grid_pattern[1][3] and "R" in grid_pattern[3][1]:
                    # print(WBR R2T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                elif "R" in grid_pattern[1][3] and "B" in grid_pattern[3][1]:
                    # print(WBR R2B")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)

                if "B" in grid_pattern[1][5] and "R" in grid_pattern[3][7]:
                    # print(WBR R3T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                elif "R" in grid_pattern[1][5] and "B" in grid_pattern[3][7]:
                    # print(WBR R3B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = algs.left_edge_insert_CFOP(grid_pattern, move_list)


                if "B" in grid_pattern[2][4] and "R" in grid_pattern[3][4]:
                    # print(WBR R4T")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = algs.match_edge_to_corner_right(grid_pattern, move_list)

                elif "R" in grid_pattern[2][4] and "B" in grid_pattern[3][4]:
                    # print(WBR R4B")
                    move_list = algs.left_edge_insert_CFOP(grid_pattern, move_list)
            move_list = moves.move_Z(grid_pattern, move_list)
            move_list = moves.move_Z(grid_pattern, move_list)
            move_list = moves.move_D(grid_pattern, move_list)
            move_list = moves.move_D(grid_pattern, move_list)

        #white, orange, blue
        elif "W" in corner and "O" in corner and "B" in corner:
            move_list = moves.move_Z(grid_pattern, move_list)
            move_list = moves.move_Dp(grid_pattern, move_list)
            edge1 = [grid_pattern[0][4], grid_pattern[3][10]]
            edge2 = [grid_pattern[1][3], grid_pattern[3][1]]
            edge3 = [grid_pattern[1][5], grid_pattern[3][7]]
            edge4 = [grid_pattern[2][4], grid_pattern[3][4]]
            # print(edge1, edge2, edge3, edge4)

            #white on top
            if "W" in grid_pattern[2][5]:
                if "O" in grid_pattern[0][4] and "B" in grid_pattern[3][10]:
                    # print(WBR 1T")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "B" in grid_pattern[0][4] and "O" in grid_pattern[3][10]:
                    # print(WBR 1B")
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Lp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_L(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                
                if "O" in grid_pattern[1][3] and "B" in grid_pattern[3][1]:
                    # print(WBR 2T")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = algs.right_edge_insert_CFOP(grid_pattern, move_list)

                    
                elif "B" in grid_pattern[1][3] and "O" in grid_pattern[3][1]:
                    # print(WBR 2B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = algs.left_edge_insert_CFOP(grid_pattern, move_list)

                if "O" in grid_pattern[1][5] and "B" in grid_pattern[3][7]:
                    # print(WBR 3T")
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "B" in grid_pattern[1][5] and "O" in grid_pattern[3][7]:
                    # print(WBR 3B")
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                if "O" in grid_pattern[2][4] and "B" in grid_pattern[3][4]:
                    # print(WBR 4T")
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "B" in grid_pattern[2][4] and "O" in grid_pattern[3][4]:
                    # print(WBR 4B")
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                
            #white on front
            elif "W" in grid_pattern[3][5]:
                if "O" in grid_pattern[0][4] and "B" in grid_pattern[3][10]:
                    # print(WBR F1T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                elif "B" in grid_pattern[0][4] and "O" in grid_pattern[3][10]:
                    # print(WBR F1B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)

                if "O" in grid_pattern[1][3] and "B" in grid_pattern[3][1]:
                    # print(WBR F2T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    
                elif "B" in grid_pattern[1][3] and "O" in grid_pattern[3][1]:
                    # print(WBR F2B")
                    move_list = algs.match_edge_to_corner_left(grid_pattern, move_list)

                if "O" in grid_pattern[1][5] and "B" in grid_pattern[3][7]:
                    # print(WBR F3T")
                    move_list = algs.right_edge_insert_CFOP(grid_pattern, move_list)

                elif "B" in grid_pattern[1][5] and "O" in grid_pattern[3][7]:
                    # print(WBR F3B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = algs.match_edge_to_corner_left(grid_pattern, move_list)
                    

                if "O" in grid_pattern[2][4] and "B" in grid_pattern[3][4]:
                    # print(WBR F4T")
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                elif "B" in grid_pattern[2][4] and "O" in grid_pattern[3][4]:
                    # print(WBR F4B")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = algs.match_edge_to_corner_left(grid_pattern, move_list)

            #white on right
            elif "W" in grid_pattern[3][6]:
                if "O" in grid_pattern[0][4] and "B" in grid_pattern[3][10]:
                    # print(WBR R1T")
                    move_list = algs.match_edge_to_corner_right(grid_pattern, move_list)
                elif "B" in grid_pattern[0][4] and "O" in grid_pattern[3][10]:
                    # print(WBR R1B")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)


                if "O" in grid_pattern[1][3] and "B" in grid_pattern[3][1]:
                    # print(WBR R2T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                elif "B" in grid_pattern[1][3] and "O" in grid_pattern[3][1]:
                    # print(WBO R2B")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)

                if "O" in grid_pattern[1][5] and "B" in grid_pattern[3][7]:
                    # print(WBR R3T")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)

                elif "B" in grid_pattern[1][5] and "O" in grid_pattern[3][7]:
                    # print(WBR R3B")
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_R(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = moves.move_Rp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = algs.left_edge_insert_CFOP(grid_pattern, move_list)


                if "O" in grid_pattern[2][4] and "B" in grid_pattern[3][4]:
                    # print(WBR R4T")
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_Fp(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_U(grid_pattern, move_list)
                    move_list = moves.move_F(grid_pattern, move_list)
                    move_list = moves.move_Up(grid_pattern, move_list)
                    move_list = algs.match_edge_to_corner_right(grid_pattern, move_list)

                elif "B" in grid_pattern[2][4] and "O" in grid_pattern[3][4]:
                    # print(WBR R4B")
                    move_list = algs.left_edge_insert_CFOP(grid_pattern, move_list)
            move_list = moves.move_Zp(grid_pattern, move_list)
            move_list = moves.move_D(grid_pattern, move_list)
        

        else:
            move_list = moves.move_U(grid_pattern, move_list)
    return move_list