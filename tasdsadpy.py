import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('ggplot')

# Create 2x2 subplot grid
fig, axs = plt.subplots(2, 2, figsize=(16, 12))

width = 0.35

# --- 1. RAM DATA (Top-Left) ---
labels_ram = ['LBL', 'CFOP', 'BLIND']
ram_inz = [7300, 7300, 7300]
ram_mag = [5.64, 3.21, 0.65]
x_ram = np.arange(len(labels_ram))

axs[0, 0].bar(x_ram - width/2, ram_inz, width, label='Inżynierka (Macierze)', color='#e74c3c')
axs[0, 0].bar(x_ram + width/2, ram_mag, width, label='Magisterka (BitCube)', color='#3498db')
axs[0, 0].set_ylabel('Zużycie RAM (MB)')
axs[0, 0].set_title('Szczytowe zużycie pamięci RAM (Skala Log)')
axs[0, 0].set_xticks(x_ram)
axs[0, 0].set_xticklabels(labels_ram)
axs[0, 0].set_yscale('log')
axs[0, 0].legend()

for i, v in enumerate(ram_inz):
    axs[0, 0].text(i - width/2, v, str(v), ha='center', va='bottom')
for i, v in enumerate(ram_mag):
    axs[0, 0].text(i + width/2, v, str(v), ha='center', va='bottom')

# --- 2. MOVES DATA (Top-Right) ---
labels_moves = ['LBL', 'CFOP', 'BLIND']
moves_inz = [320, 320, 780]
moves_mag = [190.0, 93.8, 395.5]
x_moves = np.arange(len(labels_moves))

axs[0, 1].bar(x_moves - width/2, moves_inz, width, label='Inżynierka', color='#f39c12')
axs[0, 1].bar(x_moves + width/2, moves_mag, width, label='Magisterka', color='#2ecc71')
axs[0, 1].set_ylabel('Średnia liczba ruchów')
axs[0, 1].set_title('Redukcja redundantnych ruchów')
axs[0, 1].set_xticks(x_moves)
axs[0, 1].set_xticklabels(labels_moves)
axs[0, 1].legend()

for i, v in enumerate(moves_inz):
    axs[0, 1].text(i - width/2, v, str(v), ha='center', va='bottom')
for i, v in enumerate(moves_mag):
    axs[0, 1].text(i + width/2, v, str(v), ha='center', va='bottom')

# --- 3. CPU DATA (Bottom-Left) ---
labels_cpu = ['Średnie bazowe', 'Szczytowe (Piki)']
cpu_inz = [10, 55] 
cpu_mag = [95, 99]
x_cpu = np.arange(len(labels_cpu))

axs[1, 0].bar(x_cpu - width/2, cpu_inz, width, label='Inżynierka', color='#e74c3c')
axs[1, 0].bar(x_cpu + width/2, cpu_mag, width, label='Magisterka', color='#3498db')
axs[1, 0].set_ylabel('Utylizacja CPU (%)')
axs[1, 0].set_title('Wykorzystanie mocy procesora (Utylizacja)')
axs[1, 0].set_xticks(x_cpu)
axs[1, 0].set_xticklabels(labels_cpu)
axs[1, 0].legend()
axs[1, 0].set_ylim(0, 110)

for i, v in enumerate(cpu_inz):
    axs[1, 0].text(i - width/2, v + 1, f'{v}%', ha='center', va='bottom')
for i, v in enumerate(cpu_mag):
    axs[1, 0].text(i + width/2, v + 1, f'{v}%', ha='center', va='bottom')

# --- 4. TIME DATA (Bottom-Right) ---
labels_time = ['LBL', 'CFOP', 'BLIND']
time_inz = [30, 30, 30] 
time_mag = [235.49, 163.49, 4.10]
x_time = np.arange(len(labels_time))

axs[1, 1].bar(x_time - width/2, time_inz, width, label='Inżynierka (~30ms)', color='#95a5a6')
axs[1, 1].bar(x_time + width/2, time_mag, width, label='Magisterka (Single Core)', color='#9b59b6')
axs[1, 1].set_ylabel('Czas układania (ms)')
axs[1, 1].set_title('Czas generowania ścieżki')
axs[1, 1].set_xticks(x_time)
axs[1, 1].set_xticklabels(labels_time)
axs[1, 1].legend()

for i, v in enumerate(time_inz):
    axs[1, 1].text(i - width/2, v + 2, str(v), ha='center', va='bottom')
for i, v in enumerate(time_mag):
    axs[1, 1].text(i + width/2, v + 2, f'{v:.1f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()