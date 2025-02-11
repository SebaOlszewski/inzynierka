import random
import numpy as np
import moves

solved_cube = [
    #       0       1       2       3     4    5    6   7   8        9  10  11
            [0,     0,      0,      'Y', 'Y', 'Y',  0,  0,  0,       0, 0, 0],        #0
            [0,     0,      0,      'Y', 'Y', 'Y',  0,  0,  0,       0, 0, 0],        #1    
            [0,     0,      0,      'Y', 'Y', 'Y',  0,  0,  0,       0, 0, 0],        #2
            ['R',   'R',    'R',    'G', 'G', 'G', 'O', 'O', 'O',   'B', 'B', 'B'],   #3
            ['R',   'R',    'R',    'G', 'G', 'G', 'O', 'O', 'O',   'B', 'B', 'B'],   #4
            ['R',   'R',    'R',    'G', 'G', 'G', 'O', 'O', 'O',   'B', 'B', 'B'],   #5
            [0,     0,      0,      'W', 'W', 'W',  0,  0,  0,      0, 0, 0],         #6
            [0,     0,      0,      'W', 'W', 'W',  0,  0,  0,      0, 0, 0],         #7
            [0,     0,      0,      'W', 'W', 'W',  0,  0,  0,      0, 0, 0]          #8
        ] 


def scramble(grid_pattern):
    with open("scrambles.txt", "w") as file:
        for _ in range(10000):
            scrmbl = ''.join(random.choices('FBUDLF', k=20))
            file.write(scrmbl + "\n")
    return grid_pattern


scramble(solved_cube)