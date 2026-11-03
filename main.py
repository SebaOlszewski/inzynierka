# main.py
import csv
import random
import sys
import time
import tracemalloc
import os
from concurrent.futures import ProcessPoolExecutor
import matplotlib.pyplot as plt
from datetime import datetime
from cube_bitboard import BitCube
import lbl_bit
import cfop_bit
import blind_bit
import optimal_bit

SCRAMBLES_FILE = "scrambles.txt"
CSV_OUTPUT_FILE = "solve_data.csv"

# Zaktualizowane nagłówki dla 4 przebiegów (Single-Core i Multi-Core)
CSV_HEADER = ["Index"]
for prefix in ["LBL", "Blind", "CFOP", "Optimal"]:
    CSV_HEADER.extend([
        f"{prefix} SC Time (ms)", f"{prefix} SC Moves", f"{prefix} SC CPU Usage", f"{prefix} SC Mem (MB)",
        f"{prefix} MC Time (ms)", f"{prefix} MC Moves", f"{prefix} MC CPU Usage", f"{prefix} MC Mem (MB)"
    ])

FACE_COLORS = {
    'W': '#FFFFFF',
    'Y': '#FFD500',
    'G': '#009B48',
    'B': '#0046AD',
    'O': '#FF5800',
    'R': '#B71234'
}


def print_progress_bar(mode, current, total, elapsed_s, bar_length=24):
    ratio = current / total if total > 0 else 1.0
    filled = int(bar_length * ratio)
    bar = "█" * filled + "-" * (bar_length - filled)
    percent = ratio * 100.0
    sys.stdout.write(
        f"\r  -> {mode:<7} [{bar}] {current}/{total} ({percent:5.1f}%) | czas: {elapsed_s:6.2f} s"
    )
    sys.stdout.flush()


def generate_random_scramble(length=20):
    faces = ['U', 'D', 'L', 'R', 'F', 'B']
    modifiers = ['', "'", '2']
    scramble = []
    last_face = None

    for _ in range(length):
        available_faces = [f for f in faces if f != last_face]
        face = random.choice(available_faces)
        mod = random.choice(modifiers)
        scramble.append(f"{face}{mod}")
        last_face = face

    return " ".join(scramble)


def save_scrambles_to_file(count, filename=SCRAMBLES_FILE, length=20):
    scrambles = []
    seen_states = set()
    
    while len(scrambles) < count:
        scramble = generate_random_scramble(length)
        
        # Weryfikacja stanu kostki za pomocą tymczasowego obiektu
        temp_cube = BitCube()
        for move in parse_moves(scramble):
            temp_cube.apply_move(move)
            
        # Zapisujemy fizyczny stan kostki, a nie tylko ciąg znaków (string)
        state_key = (temp_cube.edges, temp_cube.corners)
        
        if state_key not in seen_states:
            seen_states.add(state_key)
            scrambles.append(scramble)
            
    with open(filename, "w", encoding="utf-8") as file:
        for scrmbl in scrambles:
            file.write(scrmbl + "\n")
            
    return scrambles


def load_scrambles_from_file(filename=SCRAMBLES_FILE):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def parse_moves(move_str):
    return [m.strip() for m in move_str.split() if m.strip()]


def draw_cube_2d(cube, ax, title="Kostka 2D"):
    grid = cube.to_2d_grid()
    ax.clear()
    ax.set_title(title)
    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(-0.5, 8.5)
    ax.set_aspect('equal')
    ax.axis('off')

    for r in range(9):
        for c in range(12):
            val = grid[r][c]
            if val:
                color = FACE_COLORS.get(val, '#333333')
                y_pos = 8 - r
                rect = plt.Rectangle(
                    (c - 0.5, y_pos - 0.5), 1, 1,
                    facecolor=color, edgecolor='black', linewidth=1.5
                )
                ax.add_patch(rect)


def is_cube_solved(cube):
    solved_cube = BitCube()
    return cube.edges == solved_cube.edges and cube.corners == solved_cube.corners


