import random
import numpy as np
import moves


def T_perm(blind_grid, move_list):
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_U(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_Up(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_F(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_Up(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_Up(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_U(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_Fp(blind_grid, move_list)
    return move_list
def edge_A(blind_grid, move_list):
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_Up(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_U(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    return move_list 
def edge_B(blind_grid, move_list):
    return move_list

def edge_C(blind_grid, move_list):
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_U(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_U(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    return move_list
def edge_D(blind_grid, move_list):
    move_list = T_perm(blind_grid, move_list)
    return move_list
def edge_E(blind_grid, move_list):
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_Z(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = moves.move_Zp(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    return move_list
def edge_F(blind_grid, move_list):
    move_list = moves.move_Z(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = moves.move_Zp(blind_grid, move_list)
    return move_list
def edge_G(blind_grid, move_list):
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_Zp(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_Z(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    return move_list
def edge_H(blind_grid, move_list):
    move_list = moves.move_Zp(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_Z(blind_grid, move_list)
    return move_list
def edge_I(blind_grid, move_list):
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_Fp(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_F(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    return move_list
def edge_K(blind_grid, move_list):
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_F(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_Fp(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    return move_list
def edge_J(blind_grid, move_list):
    move_list = moves.move_Z(blind_grid, move_list)
    move_list = moves.move_Z(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = moves.move_Z(blind_grid, move_list)
    move_list = moves.move_Z(blind_grid, move_list)
    return move_list
def edge_L(blind_grid, move_list):
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    return move_list
def edge_M(blind_grid, move_list):
    return move_list

def edge_N(blind_grid, move_list):
    move_list = moves.move_Zp(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = moves.move_Z(blind_grid, move_list)
    return move_list
def edge_O(blind_grid, move_list):
    move_list = moves.move_Dp(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_F(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_Fp(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    return move_list
def edge_P(blind_grid, move_list):
    move_list = moves.move_Z(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_Zp(blind_grid, move_list)
    return move_list
def edge_R(blind_grid, move_list):
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_B(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = moves.move_Bp(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    return move_list
def edge_S(blind_grid, move_list):
    move_list = moves.move_L(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    return move_list
def edge_T(blind_grid, move_list):
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_Bp(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = moves.move_B(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    return move_list
def edge_U(blind_grid, move_list):
    move_list = moves.move_Z(blind_grid, move_list)
    move_list = moves.move_Z(blind_grid, move_list)
    move_list = moves.move_Lp(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_Z(blind_grid, move_list)
    move_list = moves.move_Z(blind_grid, move_list)
    return move_list
def edge_W(blind_grid, move_list):
    move_list = moves.move_Dp(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    return move_list
def edge_X(blind_grid, move_list):
    move_list = moves.move_Dp(blind_grid, move_list)
    move_list = moves.move_Dp(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    return move_list
def edge_Y(blind_grid, move_list):
    move_list = moves.move_D(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_Dp(blind_grid, move_list)
    return move_list
def edge_Z(blind_grid, move_list):
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = T_perm(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    move_list = moves.move_L(blind_grid, move_list)
    return move_list

def swap_corners(blind_grid, move_list):
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_Up(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_Up(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_U(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_Fp(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_U(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_Up(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_F(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    return move_list

def corner_A(blind_grid, move_list):
    return move_list

def corner_B(blind_grid, move_list):
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    return move_list
def corner_C(blind_grid, move_list):
    move_list = moves.move_F(blind_grid, move_list)
    move_list = moves.move_F(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_F(blind_grid, move_list)
    move_list = moves.move_F(blind_grid, move_list)
    return move_list
def corner_D(blind_grid, move_list):
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_Dp(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    return move_list
def corner_E(blind_grid, move_list):
    return move_list

def corner_F(blind_grid, move_list):
    move_list = moves.move_Fp(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_Dp(blind_grid, move_list)
    move_list = moves.move_F(blind_grid, move_list)
    return move_list
def corner_G(blind_grid, move_list):
    move_list = moves.move_Fp(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_F(blind_grid, move_list)
    return move_list
def corner_H(blind_grid, move_list):
    move_list = moves.move_D(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_Dp(blind_grid, move_list)
    return move_list
def corner_I(blind_grid, move_list):
    move_list = moves.move_F(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_Fp(blind_grid, move_list)
    return move_list
def corner_J(blind_grid, move_list):
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    return move_list
def corner_K(blind_grid, move_list):
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_Dp(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    return move_list
def corner_L(blind_grid, move_list):
    move_list = moves.move_D(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    return move_list
def corner_M(blind_grid, move_list):
    move_list = moves.move_F(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_Fp(blind_grid, move_list) 
    return move_list
def corner_N(blind_grid, move_list):
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_F(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_Fp(blind_grid, move_list) 
    move_list = moves.move_R(blind_grid, move_list)
    return move_list
def corner_O(blind_grid, move_list):
    move_list = moves.move_Dp(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = moves.move_Dp(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    return move_list
def corner_P(blind_grid, move_list):
    move_list = moves.move_F(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_Dp(blind_grid, move_list)
    move_list = moves.move_Fp(blind_grid, move_list)
    return move_list
def corner_R(blind_grid, move_list):
    move_list = moves.move_R(blind_grid, move_list)
    move_list = moves.move_Dp(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    move_list = moves.move_Rp(blind_grid, move_list)
    return move_list
def corner_S(blind_grid, move_list):
    return move_list

def corner_T(blind_grid, move_list):
    move_list = moves.move_Dp(blind_grid, move_list)
    move_list = moves.move_Fp(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    return move_list
def corner_U(blind_grid, move_list):
    move_list = moves.move_Rp(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_R(blind_grid, move_list)
    return move_list
def corner_W(blind_grid, move_list):
    move_list = moves.move_D(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_Dp(blind_grid, move_list)
    return move_list
def corner_X(blind_grid, move_list): 
    move_list = swap_corners(blind_grid, move_list)
    return move_list
def corner_Y(blind_grid, move_list):
    move_list = moves.move_Dp(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    return move_list
def corner_Z(blind_grid, move_list):
    move_list = moves.move_D(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    move_list = swap_corners(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    move_list = moves.move_D(blind_grid, move_list)
    return move_list