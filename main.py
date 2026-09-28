# main.py
import csv
import random
import sys
import time
import tracemalloc
import matplotlib.pyplot as plt
from cube_bitboard import BitCube
import lbl_bit
import cfop_bit
import blind_bit
import optimal_bit

SCRAMBLES_FILE = "scrambles.txt"
CSV_OUTPUT_FILE = "solve_data.csv"

CSV_HEADER = [
    "Index",
    "LBL Time (ms)", "LBL Moves", "LBL CPU Usage", "LBL Memory Used (MB)",
    "Blind Time (ms)", "Blind Moves", "Blind CPU Usage", "Blind Memory Used (MB)",
    "CFOP Time (ms)", "CFOP Moves", "CFOP CPU Usage", "CFOP Memory Used (MB)",
    "Optimal Time (ms)", "Optimal Moves", "Optimal CPU Usage", "Optimal Memory Used (MB)"
]

FACE_COLORS = {
    'W': '#FFFFFF',
    'Y': '#FFD500',
    'G': '#009B48',
    'B': '#0046AD',
    'O': '#FF5800',
    'R': '#B71234'
}


def print_progress_bar(mode, current, total, elapsed_s, bar_length=24):
    """Nadpisuje bieżący wiersz w terminalu paskiem postępu (np. 1/10 -> 2/10)."""
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
    scrambles = [generate_random_scramble(length) for _ in range(count)]
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


def _execute_solver(mode, cube):
    """Wykonuje pełne ułożenie kostki dla wybranego trybu i zwraca liczbę ruchów."""
    total_moves = 0
    if mode == "LBL":
        for step_id in range(1, 9):
            solution, _ = lbl_bit.solve_step(cube, step_id)
            total_moves += len(solution.split()) if solution else 0
    elif mode == "CFOP":
        for step_id in range(1, 5):
            solution, _ = cfop_bit.solve_step(cube, step_id)
            total_moves += len(solution.split()) if solution else 0
    elif mode == "BLIND":
        log = []
        solver_blind = blind_bit.OptimizedBlindSolver()
        solver_blind.solve(cube, log)
        total_moves = len(log)
    elif mode == "OPTIMAL":
        log = []
        solver_opt = optimal_bit.BidirectionalOptimalSolver()
        solver_opt.solve(cube, log)
        total_moves = len(log)
    else:
        raise ValueError(f"Nieznany solver: {mode}")
    return total_moves