def _execute_solver(mode, cube, is_debug=False):
    total_moves = 0
    if mode == "LBL":
        for step_id in range(1, 9):
            if is_debug:
                print(f"\n      -> [Krok {step_id}] Uruchamiam... ", end="", flush=True)
            solution, name = lbl_bit.solve_step(cube, step_id)
            step_moves = len(solution.split()) if solution else 0
            total_moves += step_moves
            if is_debug:
                print(f"ZAKOŃCZONO ({name}) | ruchy: {step_moves} | wykonano: {solution or 'brak'}", end="", flush=True)
    elif mode == "CFOP":
        for step_id in range(1, 5):
            if is_debug:
                print(f"\n      -> [Krok {step_id}] Uruchamiam... ", end="", flush=True)
            solution, name = cfop_bit.solve_step(cube, step_id)
            step_moves = len(solution.split()) if solution else 0
            total_moves += step_moves
            if is_debug:
                print(f"ZAKOŃCZONO ({name}) | ruchy: {step_moves} | wykonano: {solution or 'brak'}", end="", flush=True)
    elif mode == "BLIND":
        if is_debug:
            print(f"\n      -> [Całość] Uruchamiam... ", end="", flush=True)
        log = []
        solver_blind = blind_bit.OptimizedBlindSolver()
        solver_blind.solve(cube, log)
        total_moves = len(log)
        if is_debug:
            print(f"ZAKOŃCZONO | ruchy: {total_moves} | wykonano: {' '.join(log) or 'brak'}", end="", flush=True)
    elif mode == "OPTIMAL":
        if is_debug:
            print(f"\n      -> [Całość] Uruchamiam... ", end="", flush=True)
        log = []
        solver_opt = optimal_bit.BidirectionalOptimalSolver()
        solver_opt.solve(cube, log)
        total_moves = len(log)
        if is_debug:
            print(f"ZAKOŃCZONO | ruchy: {total_moves} | wykonano: {' '.join(log) or 'brak'}", end="", flush=True)
    else:
        raise ValueError(f"Nieznany solver: {mode}")
    return total_moves


def _get_mode_trials(mode, total_trials):
    if mode == "OPTIMAL":
        return max(1, total_trials // 10)
    return total_trials


# =========================================================================
# WORKERY DLA MULTIPROCESSINGU (Muszą być na poziomie modułu)
# =========================================================================
def _worker_pass3_cpu(args):
    scramble, mode = args
    cube = BitCube()
    for m in parse_moves(scramble):
        cube.apply_move(m)

    cpu_t0 = time.process_time()
    wall_t0 = time.perf_counter()
    try:
        moves_count = _execute_solver(mode, cube, is_debug=False)
        wall_dt = time.perf_counter() - wall_t0
        cpu_dt = time.process_time() - cpu_t0
        solved = is_cube_solved(cube)
    except Exception as err:
        moves_count = 0
        wall_dt = 0.0
        cpu_dt = 0.0
        solved = False

    elapsed_ms = wall_dt * 1000.0
    cpu_usage = min(100.0, (cpu_dt / wall_dt) * 100.0) if wall_dt > 0 else 0.0

    return {
        "solved": solved,
        "time_ms": elapsed_ms,
        "moves": moves_count,
        "cpu_usage": cpu_usage
    }


def _worker_pass4_memory(args):
    scramble, mode = args
    cube = BitCube()
    for m in parse_moves(scramble):
        cube.apply_move(m)

    tracemalloc.start()
    tracemalloc.reset_peak()
    try:
        _execute_solver(mode, cube, is_debug=False)
    except Exception:
        pass
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "memory_mb": peak_bytes / (1024.0 * 1024.0)
    }


