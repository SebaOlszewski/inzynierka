import random
import numpy as np
import moves

def matches_pattern(curr_str, pattern):
    return all(p == 'X' or p == c for p, c in zip(pattern, curr_str))

def dot_1(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def dot_2(grid_pattern, move_list): 
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def dot_3(grid_pattern, move_list):
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    return move_list
def dot_4(grid_pattern, move_list):
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    return move_list
def square_1(grid_pattern, move_list):
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    return move_list
def square_2(grid_pattern, move_list):
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def small_bolt_1(grid_pattern, move_list):
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def small_bolt_2(grid_pattern, move_list):
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    return move_list
def fish_1(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def fish_2(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def small_bolt_3(grid_pattern, move_list):
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def small_bolt_4(grid_pattern, move_list):
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def knight_move1(grid_pattern, move_list):
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def knight_move2(grid_pattern, move_list):
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def knight_move3(grid_pattern, move_list):
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    return move_list
def knight_move4(grid_pattern, move_list):
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def dot_5(grid_pattern, move_list):
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    return move_list
def dot_6(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    return move_list
def dot_7(grid_pattern, move_list):
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def dot_8(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)  
    return move_list
def cross_1(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def cross_2(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    return move_list
def cross_3(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Dp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_D(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    return move_list
def cross_4(grid_pattern, move_list):
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def cross_5(grid_pattern, move_list):
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    return move_list
def cross_6(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def cross_7(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def corners_oriented_1(grid_pattern, move_list):
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def awkward_shape_1(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def awkward_shape_2(grid_pattern, move_list):
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    return move_list
def p_shape_1(grid_pattern, move_list):
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    return move_list
def p_shape_2(grid_pattern, move_list):
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    return move_list
def t_shape_1(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def c_shape_1(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def fish_3(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)   
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def w_shape_1(grid_pattern, move_list):
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    return move_list
def fish_4(grid_pattern, move_list):
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def w_shape_2(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def big_lightning_1(grid_pattern, move_list):
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    return move_list
def big_lightning_2(grid_pattern, move_list):
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    return move_list
def awkward_shape_3(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def awkward_shape_4(grid_pattern, move_list):
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def p_shape_3(grid_pattern, move_list):
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    return move_list
def p_shape_4(grid_pattern, move_list):
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def t_shape_2(grid_pattern, move_list):
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def c_shape_2(grid_pattern, move_list):
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    return move_list
def l_shape_1(grid_pattern, move_list):
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    return move_list
def l_shape_2(grid_pattern, move_list):
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def l_shape_3(grid_pattern, move_list):
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    return move_list
def l_shape_4(grid_pattern, move_list):
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def I_shape_1(grid_pattern, move_list):
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def I_shape_2(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_B(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Bp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def l_shape_5(grid_pattern, move_list):
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    return move_list
def l_shape_6(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    return move_list
def I_shape_3(grid_pattern, move_list):
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def I_shape_4(grid_pattern, move_list):
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    return move_list
def corners_oriented_2(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list

def oll(grid_pattern, move_list):
    for x in range(5):
        edges = grid_pattern[3]
        yellow_face = [grid_pattern[0][3], grid_pattern[0][4], grid_pattern[0][5],
                    grid_pattern[1][3], grid_pattern[1][4], grid_pattern[1][5],
                    grid_pattern[2][3], grid_pattern[2][4], grid_pattern[2][5]] 

        edges_str = "".join(str(cell) for cell in edges)
        yellow_face_str = "".join(str(cell) for cell in yellow_face)
        curr_str = edges_str + yellow_face_str
        
        patterns = [
            ("YYYXYXYYYXYXXXXXYXXXX", dot_1),
            ("XYYXYXYYXYYYXXXXYXXXX", dot_2),
            ("XYXXYYXYYXYYXXXXYXYXX", dot_3),
            ("YYXYYXXYXYYXXXXXYXXXY", dot_4),
            ("XXYXYYXYYXXXYYXYYXXXX", square_1),
            ("YYXYYXYXXXXXXYYXYYXXX", square_2),
            ("XXXXYYXYYXXYXYXYYXYXX", small_bolt_1),
            ("YYXYYXXXXYXXXYXXYYXXY", small_bolt_2),
            ("YXXYYXXYXYXXXYXYYXXXY", fish_1),
            ("XXYXXYXYXXYYXXYYYXXYX", fish_2),
            ("XXYXYYXYXXXYXYYYYXXXX", small_bolt_3),
            ("XYXYYXYXXYXXYYXXYYXXX", small_bolt_4),
            ("XXXXYYXXYXYYXXXYYYYXX", knight_move1),
            ("YXXYYXXXXYYXXXXYYYXXY", knight_move2),
            ("XXYXYYXXYXYXYXXYYYXXX", knight_move3),
            ("YXXYYXYXXXYXXXYYYYXXX", knight_move4),
            ("XYXYYXXYYXYXYXXXYXXXY", dot_5),
            ("XYXYYYXYXXYXYXYXYXXXX", dot_6),
            ("XYYXYXYYXXYXYXYXYXXXX", dot_7),
            ("XYXXYXXYXXYXYXYXYXYXY", dot_8),
            ("XXXYXYXXXYXYXYXYYYXYX", cross_1),
            ("YXYXXYXXXYXXXYXYYYXYX", cross_2),
            ("XXXXXXXXXYXYXYXYYYYYY", cross_3),
            ("XXXYXXXXXXXYXYYYYYXYY", cross_4),
            ("YXXXXYXXXXXXXYYYYYYYX", cross_5),
            ("YXXYXXYXXXXXXYYYYYXYX", cross_6),
            ("XXXXXYXXYXXYXYXYYYYYX", cross_7),
            ("XXXXYXXYXXXXYYYYYXYXY", corners_oriented_1),
            ("XXXYYXXYXXXYXYYYYXXXY", awkward_shape_1),
            ("YXXXYXXYYXXXXYXYYXYXY", awkward_shape_2),
            ("XYXYYXXXXXXYXYYXYYXXY", p_shape_1),
            ("XXXXYYXYXYXXYYXYYXYXX", p_shape_2),
            ("XXXYYXXXXXYYXXYYYYXXY", t_shape_1),
            ("YXXXYXXXYXYXXXXYYYYXY", c_shape_1),
            ("XYXYXXXXYXYXYXXXYYXYY", fish_3),
            ("XYYXYXXXXYXXYYXXYYXXY", w_shape_1),
            ("XXXYYXXYYXXXYYXYYXXXY", fish_4),
            ("XXXXYXYYXXXYXYYYYXYXX", w_shape_2),
            ("XXXXYXYXXXYYXXYYYYYXX", big_lightning_1),
            ("XXYXYXXXXYYXYXXYYYXXY", big_lightning_2),
            ("XXXXYXXYXYXYXYXYYXYXY", awkward_shape_3),
            ("XXXYXYXYXXYXYXYYYXXYX", awkward_shape_4),
            ("YYYXYXXXXXXXXYYXYYXXY", p_shape_3),
            ("XXXXYXYYYXXXYYXYYXYXX", p_shape_4),
            ("YXYXYXXXXXYXXXYYYYXXY", t_shape_2),
            ("XYXXXXYYYXXXYYXXYXYYX", c_shape_2),
            ("XYXYYXYXYXXYXYXXYYXXX", l_shape_1),
            ("YXYXYYXYXYXXXYXYYXXXX", l_shape_2),
            ("YYYXYYXXXYXXXYXXYYXXX", l_shape_3),
            ("YYYXXYXXXYYXXXXXYYXYX", l_shape_4),
            ("XXXYYXYXYXYYXXXYYYXXX", I_shape_1),
            ("XYXYXXYYYXXYXYXXYXXYX", I_shape_2),
            ("XYXYYYXXXYXYXYXXYYXXX", l_shape_5),
            ("XXXYYYXYXYXYXYXYYXXXX", l_shape_6),
            ("XXXYYYXXXYYYXXXYYYXXX", I_shape_3),
            ("YXYXYXYXYXYXXXXYYYXXX", I_shape_4),
            ("XXXXYXXXXXYXYXYYYYYXY", corners_oriented_2)
        ]

        for pattern, func in patterns:
            if matches_pattern(curr_str, pattern):
                move_list = func(grid_pattern, move_list)
                #print(func.__name__)  # Print function name
                return move_list
        
        move_list = moves.move_U(grid_pattern, move_list)
    

    return move_list