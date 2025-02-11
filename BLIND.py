import random
import numpy as np
import moves
import BLIND_moves


def solve_blind(blind_grid, move_list):
    move_list = solve_edges(blind_grid, move_list)
    move_list = solve_corners(blind_grid, move_list)
    return move_list

def solve_edges(blind_grid, move_list):
    edge_string = ""
    used_letters = set()
    all_letters = set("ABCDEFGHIJKLMNOPRSTUWXYZ")
    
    while used_letters != all_letters:
        current_letter = blind_grid[1][5]
        
        if current_letter in used_letters:
            remaining_letters = all_letters - used_letters
            if remaining_letters:
                current_letter = remaining_letters.pop()
            else:
                break
        
        edge_string += current_letter
        used_letters.add(current_letter)
        
        if current_letter == "A":
            move_list = BLIND_moves.edge_A(blind_grid, move_list)
            used_letters.add("R")
        elif current_letter == "B":
            move_list = BLIND_moves.edge_B(blind_grid, move_list)
            used_letters.add("M")
        elif current_letter == "C":
            move_list = BLIND_moves.edge_C(blind_grid, move_list)
            used_letters.add("I")
        elif current_letter == "D":
            move_list = BLIND_moves.edge_D(blind_grid, move_list)
            used_letters.add("E")
        elif current_letter == "E":
            move_list = BLIND_moves.edge_E(blind_grid, move_list)
            used_letters.add("D")
        elif current_letter == "F":
            move_list = BLIND_moves.edge_F(blind_grid, move_list)
            used_letters.add("L")
        elif current_letter == "G":
            move_list = BLIND_moves.edge_G(blind_grid, move_list)
            used_letters.add("Z")
        elif current_letter == "H":
            move_list = BLIND_moves.edge_H(blind_grid, move_list)
            used_letters.add("S")
        elif current_letter == "I":
            move_list = BLIND_moves.edge_I(blind_grid, move_list)
            used_letters.add("C")
        elif current_letter == "J":
            move_list = BLIND_moves.edge_J(blind_grid, move_list)
            used_letters.add("P")
        elif current_letter == "K":
            move_list = BLIND_moves.edge_K(blind_grid, move_list)
            used_letters.add("W")
        elif current_letter == "L":
            move_list = BLIND_moves.edge_L(blind_grid, move_list)
            used_letters.add("F")
        elif current_letter == "M":
            move_list = BLIND_moves.edge_M(blind_grid, move_list)
            used_letters.add("B")
        elif current_letter == "N":
            move_list = BLIND_moves.edge_N(blind_grid, move_list)
            used_letters.add("U")
        elif current_letter == "O":
            move_list = BLIND_moves.edge_O(blind_grid, move_list)
            used_letters.add("N")
        elif current_letter == "P":
            move_list = BLIND_moves.edge_P(blind_grid, move_list)
            used_letters.add("J")
        elif current_letter == "R":
            move_list = BLIND_moves.edge_R(blind_grid, move_list)
            used_letters.add("A")
        elif current_letter == "S":
            move_list = BLIND_moves.edge_S(blind_grid, move_list)
            used_letters.add("H")
        elif current_letter == "T":
            move_list = BLIND_moves.edge_T(blind_grid, move_list)
            used_letters.add("Y")
        elif current_letter == "U":
            move_list = BLIND_moves.edge_U(blind_grid, move_list)
            used_letters.add("N")
        elif current_letter == "W":
            move_list = BLIND_moves.edge_W(blind_grid, move_list)
            used_letters.add("K")
        elif current_letter == "X":
            move_list = BLIND_moves.edge_X(blind_grid, move_list)
            used_letters.add("O")
        elif current_letter == "Y":
            move_list = BLIND_moves.edge_Y(blind_grid, move_list)
            used_letters.add("T")
        elif current_letter == "Z":
            move_list = BLIND_moves.edge_Z(blind_grid, move_list)
            used_letters.add("G")

    return move_list

    # print(edge_string)
