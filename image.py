import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_search_tree_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # ==========================================
    # WYKRES 1: Klasyczne przeszukiwanie (LBL, itp.)
    # ==========================================
    ax1.set_title("Klasyczne przeszukiwanie\n(Jednokierunkowe)", fontsize=14, fontweight='bold', pad=20)
    
    # Główny wielki trójkąt
    poly1 = patches.Polygon([[0.5, 1], [0, 0], [1, 0]], closed=True, fill=True, color='#e0e0e0', edgecolor='black', linewidth=2)
    ax1.add_patch(poly1)
    
    # Podpisy stanów
    ax1.text(0.5, 1.02, "Stan początkowy\n(Pomieszany)", ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax1.text(0.5, -0.02, "Stan docelowy\n(Ułożony)", ha='center', va='top', fontsize=12, fontweight='bold')
    
    # Złożoność wewnątrz
    ax1.text(0.5, 0.4, "Przestrzeń stanów\n$\mathcal{O}(b^d)$", ha='center', va='center', fontsize=16)
    
    # Strzałka i podpis głębokości (prawa strona)
    ax1.annotate('', xy=(1.1, 0), xytext=(1.1, 1), arrowprops=dict(arrowstyle='<->', lw=2))
    ax1.text(1.15, 0.5, "Głębokość $d$", ha='left', va='center', fontsize=14)

    # ==========================================
    # WYKRES 2: Double Search (Dwukierunkowe)
    # ==========================================
    ax2.set_title("Algorytm Double Search\n(Dwukierunkowe)", fontsize=14, fontweight='bold', pad=20)
    
    # Zarys starego wielkiego trójkąta (żeby pokazać ile pamięci oszczędzamy)
    poly2_outline = patches.Polygon([[0.5, 1], [0, 0], [1, 0]], closed=True, fill=False, edgecolor='gray', linestyle='--', linewidth=1.5)
    ax2.add_patch(poly2_outline)
    
    # Górny trójkąt (szukanie w przód)
    poly2_top = patches.Polygon([[0.5, 1], [0.25, 0.5], [0.75, 0.5]], closed=True, fill=True, color='#a8d0e6', edgecolor='black', linewidth=2)
    ax2.add_patch(poly2_top)
    
    # Dolny trójkąt (szukanie wstecz)
    poly2_bot = patches.Polygon([[0.5, 0], [0.25, 0.5], [0.75, 0.5]], closed=True, fill=True, color='#f8e9a1', edgecolor='black', linewidth=2)
    ax2.add_patch(poly2_bot)
    
    # Podpisy stanów
    ax2.text(0.5, 1.02, "Stan początkowy\n(Pomieszany)", ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax2.text(0.5, -0.02, "Stan docelowy\n(Ułożony)", ha='center', va='top', fontsize=12, fontweight='bold')
    
    # Linia spotkania w połowie (Meet in the middle)
    ax2.plot([0.15, 0.85], [0.5, 0.5], color='red', linestyle='-', lw=2.5)
    ax2.text(0.85, 0.52, "Punkt spotkania\n(Meet-in-the-middle)", ha='center', va='bottom', color='red', fontsize=11, fontweight='bold')
    
    # Złożoność wewnątrz małych trójkątów
    ax2.text(0.5, 0.7, "$\mathcal{O}(b^{d/2})$", ha='center', va='center', fontsize=14)
    ax2.text(0.5, 0.3, "$\mathcal{O}(b^{d/2})$", ha='center', va='center', fontsize=14)
    
    # Strzałki i podpisy głębokości (prawa strona)
    ax2.annotate('', xy=(1.1, 0.5), xytext=(1.1, 1), arrowprops=dict(arrowstyle='<->', lw=2))
    ax2.text(1.15, 0.75, "Głębokość $d/2$", ha='left', va='center', fontsize=14)
    
    ax2.annotate('', xy=(1.1, 0), xytext=(1.1, 0.5), arrowprops=dict(arrowstyle='<->', lw=2))
    ax2.text(1.15, 0.25, "Głębokość $d/2$", ha='left', va='center', fontsize=14)

    # Ustawienia osi dla obu wykresów (ukrycie siatki i ramek)
    for ax in [ax1, ax2]:
        ax.set_xlim(-0.1, 1.4)
        ax.set_ylim(-0.1, 1.15)
        ax.axis('off')

    plt.tight_layout()
    plt.savefig("wykres_double_search.jpg", dpi=300, bbox_inches='tight')
    print("Zapisano plik: wykres_double_search.jpg")
    plt.show()

if __name__ == "__main__":
    generate_search_tree_diagram()