def _get_mode_trials(mode, total_trials):
    """Dla OPTIMAL zwraca pierwsze 10% scrambli (minimum 1), dla pozostałych 100%."""
    if mode == "OPTIMAL":
        return max(1, total_trials // 10)
    return total_trials


def run_pass1_time_moves_cpu(scrambles, modes):
    """
    PRZEBIEG 1: Czysty pomiar czasu wykonania (ms), liczby ruchów oraz CPU Usage (%)
    z paskiem postępu aktualizowanym pomiędzy pomiarami.
    """
    total_trials = len(scrambles)
    pass1_results = {m: [] for m in modes}

    print("\n[PRZEBIEG 1/2] Pomiar CZASU, RUCHÓW i CPU...")
    for m in modes:
        m_trials = _get_mode_trials(m, total_trials)
        mode_scrambles = scrambles[:m_trials]
        mode_start = time.perf_counter()

        # Wyświetlenie stanu 0/N od razu w momencie startu danego algorytmu
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

            # Odświeżenie paska postępu już po zatrzymaniu stopera dla danej kostki
            print_progress_bar(m, idx, m_trials, time.perf_counter() - mode_start)

        sys.stdout.write("\n")
        sys.stdout.flush()

    return pass1_results


def run_pass2_memory(scrambles, modes):
    """
    PRZEBIEG 2: Wyłącznie pomiar szczytowego zużycia pamięci RAM (Memory Used MB)
    z paskiem postępu aktualizowanym poza pomiarem pamięci.
    """
    total_trials = len(scrambles)
    pass2_results = {m: [] for m in modes}

    print("\n[PRZEBIEG 2/2] Pomiar PAMIĘCI RAM...")
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

                # Aktualizacja paska po pobraniu peak_bytes (nie zaburza kolejnego reset_peak)
                print_progress_bar(m, idx, m_trials, time.perf_counter() - mode_start)

            sys.stdout.write("\n")
            sys.stdout.flush()
    finally:
        tracemalloc.stop()

    return pass2_results


def run_comparison_test(trials):
    print(f"\nGenerowanie {trials} losowych scrambli do pliku '{SCRAMBLES_FILE}'...")
    save_scrambles_to_file(trials, SCRAMBLES_FILE)
    scrambles = load_scrambles_from_file(SCRAMBLES_FILE)

    modes = ("LBL", "BLIND", "CFOP", "OPTIMAL")
    csv_prefix = {"LBL": "LBL", "BLIND": "Blind", "CFOP": "CFOP", "OPTIMAL": "Optimal"}

    pass1 = run_pass1_time_moves_cpu(scrambles, modes)
    pass2 = run_pass2_memory(scrambles, modes)

    stats = {
        m: {
            "trials": _get_mode_trials(m, trials),
            "successes": 0,
            "time_ms": [],
            "moves": [],
            "cpu": [],
            "mem": []
        }
        for m in modes
    }
    csv_rows = []

    for i in range(trials):
        row_data = {"Index": i + 1}
        for m in modes:
            prefix = csv_prefix[m]
            if i < len(pass1[m]):
                p1 = pass1[m][i]
                p2 = pass2[m][i]

                if p1["solved"]:
                    stats[m]["successes"] += 1
                    stats[m]["time_ms"].append(p1["time_ms"])
                    stats[m]["moves"].append(p1["moves"])
                    stats[m]["cpu"].append(p1["cpu_usage"])
                    stats[m]["mem"].append(p2["memory_mb"])

                row_data[f"{prefix} Time (ms)"] = f"{p1['time_ms']:.4f}"
                row_data[f"{prefix} Moves"] = p1["moves"]
                row_data[f"{prefix} CPU Usage"] = f"{p1['cpu_usage']:.2f}"
                row_data[f"{prefix} Memory Used (MB)"] = f"{p2['memory_mb']:.6f}"
            else:
                row_data[f"{prefix} Time (ms)"] = ""
                row_data[f"{prefix} Moves"] = ""
                row_data[f"{prefix} CPU Usage"] = ""
                row_data[f"{prefix} Memory Used (MB)"] = ""

        csv_rows.append(row_data)

    with open(CSV_OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_HEADER)
        writer.writeheader()
        writer.writerows(csv_rows)

    print(f"\nZapisano pełne dane ({len(csv_rows)} wierszy) w pliku '{CSV_OUTPUT_FILE}'.")

    print("\n" + "=" * 90)
    print(f"                 PODSUMOWANIE BENCHMARKU ({trials} SCRAMBLI, OPTIMAL: 10%)")
    print("=" * 90)
    print(
        f"{'Algorytm':<10} | {'Sukcesy':<12} | {'Śr. Czas [ms]':<14} | "
        f"{'Śr. Ruchy':<12} | {'Śr. CPU [%]':<12} | {'Śr. Pamięć [MB]':<15}"
    )
    print("-" * 90)
    for m in modes:
        s = stats[m]
        cnt = len(s["moves"])
        avg_time = sum(s["time_ms"]) / cnt if cnt else 0.0
        avg_moves = sum(s["moves"]) / cnt if cnt else 0.0
        avg_cpu = sum(s["cpu"]) / cnt if cnt else 0.0
        avg_mem = sum(s["mem"]) / cnt if cnt else 0.0
        succ_str = f"{s['successes']}/{s['trials']}"
        print(
            f"{m:<10} | {succ_str:<12} | {avg_time:<14.4f} | "
            f"{avg_moves:<12.2f} | {avg_cpu:<12.2f} | {avg_mem:<15.6f}"
        )
    print("=" * 90)


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
    print("               SYMULATOR I BENCHMARK KOSTKI RUBIKA (BITBOARD)")
    print("=" * 80)
    print("Komendy: S, LBL, CFOP, BLIND, OPT (Double Search), V/ON/OFF, TEST, Q")
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

        if mode == "TEST":
            test_count = ask_test_count()
            if test_count is not None:
                run_comparison_test(test_count)
            continue

        if error:
            print(f"Nieznana komenda: {error}. Dostępne: S, LBL, CFOP, BLIND, OPT, V, ON, OFF, TEST, Q")
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
    main()