# =========================================================================
# PRZEBIEGI 1 i 2: SINGLE-CORE
# =========================================================================
def run_pass1_time_moves_cpu(scrambles, modes):
    total_trials = len(scrambles)
    pass1_results = {m: [] for m in modes}

    print("\n[PRZEBIEG 1/4] SC Pomiar CZASU, RUCHÓW i CPU (Pojedynczy wątek)...")
    for m in modes:
        m_trials = _get_mode_trials(m, total_trials)
        mode_scrambles = scrambles[:m_trials]
        mode_start = time.perf_counter()

        print_progress_bar(m, 0, m_trials, 0.0)

        for idx, scramble in enumerate(mode_scrambles, 1):
            cube = BitCube()
            for move in parse_moves(scramble):
                cube.apply_move(move)

            cpu_t0 = time.process_time()
            wall_t0 = time.perf_counter()
            try:
                moves_count = _execute_solver(m, cube)
                wall_dt = time.perf_counter() - wall_t0
                cpu_dt = time.process_time() - cpu_t0
                solved = is_cube_solved(cube)
            except (RuntimeError, ValueError) as err:
                moves_count = 0
                wall_dt = 0.0
                cpu_dt = 0.0
                solved = False
                sys.stdout.write(f"\n  [BŁĄD P1] Scramble #{idx} ({m}): {err}\n")

            elapsed_ms = wall_dt * 1000.0
            cpu_usage = min(100.0, (cpu_dt / wall_dt) * 100.0) if wall_dt > 0 else 0.0

            pass1_results[m].append({
                "solved": solved,
                "time_ms": elapsed_ms,
                "moves": moves_count,
                "cpu_usage": cpu_usage
            })

            print_progress_bar(m, idx, m_trials, time.perf_counter() - mode_start)

        sys.stdout.write("\n")
        sys.stdout.flush()

    return pass1_results


def run_pass2_memory(scrambles, modes):
    total_trials = len(scrambles)
    pass2_results = {m: [] for m in modes}

    print("\n[PRZEBIEG 2/4] SC Pomiar PAMIĘCI RAM (Pojedynczy wątek)...")
    tracemalloc.start()
    try:
        for m in modes:
            m_trials = _get_mode_trials(m, total_trials)
            mode_scrambles = scrambles[:m_trials]
            mode_start = time.perf_counter()

            print_progress_bar(m, 0, m_trials, 0.0)

            for idx, scramble in enumerate(mode_scrambles, 1):
                cube = BitCube()
                for move in parse_moves(scramble):
                    cube.apply_move(move)

                tracemalloc.reset_peak()
                try:
                    _execute_solver(m, cube)
                except (RuntimeError, ValueError):
                    pass
                _, peak_bytes = tracemalloc.get_traced_memory()

                pass2_results[m].append({
                    "memory_mb": peak_bytes / (1024.0 * 1024.0)
                })

                print_progress_bar(m, idx, m_trials, time.perf_counter() - mode_start)

            sys.stdout.write("\n")
            sys.stdout.flush()
    finally:
        tracemalloc.stop()

    return pass2_results


# =========================================================================
# PRZEBIEGI 3 i 4: MULTI-CORE (MULTIPROCESSING)
# =========================================================================
def run_pass3_multiprocess_cpu(scrambles, modes):
    total_trials = len(scrambles)
    pass3_results = {m: [] for m in modes}
    workers = max(1, os.cpu_count() - 1)

    print(f"\n[PRZEBIEG 3/4] MC Pomiar CZASU, RUCHÓW i CPU ({workers} workery)...")
    with ProcessPoolExecutor(max_workers=workers) as executor:
        for m in modes:
            m_trials = _get_mode_trials(m, total_trials)
            mode_scrambles = scrambles[:m_trials]
            mode_start = time.perf_counter()
            
            print_progress_bar(m, 0, m_trials, 0.0)
            
            args = [(s, m) for s in mode_scrambles]
            for idx, result in enumerate(executor.map(_worker_pass3_cpu, args), 1):
                pass3_results[m].append(result)
                print_progress_bar(m, idx, m_trials, time.perf_counter() - mode_start)
            
            sys.stdout.write("\n")
            sys.stdout.flush()
            
    return pass3_results


