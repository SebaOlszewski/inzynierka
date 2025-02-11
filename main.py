
import time
import csv
import moves
import LBL 
import BLIND
import F2L
import OLL
import PLL

import plot_data

# Define grid pattern and edges
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

grid_pattern = solved_cube.copy()
        
x = 0
total_solves = sum(1 for _ in open("scrambles.txt"))  # Count total lines (scrambles)

with open("solve_data.csv", "w", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([
        "Index", "LBL Time (ms)", "LBL Moves",
        "Blind Time (ms)", "Blind Moves",
        "CFOP Time (ms)", "CFOP Moves",
    ])
    with open("scrambles.txt", "r") as file:
        for scrmbl in file:
            
            scrmbl = scrmbl.strip()           
            
            # LBL Solve
            for move in scrmbl:
                lbl_grid = moves.move(grid_pattern, move.upper())
            LBL_move_list = ""
            LBL_START_TIME = time.time()
            LBL_move_list = LBL.LBL_FULL(lbl_grid, LBL_move_list)
            LBL_FINISH_TIME =  time.time() - LBL_START_TIME
            LBL_move_list = len(str(LBL_move_list)[4:])
            
            while LBL_FINISH_TIME == 0:
                LBL_move_list = ""
                LBL_START_TIME = time.time()
                LBL_move_list = LBL.LBL_FULL(lbl_grid, LBL_move_list)
                LBL_FINISH_TIME =  time.time() - LBL_START_TIME
                LBL_move_list = len(str(LBL_move_list)[4:])
            # Blind Solve
            for move in scrmbl:
                blind_grid = moves.move(grid_pattern, move.upper())
            BLIND_move_list = ""
            BLIND_START_TIME = time.time()
            BLIND_move_list = BLIND.solve_blind(blind_grid, BLIND_move_list)
            BLIND_FINISH_TIME = time.time() - BLIND_START_TIME 
            BLIND_move_list = len(str(BLIND_move_list)[4:])
            
            while BLIND_FINISH_TIME == 0:
                BLIND_move_list = ""
                BLIND_START_TIME = time.time()
                BLIND_move_list = BLIND.solve_blind(blind_grid, BLIND_move_list)
                BLIND_FINISH_TIME = time.time() - BLIND_START_TIME 
                BLIND_move_list = len(str(BLIND_move_list)[4:])
            # CFOP Solve
            for move in scrmbl:
                cfop_grid = moves.move(grid_pattern, move.upper())
            CFOP_move_list = ""
            CFOP_START_TIME = time.time()
            CFOP_move_list = F2L.solve_2_layers(cfop_grid, CFOP_move_list)
            CFOP_move_list = OLL.oll(cfop_grid, CFOP_move_list)
            CFOP_move_list = PLL.pll(cfop_grid, CFOP_move_list)
            CFOP_STOP_TIME = time.time() - CFOP_START_TIME
            CFOP_move_list = len(str(CFOP_move_list)[4:])
            
            while CFOP_STOP_TIME == 0:
                CFOP_move_list = ""
                CFOP_START_TIME = time.time()
                CFOP_move_list = F2L.solve_2_layers(cfop_grid, CFOP_move_list)
                CFOP_move_list = OLL.oll(cfop_grid, CFOP_move_list)
                CFOP_move_list = PLL.pll(cfop_grid, CFOP_move_list)
                CFOP_STOP_TIME = time.time() - CFOP_START_TIME
                CFOP_move_list = len(str(CFOP_move_list)[4:])
            # Save results
            csv_writer.writerow([
                x, 
                (LBL_FINISH_TIME) * 1000, LBL_move_list,
                (BLIND_FINISH_TIME) * 1000, BLIND_move_list,
                (CFOP_STOP_TIME) * 1000, CFOP_move_list,
            ])

            # Print progress every 10 solves
            x += 1
            if x % 10 == 0:
                print(f"Progress: {x}/{total_solves} solves completed.")

print("All solves completed.")
plot_data.plot_solve_data("solve_data.csv")