def solve_corners(blind_grid, move_list):
    corner_string = ""
    used_letters = set()
    all_letters = set("ABCDEFGHIJKLMNOPRSTUWXYZ")
    
    while used_letters != all_letters:
        current_letter = blind_grid[3][0]
        
        if current_letter in used_letters:
            remaining_letters = all_letters - used_letters
            if remaining_letters:
                current_letter = remaining_letters.pop()
            else:
                break
        
        corner_string += current_letter
        used_letters.add(current_letter)
        
        if current_letter == "A":
            move_list = BLIND_moves.corner_A(blind_grid, move_list)
            used_letters.add("E")
            used_letters.add("S")
        elif current_letter == "B":
            move_list = BLIND_moves.corner_B(blind_grid, move_list)
            used_letters.add("N")
            used_letters.add("R")
        elif current_letter == "C":
            move_list = BLIND_moves.corner_C(blind_grid, move_list)
            used_letters.add("J")
            used_letters.add("M")
        elif current_letter == "D":
            move_list = BLIND_moves.corner_D(blind_grid, move_list)
            used_letters.add("I")
            used_letters.add("F")
        elif current_letter == "E":
            move_list = BLIND_moves.corner_E(blind_grid, move_list)
            used_letters.add("A")
            used_letters.add("S")
        elif current_letter == "F":
            move_list = BLIND_moves.corner_F(blind_grid, move_list)
            used_letters.add("D")
            used_letters.add("I")
        elif current_letter == "G":
            move_list = BLIND_moves.corner_G(blind_grid, move_list)
            used_letters.add("L")
            used_letters.add("W")
        elif current_letter == "H":
            move_list = BLIND_moves.corner_H(blind_grid, move_list)
            used_letters.add("Z")
            used_letters.add("T")
        elif current_letter == "I":
            move_list = BLIND_moves.corner_I(blind_grid, move_list)
            used_letters.add("D")
            used_letters.add("F")
        elif current_letter == "J":
            move_list = BLIND_moves.corner_J(blind_grid, move_list)
            used_letters.add("C")
            used_letters.add("M")
        elif current_letter == "K":
            move_list = BLIND_moves.corner_K(blind_grid, move_list)
            used_letters.add("P")
            used_letters.add("X")
        elif current_letter == "L":
            move_list = BLIND_moves.corner_L(blind_grid, move_list)
            used_letters.add("W")
            used_letters.add("G")
        elif current_letter == "M":
            move_list = BLIND_moves.corner_M(blind_grid, move_list)
            used_letters.add("C")
            used_letters.add("J")
        elif current_letter == "N":
            move_list = BLIND_moves.corner_N(blind_grid, move_list)
            used_letters.add("R")
            used_letters.add("B")
        elif current_letter == "O":
            move_list = BLIND_moves.corner_O(blind_grid, move_list)
            used_letters.add("U")
            used_letters.add("Y")
        elif current_letter == "P":
            move_list = BLIND_moves.corner_P(blind_grid, move_list)
            used_letters.add("K")
            used_letters.add("X")
        elif current_letter == "R":
            move_list = BLIND_moves.corner_R(blind_grid, move_list)
            used_letters.add("N")
            used_letters.add("B")
        elif current_letter == "S":
            move_list = BLIND_moves.corner_S(blind_grid, move_list)
            used_letters.add("B")
            used_letters.add("E")
        elif current_letter == "T":
            move_list = BLIND_moves.corner_T(blind_grid, move_list)
            used_letters.add("Y")
            used_letters.add("H")
        elif current_letter == "U":
            move_list = BLIND_moves.corner_U(blind_grid, move_list)
            used_letters.add("O")
            used_letters.add("Y")
        elif current_letter == "W":
            move_list = BLIND_moves.corner_W(blind_grid, move_list)
            used_letters.add("L")
            used_letters.add("G")
        elif current_letter == "X":
            used_letters.add("K")
            used_letters.add("P")
        elif current_letter == "Y":
            move_list = BLIND_moves.corner_Y(blind_grid, move_list)
            used_letters.add("O")
            used_letters.add("U")
        elif current_letter == "Z":
            move_list = BLIND_moves.corner_Z(blind_grid, move_list)
            used_letters.add("T")
            used_letters.add("H")
    # print(corner_string)


    return move_list