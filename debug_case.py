import sys
import main
from cube_bitboard import BitCube
import cfop_bit
import f2l_bit
import matplotlib.pyplot as plt

def debug_from_file(scramble_index):
    # Wczytanie konkretnego scrambla z pliku tekstowego
    try:
        with open("scrambles.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            scramble = lines[scramble_index - 1].strip()
    except Exception as e:
        print(f"Błąd odczytu pliku: {e}")
        return

    print(f"Odtwarzam Scramble #{scramble_index}: {scramble}")
    
    cube = BitCube()
    for m in scramble.split():
        cube.apply_move(m)

    log = []
    
    print("\n-> Układam krzyż (Krok 1)...")
    try:
        cfop_bit.solve_cross(cube, log)
        print(f"   Zakończono. Wykonano: {' '.join(log)}")
    except Exception as e:
        print(f"   [!] Błąd krzyża: {e}")
        return

    log.clear()

    print("\n-> Układam F2L (Krok 2) slot po slocie...")
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 6))

    for slot_id in range(4):
        print(f"   -> Próbuję ułożyć slot {slot_id}...")
        try:
            f2l_bit.solve_f2l_pair(cube, slot_id, log)
            main.draw_cube_2d(cube, ax, f"Stan po slocie {slot_id}")
            fig.canvas.draw()
            fig.canvas.flush_events()
            plt.pause(1.5)
        except Exception as e:
            print(f"\n   [!] BŁĄD: {e}")
            main.draw_cube_2d(cube, ax, f"BŁĄD F2L - poddał się na slocie {slot_id}")
            plt.show(block=True)
            return

    print("\nKoniec debugowania. F2L ułożyło się poprawnie!")
    plt.show(block=True)

if __name__ == "__main__":
    # Ustawiamy index 60 - pierwszy błąd z Twojego terminala
    debug_from_file(60)