def run_pass4_multiprocess_memory(scrambles, modes):
    total_trials = len(scrambles)
    pass4_results = {m: [] for m in modes}
    workers = max(1, os.cpu_count() - 1)

    print(f"\n[PRZEBIEG 4/4] MC Pomiar PAMIĘCI RAM ({workers} workery)...")
    with ProcessPoolExecutor(max_workers=workers) as executor:
        for m in modes:
            m_trials = _get_mode_trials(m, total_trials)
            mode_scrambles = scrambles[:m_trials]
            mode_start = time.perf_counter()
            
            print_progress_bar(m, 0, m_trials, 0.0)
            
            args = [(s, m) for s in mode_scrambles]
            for idx, result in enumerate(executor.map(_worker_pass4_memory, args), 1):
                pass4_results[m].append(result)
                print_progress_bar(m, idx, m_trials, time.perf_counter() - mode_start)
            
            sys.stdout.write("\n")
            sys.stdout.flush()
            
    return pass4_results


def run_comparison_test(trials, modes):
    start_time_dt = datetime.now()
    start_time_perf = time.perf_counter()
    print(f"\n[{start_time_dt.strftime('%Y-%m-%d %H:%M:%S')}] ROZPOCZĘTO TESTOWANIE.")
    
    print(f"Generowanie {trials} losowych scrambli do pliku '{SCRAMBLES_FILE}'...")
    save_scrambles_to_file(trials, SCRAMBLES_FILE)
    scrambles = load_scrambles_from_file(SCRAMBLES_FILE)

    all_possible_modes = ("LBL", "BLIND", "CFOP", "OPTIMAL")
    csv_prefix = {"LBL": "LBL", "BLIND": "Blind", "CFOP": "CFOP", "OPTIMAL": "Optimal"}

    # 4 Niezależne Przebiegi
    pass1 = run_pass1_time_moves_cpu(scrambles, modes)
    pass2 = run_pass2_memory(scrambles, modes)
    pass3 = run_pass3_multiprocess_cpu(scrambles, modes)
    pass4 = run_pass4_multiprocess_memory(scrambles, modes)

    stats = {
        m: {
            "trials": _get_mode_trials(m, trials),
            "successes_sc": 0, "successes_mc": 0,
            "time_ms_sc": [], "moves_sc": [], "cpu_sc": [], "mem_sc": [],
            "time_ms_mc": [], "moves_mc": [], "cpu_mc": [], "mem_mc": []
        }
        for m in modes
    }
    csv_rows = []

    for i in range(trials):
        row_data = {"Index": i + 1}
        for m in all_possible_modes:
            prefix = csv_prefix[m]
            if m in modes and i < len(pass1[m]):
                p1, p2, p3, p4 = pass1[m][i], pass2[m][i], pass3[m][i], pass4[m][i]

                if p1["solved"]:
                    stats[m]["successes_sc"] += 1
                    stats[m]["time_ms_sc"].append(p1["time_ms"])
                    stats[m]["moves_sc"].append(p1["moves"])
                    stats[m]["cpu_sc"].append(p1["cpu_usage"])
                    stats[m]["mem_sc"].append(p2["memory_mb"])
                
                if p3["solved"]:
                    stats[m]["successes_mc"] += 1
                    stats[m]["time_ms_mc"].append(p3["time_ms"])
                    stats[m]["moves_mc"].append(p3["moves"])
                    stats[m]["cpu_mc"].append(p3["cpu_usage"])
                    stats[m]["mem_mc"].append(p4["memory_mb"])

                # SC Columns
                row_data[f"{prefix} SC Time (ms)"] = f"{p1['time_ms']:.4f}"
                row_data[f"{prefix} SC Moves"] = p1["moves"]
                row_data[f"{prefix} SC CPU Usage"] = f"{p1['cpu_usage']:.2f}"
                row_data[f"{prefix} SC Mem (MB)"] = f"{p2['memory_mb']:.6f}"
                
                # MC Columns
                row_data[f"{prefix} MC Time (ms)"] = f"{p3['time_ms']:.4f}"
                row_data[f"{prefix} MC Moves"] = p3["moves"]
                row_data[f"{prefix} MC CPU Usage"] = f"{p3['cpu_usage']:.2f}"
                row_data[f"{prefix} MC Mem (MB)"] = f"{p4['memory_mb']:.6f}"
            else:
                row_data[f"{prefix} SC Time (ms)"] = ""
                row_data[f"{prefix} SC Moves"] = ""
                row_data[f"{prefix} SC CPU Usage"] = ""
                row_data[f"{prefix} SC Mem (MB)"] = ""
                row_data[f"{prefix} MC Time (ms)"] = ""
                row_data[f"{prefix} MC Moves"] = ""
                row_data[f"{prefix} MC CPU Usage"] = ""
                row_data[f"{prefix} MC Mem (MB)"] = ""

        csv_rows.append(row_data)

    with open(CSV_OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_HEADER)
        writer.writeheader()
        writer.writerows(csv_rows)

    print(f"\nZapisano pełne dane ({len(csv_rows)} wierszy) w pliku '{CSV_OUTPUT_FILE}'.")

    print("\n" + "=" * 90)
    print(f"                PODSUMOWANIE BENCHMARKU ({trials} SCRAMBLI, OPTIMAL: 10%)")
    print("=" * 90)
    print(
        f"{'Algorytm':<10} | {'Tryb':<5} | {'Sukcesy':<10} | {'Śr. Czas [ms]':<13} | "
        f"{'Śr. Ruchy':<10} | {'Śr. CPU [%]':<11} | {'Śr. Pamięć [MB]':<15}"
    )
    print("-" * 90)
    for m in modes:
        s = stats[m]
        
        # Single-Core obliczenia
        cnt_sc = len(s["moves_sc"])
        avg_time_sc = sum(s["time_ms_sc"]) / cnt_sc if cnt_sc else 0.0
        avg_moves_sc = sum(s["moves_sc"]) / cnt_sc if cnt_sc else 0.0
        avg_cpu_sc = sum(s["cpu_sc"]) / cnt_sc if cnt_sc else 0.0
        avg_mem_sc = sum(s["mem_sc"]) / cnt_sc if cnt_sc else 0.0
        succ_str_sc = f"{s['successes_sc']}/{s['trials']}"
        
        # Multi-Core obliczenia
        cnt_mc = len(s["moves_mc"])
        avg_time_mc = sum(s["time_ms_mc"]) / cnt_mc if cnt_mc else 0.0
        avg_moves_mc = sum(s["moves_mc"]) / cnt_mc if cnt_mc else 0.0
        avg_cpu_mc = sum(s["cpu_mc"]) / cnt_mc if cnt_mc else 0.0
        avg_mem_mc = sum(s["mem_mc"]) / cnt_mc if cnt_mc else 0.0
        succ_str_mc = f"{s['successes_mc']}/{s['trials']}"

        print(
            f"{m:<10} | {'SC':<5} | {succ_str_sc:<10} | {avg_time_sc:<13.4f} | "
            f"{avg_moves_sc:<10.2f} | {avg_cpu_sc:<11.2f} | {avg_mem_sc:<15.6f}"
        )
        print(
            f"{m:<10} | {'MC':<5} | {succ_str_mc:<10} | {avg_time_mc:<13.4f} | "
            f"{avg_moves_mc:<10.2f} | {avg_cpu_mc:<11.2f} | {avg_mem_mc:<15.6f}"
        )
    print("=" * 90)

    end_time_dt = datetime.now()
    total_time_s = time.perf_counter() - start_time_perf
    mins, secs = divmod(total_time_s, 60)
    
    print(f"[{end_time_dt.strftime('%Y-%m-%d %H:%M:%S')}] ZAKOŃCZONO TESTOWANIE.")
    print(f"CAŁKOWITY CZAS TRWANIA (4 PRZEBIEGI): {int(mins)} minut {secs:.2f} sekund")
    print("=" * 90)


