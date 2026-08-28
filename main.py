# main.py
import random
import matplotlib.pyplot as plt
from cube_bitboard import BitCube
import lbl_bit

FACE_COLORS = {
    'W': '#FFFFFF',
    'Y': '#FFD500',
    'G': '#009B48',
    'B': '#0046AD',
    'O': '#FF5800',
    'R': '#B71234'
}

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
            if val is not None:
                color = FACE_COLORS.get(val, '#333333')
                # Inwersja osi Y dla widoku siatki (0 na górze)
                y_pos = 8 - r
                rect = plt.Rectangle((c - 0.5, y_pos - 0.5), 1, 1,
                                     facecolor=color, edgecolor='black', linewidth=1.5)
                ax.add_patch(rect)


def parse_step_sequence(cmd):
    """
    Parsuje sekwencje wpisane przez uzytkownika, np:
    - '1', '2', ..., '8'
    - '11', '12', '13', '14'
    - '12345678' -> [1, 2, 3, 4, 5, 6, 7, 8]
    - 's12345678' -> scramble + kroki 1..8
    """
    cmd = cmd.strip().lower()
    do_scramble = False
    if cmd.startswith('s'):
        do_scramble = True
        cmd = cmd[1:].strip()

    if not cmd:
        return do_scramble, []

    # Sprawdzenie czy to pojedynczy krok (np. 11, 12, 13, 14 lub 1..8)
    if cmd in [str(k) for k in lbl_bit.STEPS.keys()]:
        return do_scramble, [int(cmd)]

    # Sekwencja pojedynczych cyfr (np. '123', '12345678')
    steps = []
    for ch in cmd:
        if ch.isdigit():
            val = int(ch)
            if val in lbl_bit.STEPS:
                steps.append(val)

    return do_scramble, steps


def main():
    cube = BitCube()
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 6))
    draw_cube_2d(cube, ax, "Ułożona Kostka")
    plt.draw()
    plt.pause(0.1)

    print("=" * 65)
    print("  SYMULATOR KOSTKI RUBIKA (LBL: Kroki 1..8)")
    print("=" * 65)
    print("Komendy:")
    print("  s                  - Losowy Scramble")
    print("  1, 2, 3, 4, 5, 6, 7, 8 - Wykonanie wybranego kroku LBL")
    print("  11, 12, 13, 14     - Podkroki Daisy")
    print("  12345678           - Ciąg kroków LBL")
    print("  s12345678          - Scramble + pełne ułożenie LBL (1..8)")
    print("  R U R' U'...       - Własna sekwencja ruchów")
    print("  q                  - Wyjście")
    print("=" * 65)

    while True:
        try:
            cmd = input("\nWprowadz komende/sekwencje (np. s, 11, 12, s12345678): ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if not cmd:
            continue
        if cmd.lower() in ['q', 'quit', 'exit']:
            break

        do_scramble, steps = parse_step_sequence(cmd)

        if do_scramble:
            scr = generate_random_scramble(20)
            print(f"\n[RANDOM SCRAMBLE]: {scr}")
            for m in parse_moves(scr):
                cube.apply_move(m)
            draw_cube_2d(cube, ax, f"Scramble: {scr}")
            plt.draw()
            plt.pause(0.01)

        if steps:
            for step_id in steps:
                solution, name = lbl_bit.solve_step(cube, step_id)
                move_count = len(solution.split()) if solution else 0
                print(f"\n[{name}]")
                print(f"Ruchy ({move_count}): {solution if solution else '(brak - stan juz poprawny)'}")
                
                draw_cube_2d(cube, ax, f"{name} ({move_count} ruchow)")
                plt.draw()
                plt.pause(0.01)

        elif not do_scramble:
            # Własna sekwencja ruchów (np. R U R' U')
            moves = parse_moves(cmd)
            valid = True
            for m in moves:
                try:
                    cube.apply_move(m)
                except Exception as e:
                    print(f"Niepoprawny ruch: {m} ({e})")
                    valid = False
                    break

            if valid:
                draw_cube_2d(cube, ax, f"Wykonano ruchy: {cmd}")
                plt.draw()
                plt.pause(0.01)

    plt.close()


if __name__ == "__main__":
    main()