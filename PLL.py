import random
import numpy as np
import moves

def matches_pattern(curr_str, pattern):
    return curr_str == pattern

def rotate_letter(letter, steps):
    """Rotates a single letter in the order B -> R -> G -> O -> B."""
    order = "BRGO"  # Define the cycle
    
    index = order.index(letter)
    return order[(index + steps) % 4]  # Rotate by 'steps' positions

def matches_pattern(current_string, target_string):
    """Checks if current_string matches target_string after rotations."""
    for steps in range(4):  # Try 4 different rotations
        transformed = ''.join(rotate_letter(char, steps) for char in current_string)
        if transformed == target_string:
            return True
    return False





def double_corner_swap(grid_pattern, move_list):
    move_list = single_corner_swap(grid_pattern, move_list)
    move_list = single_corner_swap(grid_pattern, move_list)
    return move_list


def single_corner_swap(grid_pattern, move_list):
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_B(grid_pattern, move_list)
    move_list = moves.move_B(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_B(grid_pattern, move_list)
    move_list = moves.move_B(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    return move_list
def F_perm(grid_pattern, move_list):
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
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
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    return move_list
def Ga_perm(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_D(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Dp(grid_pattern, move_list)
    return move_list
def Gb_perm(grid_pattern, move_list):
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Dp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_D(grid_pattern, move_list)
    return move_list
def Gc_perm(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Dp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_D(grid_pattern, move_list)
    return move_list
def Gd_perm(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_D(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Dp(grid_pattern, move_list)
    return move_list
def Ja_perm(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Lp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_L(grid_pattern, move_list)
    return move_list
def Jb_perm(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def Ra_perm(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_D(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Dp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def Rb_perm(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    return move_list
def T_perm(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
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
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def E_perm(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)    
    return move_list
def Na_perm(grid_pattern, move_list):
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    return move_list
def Nb_perm(grid_pattern, move_list):
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    return move_list
def V_perm(grid_pattern, move_list):
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Dp(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_D(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Dp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_D(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    return move_list
def Y_perm(grid_pattern, move_list):
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_Rp(grid_pattern, move_list)
    move_list = moves.move_F(grid_pattern, move_list)
    move_list = moves.move_R(grid_pattern, move_list)
    move_list = moves.move_Fp(grid_pattern, move_list)
    return move_list
def H_perm(grid_pattern, move_list):
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    return move_list
def Ua_perm(grid_pattern, move_list):
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    return move_list
def Ub_perm(grid_pattern, move_list):
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_Up(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    return move_list
def Z_perm(grid_pattern, move_list):
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_Mp(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_U(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    move_list = moves.move_M(grid_pattern, move_list)
    return move_list



def pll_solver(grid_pattern, move_list):
    while True:
        edges = grid_pattern[3]
        curr_str = "".join(str(cell) for cell in edges)
        if curr_str == "RRRGGGOOOBBB":
            break
        patterns = [
            ("ROOBBRGRGOGB", double_corner_swap),#
            ("GOOBBGORBRGR", single_corner_swap),#
            ("OOOBGRGRBRBG", F_perm),#
            ("OGOBRRGOBRBG", Ga_perm),#
            ("OROBGRGBBROG", Gb_perm),#
            ("OBOBGRGOBRRG", Gc_perm),#
            ("OROBORGGBRBG", Gd_perm),#
            ("OOOBBRGGBRRG", Ja_perm),#
            ("GGGOBBROOBRR", Jb_perm),#
            ("GRGOOBRBOBGR", Ra_perm),#
            ("BRBRBGOGRGOO", Rb_perm),#
            ("OROBBRGOBRGG", T_perm),#
            ("BOGOBRGRBRGO", E_perm),#
            ("ORRGBBROOBGG", Na_perm),#
            ("RROBBGOORGGB", Nb_perm),#
            ("ROOBBGOGRGRB", V_perm),#
            ("RGOBBGORRGOB", Y_perm),#
            ("OROBGBRORGBG", H_perm),#
            ("OBOBRBRORGGG", Ua_perm),#
            ("OROBOBRBRGGG", Ub_perm),#
            ("GOGOGOBRBRBR", Z_perm),#
        ]

        for pattern, func in patterns:
            if matches_pattern(curr_str, pattern):
                move_list = func(grid_pattern, move_list)
                return move_list
        
        move_list = moves.move_U(grid_pattern, move_list)
    return move_list

def pll(grid_pattern, move_list):
    while grid_pattern[3] != ["R", "R", "R", "G", "G", "G", "O", "O", "O", "B", "B", "B"]:
        move_list = pll_solver(grid_pattern, move_list)

    while grid_pattern[3][4] != "G":
                    move_list = moves.move_U(grid_pattern, move_list)

    return move_list