def run_debug_test(trials, modes):
    """
    Tryb DEBUG: Generuje po jednym scramblu naraz. Najpierw wypisuje
    w terminalu wygenerowany układ, a potem wywołuje solvery. 
    W przypadku nieskończonej pętli, terminal jednoznacznie wskaże ostatni scramble.
    """
    start_time_dt = datetime.now()
    print(f"\n[{start_time_dt.strftime('%Y-%m-%d %H:%M:%S')}] ROZPOCZĘTO DEBUGOWANIE ({trials} SCRAMBLI).")
    print(f"Wybrane algorytmy: {', '.join(modes)}")

    for i in range(1, trials + 1):
        scramble = generate_random_scramble(20)
        print(f"\n--- [Ułożenie {i}/{trials}] ---")
        print(f"Oto Scramble: {scramble}")
        
        for m in modes:
            print(f"  -> Uruchamiam {m:<7} ... ", end="", flush=True)
            
            cube = BitCube()
            for move in parse_moves(scramble):
                cube.apply_move(move)

            t0 = time.perf_counter()
            try:
                moves_count = _execute_solver(m, cube, is_debug=True)
                dt_ms = (time.perf_counter() - t0) * 1000.0
                solved_str = "SUKCES" if is_cube_solved(cube) else "NIEUŁOŻONA"
                print(f"\n    === ZAKOŃCZONO ALGORYTM [{solved_str}] (czas całkowity: {dt_ms:.2f} ms, ruchy: {moves_count}) ===")
            except Exception as e:
                print(f"\n    === BŁĄD ZGŁOSZONY PRZEZ SOLVER: {e} ===")

    print("\n=======================================================")
    print("[DEBUG] PROCEDURA DEBUGOWANIA ZOSTAŁA ZAKOŃCZONA.")
    print("=======================================================")


