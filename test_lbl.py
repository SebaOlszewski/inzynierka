# test_lbl.py
import time
from cube_bitboard import BitCube
import lbl_bit
from main import parse_moves, generate_random_scramble


def run_test_lbl_100(iterations=100):
    # Wzorcowy stan bitowy ułożonej kostki
    solved_cube = BitCube()
    TARGET_EDGES = solved_cube.edges
    TARGET_CORNERS = solved_cube.corners

    print("=" * 85)
    print(f"  TEST LBL: {iterations}x (Scramble -> Ułożenie 1..8 -> Bit Check: edges & corners)")
    print("=" * 85)

    success_count = 0
    failed_cases = []
    moves_history = []
    start_time = time.time()

    for i in range(1, iterations + 1):
        cube = BitCube()
        scramble = generate_random_scramble(20)

        # 1. Scramble
        for m in parse_moves(scramble):
            cube.apply_move(m)

        # 2. Ułożenie metodą LBL (kroki 1..8)
        total_moves = 0
        step_details = []
        for step_id in [1, 2, 3, 4, 5, 6, 7, 8]:
            sol, _ = lbl_bit.solve_step(cube, step_id)
            cnt = len(sol.split()) if sol else 0
            total_moves += cnt
            step_details.append(cnt)

        # 3. Weryfikacja bitowa stanu kostki
        is_solved = (cube.edges == TARGET_EDGES and cube.corners == TARGET_CORNERS)

        if is_solved:
            success_count += 1
            moves_history.append(total_moves)
            print(f"[{i:03d}/{iterations}] SUKCES | Ruchy: {total_moves:3d} (K1:{step_details[0]:2d} K2:{step_details[1]:2d} K3:{step_details[2]:2d} K4:{step_details[3]:2d} K5:{step_details[4]:2d} K6:{step_details[5]:2d} K7:{step_details[6]:2d} K8:{step_details[7]:2d})")
        else:
            failed_cases.append((i, scramble, cube.edges, cube.corners))
            print(f"[{i:03d}/{iterations}] BLAD   | edges={cube.edges}, corners={cube.corners}")

    elapsed = time.time() - start_time
    avg_moves = sum(moves_history) / len(moves_history) if moves_history else 0

    print("\n" + "=" * 85)
    print("                           PODSUMOWANIE TESTU                       ")
    print("=" * 85)
    print(f"Liczba prob:                 {iterations}")
    print(f"Sukcesy:                     {success_count} / {iterations} ({success_count/iterations*100:.1f}%)")
    print(f"Srednia liczba ruchow:       {avg_moves:.2f}")
    if moves_history:
        print(f"Min / Max liczba ruchow:     {min(moves_history)} / {max(moves_history)}")
    print(f"Laczny czas testu:           {elapsed:.2f} s")

    if failed_cases:
        print("\nNieudane przypadki:")
        for idx, scr, e, c in failed_cases:
            print(f"- Proba #{idx}\n  Scramble: {scr}\n  Edges: {e} | Corners: {c}\n")
    else:
        print("\n100/100 testow zakonczonych pelnym sukcesem!")
    print("=" * 85)

    input("\nNacisnij ENTER, aby zakonczyc...")


if __name__ == "__main__":
    run_test_lbl_100(100)