import random
import numpy as np
import moves

def checkers(grid_pattern):
    grid_pattern = moves.move(grid_pattern, "C")
    predefined_moves = 'uuddffbbllrr'
    for move in predefined_moves:
        grid_pattern = moves.move(grid_pattern, move.upper())
    return grid_pattern

def scramble(grid_pattern, scramble_list):
    with open("scrambles.txt", "w") as file:
        for _ in range(1000):
            scrmbl = ''.join(random.choices('FBUDLF', k=20))
            file.write(scrmbl + "\n")
            for move in scrmbl:
                grid_pattern = moves.move(grid_pattern, move.upper())
    return grid_pattern

def center_cube(grid_pattern, move_list):
    while grid_pattern[4][4] != "G":
            move_list = moves.move_Z(grid_pattern, move_list)
    while grid_pattern[5][4] != "G":
            move_list = moves.move_D(grid_pattern, move_list)
    return move_list

def ruru(grid_pattern, move_list):
        move_list = moves.move_R(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_Rp(grid_pattern, move_list)
        move_list = moves.move_Up(grid_pattern, move_list)
        return move_list

def edge_to_right(grid_pattern, move_list):
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_R(grid_pattern, move_list)
        move_list = moves.move_Up(grid_pattern, move_list)
        move_list = moves.move_Rp(grid_pattern, move_list)
        move_list = moves.move_Up(grid_pattern, move_list)
        move_list = moves.move_Fp(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_F(grid_pattern, move_list)
        return move_list
def edge_to_left(grid_pattern, move_list):
        
        move_list = moves.move_Up(grid_pattern, move_list)
        move_list = moves.move_Lp(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_L(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_F(grid_pattern, move_list)
        move_list = moves.move_Up(grid_pattern, move_list)
        move_list = moves.move_Fp(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        return move_list
def swap_to_left(grid_pattern, move_list):
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_L(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_Lp(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_L(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_Lp(grid_pattern, move_list)
        return move_list
def swap_to_right(grid_pattern, move_list):
        move_list = moves.move_Up(grid_pattern, move_list)
        move_list = moves.move_Rp(grid_pattern, move_list)
        move_list = moves.move_Up(grid_pattern, move_list)
        move_list = moves.move_R(grid_pattern, move_list)
        move_list = moves.move_Up(grid_pattern, move_list)
        move_list = moves.move_Rp(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_R(grid_pattern, move_list)
        return move_list
def swap_corners(grid_pattern, move_list):

        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_R(grid_pattern, move_list)
        move_list = moves.move_Up(grid_pattern, move_list)
        move_list = moves.move_Lp(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_Rp(grid_pattern, move_list)
        move_list = moves.move_Up(grid_pattern, move_list)
        move_list = moves.move_L(grid_pattern, move_list)
        return move_list
def right_edge_insert_CFOP(grid_pattern, move_list):
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_R(grid_pattern, move_list)
        move_list = moves.move_Up(grid_pattern, move_list)
        move_list = moves.move_Rp(grid_pattern, move_list)
        return move_list
def left_edge_insert_CFOP(grid_pattern, move_list):
        move_list = moves.move_Up(grid_pattern, move_list)
        move_list = moves.move_Fp(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_F(grid_pattern, move_list)
        return move_list
def match_edge_to_corner_left(grid_pattern, move_list):
        move_list = moves.move_Fp(grid_pattern, move_list)
        move_list = moves.move_Up(grid_pattern, move_list)
        move_list = moves.move_F(grid_pattern, move_list)
        return move_list
def match_edge_to_corner_right(grid_pattern, move_list):
        move_list = moves.move_R(grid_pattern, move_list)
        move_list = moves.move_U(grid_pattern, move_list)
        move_list = moves.move_Rp(grid_pattern, move_list)
        return move_list