def ask_modes():
    print("\nKtóre algorytmy chcesz uwzględnić?")
    print(" 1 - LBL")
    print(" 2 - CFOP")
    print(" 3 - BLIND")
    print(" 4 - OPTIMAL")
    print(" 5 - ALL (wszystkie)")
    print("Możesz wybrać kilka rozdzielając je spacją, np. '1 2'.")
    choice = input("Wybór [5]: ").strip()
    
    if not choice:
        choice = "5"
        
    modes = []
    if "5" in choice.split() or choice.upper() == "ALL":
        return ["LBL", "CFOP", "BLIND", "OPTIMAL"]
        
    mapping = {"1": "LBL", "2": "CFOP", "3": "BLIND", "4": "OPTIMAL"}
    for c in choice.split():
        if c in mapping and mapping[c] not in modes:
            modes.append(mapping[c])
            
    if not modes:
        print("Nie wybrano prawidłowych algorytmów. Domyślnie ładuję ALL.")
        return ["LBL", "CFOP", "BLIND", "OPTIMAL"]
        
    return modes


def ask_test_count():
    try:
        count = int(input("Ile scrambli wygenerować i ułożyć? [100]: ").strip() or "100")
    except (ValueError, EOFError, KeyboardInterrupt):
        print("Nieprawidłowa liczba scrambli.")
        return None
    if count < 1:
        print("Liczba scrambli musi być większa od zera.")
        return None
    return count


def parse_command(cmd):
    cmd = cmd.strip()
    if not cmd:
        return False, None, ""

    cmd_upper = cmd.upper()
    if cmd_upper in {"Q", "QUIT", "EXIT"}:
        return False, "QUIT", ""
    if cmd_upper == "TEST":
        return False, "TEST", ""
    if cmd_upper == "DEBUG":
        return False, "DEBUG", ""
    if cmd_upper in {"V", "VIS", "TOGGLE"}:
        return False, "TOGGLE_VIS", ""
    if cmd_upper in {"ON", "V ON", "VIS ON"}:
        return False, "VIS_ON", ""
    if cmd_upper in {"OFF", "V OFF", "VIS OFF"}:
        return False, "VIS_OFF", ""

    do_scramble = False
    if cmd_upper == "S":
        return True, None, ""
    if cmd_upper.startswith("S "):
        do_scramble = True
        cmd_upper = cmd_upper[2:].strip()

    if cmd_upper in {"OPT", "OPTIMAL"}:
        return do_scramble, "OPTIMAL", ""
    if cmd_upper in {"LBL", "CFOP", "BLIND"}:
        return do_scramble, cmd_upper, ""

    return False, None, cmd


