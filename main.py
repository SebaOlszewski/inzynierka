import time
import psutil
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

grid_pattern = solved_cube.copy()

# Normal test
total_solves = sum(1 for _ in open("scrambles.txt"))
with open("solve_data.csv", "w", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([
        "Index", "LBL Time (ms)", "LBL Moves", "LBL CPU Usage", "LBL Memory Used (MB)",
        "Blind Time (ms)", "Blind Moves", "Blind CPU Usage", "Blind Memory Used (MB)",
        "CFOP Time (ms)", "CFOP Moves", "CFOP CPU Usage", "CFOP Memory Used (MB)"
    ])
    
    with open("scrambles.txt", "r") as file:
        for x, scrmbl in enumerate(file):
            scrmbl = scrmbl.strip()
            
            # LBL Solve
            for move in scrmbl:
                lbl_grid = moves.move(grid_pattern, move.upper())
            
            LBL_move_list = ""
            LBL_START_TIME = time.time()
            LBL_move_list = LBL.LBL_FULL(lbl_grid, LBL_move_list)
            LBL_FINISH_TIME = time.time() - LBL_START_TIME
            LBL_move_list = len(str(LBL_move_list)[4:])
            LBL_stop_cpu_usage = psutil.cpu_percent(0.1)
            LBL_memory_used = psutil.virtual_memory().used / (1024 * 1024)  # Convert to MB
            
            # Blind Solve
            for move in scrmbl:
                blind_grid = moves.move(grid_pattern, move.upper())
            
            BLIND_move_list = ""
            BLIND_START_TIME = time.time()
            BLIND_move_list = BLIND.solve_blind(blind_grid, BLIND_move_list)
            BLIND_FINISH_TIME = time.time() - BLIND_START_TIME
            BLIND_move_list = len(str(BLIND_move_list)[4:])
            BLIND_stop_cpu_usage = psutil.cpu_percent(0.1)
            BLIND_memory_used = psutil.virtual_memory().used / (1024 * 1024)  # Convert to MB
            
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
            CFOP_stop_cpu_usage = psutil.cpu_percent(interval=0.1)
            CFOP_memory_used = psutil.virtual_memory().used / (1024 * 1024)  # Convert to MB
            
            # Save results
            csv_writer.writerow([
                x, 
                (LBL_FINISH_TIME) * 1000, LBL_move_list, LBL_stop_cpu_usage, LBL_memory_used,
                (BLIND_FINISH_TIME) * 1000, BLIND_move_list, BLIND_stop_cpu_usage, BLIND_memory_used,
                (CFOP_STOP_TIME) * 1000, CFOP_move_list, CFOP_stop_cpu_usage, CFOP_memory_used
            ])

            # Print progress every 10 solves
            if x % 10 == 0:
                print(f"Progress: {x}/{total_solves} solves completed.")

print("All solves completed.")
plot_data.plot_solve_data("solve_data.csv")