def main():
    cube = BitCube()
    vis_enabled = False
    last_title = "Kostka ułożona"
    fig, ax = None, None

    plt.ion()

    def set_visualizer_state(new_state):
        nonlocal vis_enabled, fig, ax
        vis_enabled = new_state
        if vis_enabled:
            print("[WIZUALIZATOR] Przełączono: OFF -> ON (WŁĄCZONY)")
            update_visualizer(last_title)
        else:
            print("[WIZUALIZATOR] Przełączono: ON -> OFF (WYŁĄCZONY)")
            if fig is not None and plt.fignum_exists(fig.number):
                plt.close(fig)
            fig, ax = None, None

    def update_visualizer(title):
        nonlocal fig, ax, last_title
        last_title = title
        if not vis_enabled:
            return
        if fig is None or not plt.fignum_exists(fig.number):
            plt.ion()
            fig, ax = plt.subplots(figsize=(10, 6))
            plt.show(block=False)
        draw_cube_2d(cube, ax, last_title)
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.05)

    print("=" * 80)
    print("              SYMULATOR I BENCHMARK KOSTKI RUBIKA (BITBOARD)")
    print("=" * 80)
    print("Komendy: S, LBL, CFOP, BLIND, OPT (Double Search), V/ON/OFF, TEST, DEBUG, Q")
    print(f"Aktualny stan wizualizatora: {'ON' if vis_enabled else 'OFF'}")

    while True:
        try:
            command = input("\n> ")
        except (EOFError, KeyboardInterrupt):
            break

        do_scramble, mode, error = parse_command(command)

        if mode == "QUIT":
            break

        if mode == "TOGGLE_VIS":
            if vis_enabled and (fig is None or not plt.fignum_exists(fig.number)):
                vis_enabled = False
            set_visualizer_state(not vis_enabled)
            continue

        if mode == "VIS_ON":
            set_visualizer_state(True)
            continue

        if mode == "VIS_OFF":
            set_visualizer_state(False)
            continue

        if mode in {"TEST", "DEBUG"}:
            selected_modes = ask_modes()
            test_count = ask_test_count()
            
            if test_count is not None and selected_modes:
                if mode == "TEST":
                    run_comparison_test(test_count, selected_modes)
                elif mode == "DEBUG":
                    run_debug_test(test_count, selected_modes)
            continue

        if error:
            print(f"Nieznana komenda: {error}. Dostępne: S, LBL, CFOP, BLIND, OPT, V, ON, OFF, TEST, DEBUG, Q")
            continue

        if do_scramble:
            scramble = generate_random_scramble(20)
            cube = BitCube()
            for move in parse_moves(scramble):
                cube.apply_move(move)
            print(f"Scramble: {scramble}")
            if mode is None:
                update_visualizer("Po scramblu")
                continue

        if mode == "BLIND":
            blind_log = []
            try:
                solver_blind = blind_bit.OptimizedBlindSolver()
                solver_blind.solve(cube, blind_log)
                print(f"[BLIND] Wykonano ruchów: {len(blind_log)}")
            except RuntimeError as err:
                print(f"[BLIND] BŁĄD: {err}")
            update_visualizer("BLIND: aktualny stan")
            continue

        if mode == "OPTIMAL":
            opt_log = []
            try:
                solver_opt = optimal_bit.BidirectionalOptimalSolver()
                solver_opt.solve(cube, opt_log)
                print(f"[OPTIMAL - DOUBLE SEARCH] Ruchy ({len(opt_log)}): {' '.join(opt_log)}")
            except RuntimeError as err:
                print(f"[OPTIMAL] BŁĄD: {err}")
            update_visualizer("OPTIMAL: aktualny stan")
            continue

        if mode in {"LBL", "CFOP"}:
            solver = cfop_bit if mode == "CFOP" else lbl_bit
            steps = list(range(1, 5)) if mode == "CFOP" else list(range(1, 9))
            total_moves = 0
            for step_id in steps:
                solution, name = solver.solve_step(cube, step_id)
                step_moves = len(solution.split()) if solution else 0
                total_moves += step_moves
                print(f"{name}: {solution or 'brak ruchów'}")
            print(f"[{mode}] Łącznie ruchów: {total_moves}")
            update_visualizer(f"{mode}: aktualny stan")
            continue

    if fig is not None and plt.fignum_exists(fig.number):
        plt.close(fig)


if __name__ == "__main__":
    # Niezbędne zabezpieczenie pętli głównej dla bezbłędnego startowania multiprocessing na systemach Windows
    main()