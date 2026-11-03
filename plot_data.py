# plot_results.py
import os
import shutil
import matplotlib
# Wyłączenie GUI – generowanie plików w tle bez otwierania okienek
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

CSV_FILE = "solve_data.csv"
RESULTS_DIR = "results"
STANDARD_DIR = os.path.join(RESULTS_DIR, "results_standard")
LOG_DIR = os.path.join(RESULTS_DIR, "results_log")

# Zaktualizowane kolory: para SC (jaśniejszy) / MC (ciemniejszy) dla każdego z 4 algorytmów
COLORS = [
    "#4a83c4", "#1f4e79",  # LBL SC/MC (Niebieskie)
    "#ff8c42", "#a64b00",  # BLIND SC/MC (Pomarańczowe)
    "#4db84d", "#1e731e",  # CFOP SC/MC (Zielone)
    "#b57365", "#5c3228"   # OPTIMAL SC/MC (Brązowe)
]

ALGORITHMS = [
    "LBL (SC)", "LBL (MC)",
    "BLIND (SC)", "BLIND (MC)",
    "CFOP (SC)", "CFOP (MC)",
    "OPTIMAL (SC)", "OPTIMAL (MC)"
]

METRICS = [
    {
        "title": "Średni czas ułożenia kostki",
        "ylabel": "Czas [ms / min dla Optimal]",
        "cols": [
            "LBL SC Time (ms)", "LBL MC Time (ms)",
            "Blind SC Time (ms)", "Blind MC Time (ms)",
            "CFOP SC Time (ms)", "CFOP MC Time (ms)",
            "Optimal SC Time (min)", "Optimal MC Time (min)"
        ],
        # Funkcja formatująca dobierająca jednostkę w zależności od algorytmu
        "fmt_func": lambda val, alg_name: f"{val:.2f} min" if "OPTIMAL" in alg_name else f"{val:.2f} ms",
        "log_capable": True
    },
    {
        "title": "Średnia liczba wykonanych ruchów",
        "ylabel": "Liczba ruchów (HTM)",
        "cols": [
            "LBL SC Moves", "LBL MC Moves",
            "Blind SC Moves", "Blind MC Moves",
            "CFOP SC Moves", "CFOP MC Moves",
            "Optimal SC Moves", "Optimal MC Moves"
        ],
        "fmt_func": lambda val, alg_name: f"{val:.1f}",
        "log_capable": True
    },
    {
        "title": "Średnie wykorzystanie procesora (CPU)",
        "ylabel": "Obciążenie CPU [%]",
        "cols": [
            "LBL SC CPU Usage", "LBL MC CPU Usage",
            "Blind SC CPU Usage", "Blind MC CPU Usage",
            "CFOP SC CPU Usage", "CFOP MC CPU Usage",
            "Optimal SC CPU Usage", "Optimal MC CPU Usage"
        ],
        "fmt_func": lambda val, alg_name: f"{val:.1f}%",
        "log_capable": False
    },
    {
        "title": "Szczytowe zużycie pamięci RAM",
        "ylabel": "Pamięć [MB]",
        "cols": [
            "LBL SC Mem (MB)", "LBL MC Mem (MB)",
            "Blind SC Mem (MB)", "Blind MC Mem (MB)",
            "CFOP SC Mem (MB)", "CFOP MC Mem (MB)",
            "Optimal SC Mem (MB)", "Optimal MC Mem (MB)"
        ],
        "fmt_func": lambda val, alg_name: f"{val:.3f} MB",
        "log_capable": True
    }
]


def wait_for_exit():
    """Zatrzymuje zamknięcie konsoli do momentu wciśnięcia Enter."""
    try:
        input("\nNaciśnij Enter, aby zakończyć...")
    except (EOFError, KeyboardInterrupt):
        pass


def prepare_results_directories():
    """Czyści główny katalog results/ i tworzy podkatalogi results_standard oraz results_log."""
    if os.path.exists(RESULTS_DIR):
        for filename in os.listdir(RESULTS_DIR):
            file_path = os.path.join(RESULTS_DIR, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"[OSTRZEŻENIE] Nie udało się usunąć {file_path}: {e}")
        print(f"[KATALOG] Wyczyszczono zawartość folderu '{RESULTS_DIR}/'.")

    os.makedirs(STANDARD_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)
    print(f"[KATALOG] Utworzono podkatalogi: '{STANDARD_DIR}/' oraz '{LOG_DIR}/'.")


def print_thesis_summary_table(df):
    """Wypisuje w konsoli tabelę statystyczną (N, Średnia, Odch. std., Mediana, Min, Max)."""
    print("\n" + "=" * 105)
    print("                    STATYSTYKI OPISOWE DO TABELI W PRACY MAGISTERSKIEJ")
    print("=" * 105)
    print(f"{'Parametr':<35} | {'N':<5} | {'Średnia':<10} | {'Odch. std':<10} | {'Mediana':<10} | {'Min':<10} | {'Max':<10}")
    print("-" * 105)

    for m in METRICS:
        for alg, col in zip(ALGORITHMS, m["cols"]):
            series = df[col].dropna()
            n_count = len(series)
            std_val = series.std() if n_count > 1 else 0.0
            label = f"{alg} {m['ylabel']}"
            print(
                f"{label:<35} | {n_count:<5} | {series.mean():<10.3f} | {std_val:<10.3f} | "
                f"{series.median():<10.3f} | {series.min():<10.3f} | {series.max():<10.3f}"
            )
        print("-" * 105)


def plot_bar_averages(df, out_dir, use_log=False):
    """Generuje osobne wykresy słupkowe (w skali standardowej lub logarytmicznej)."""
    n_total = len(df)
    n_opt = len(df["Optimal SC Moves"].dropna())
    scale_label = "SKALA LOGARYTMICZNA" if use_log else "SKALA LINIOWA"

    for i, m in enumerate(METRICS):
        fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
        
        means = [df[c].dropna().mean() for c in m["cols"]]
        is_log_axis = use_log and m["log_capable"]

        bars = ax.bar(
            ALGORITHMS, means,
            color=COLORS, edgecolor="black", linewidth=1.0, alpha=0.88, width=0.6
        )

        title_suffix = " (skala log)" if is_log_axis else ""
        full_title = f"{m['title']}{title_suffix}\n(LBL, BLIND, CFOP: n={n_total} | OPTIMAL: n={n_opt}) [{scale_label}]"
        
        ax.set_title(full_title, fontsize=12, fontweight="bold", pad=10)
        ax.set_ylabel(m["ylabel"], fontsize=10)
        ax.grid(axis="y", which="both" if is_log_axis else "major", linestyle="--", alpha=0.5)
        ax.set_axisbelow(True)
        ax.tick_params(axis='x', rotation=45, labelsize=9)

        if is_log_axis:
            ax.set_yscale("log")
            positive_means = [v for v in means if v > 0]
            min_v = min(positive_means) if positive_means else 1e-3
            max_v = max(positive_means) if positive_means else 1.0
            ax.set_ylim(min_v * 0.35, max_v * 4.5)

            for bar, mu, alg_name in zip(bars, means, ALGORITHMS):
                if mu > 0:
                    ax.text(
                        bar.get_x() + bar.get_width() / 2.0, mu * 1.22,
                        m["fmt_func"](mu, alg_name),
                        ha="center", va="bottom", fontsize=8, fontweight="bold", rotation=90
                    )
        else:
            max_height = max(means + [1e-6])
            ax.set_ylim(0, max_height * 1.25)

            for bar, mu, alg_name in zip(bars, means, ALGORITHMS):
                y_pos = mu + (max_height * 0.03)
                ax.text(
                    bar.get_x() + bar.get_width() / 2.0, y_pos,
                    m["fmt_func"](mu, alg_name),
                    ha="center", va="bottom", fontsize=8, fontweight="bold", rotation=90
                )

        plt.tight_layout()
        
        safe_name = m["title"].replace(" ", "_").replace("(", "").replace(")", "").lower()
        out_path = os.path.join(out_dir, f"wykres_slupkowy_{i+1}_{safe_name}.png")
        plt.savefig(out_path, dpi=300)
        plt.close(fig)
        print(f"[ZAPISANO] {out_path}")


def plot_boxplots(df, out_dir, use_log=False):
    """Generuje osobne wykresy pudełkowe (w skali standardowej lub logarytmicznej)."""
    n_total = len(df)
    n_opt = len(df["Optimal SC Moves"].dropna())
    scale_label = "SKALA LOGARYTMICZNA" if use_log else "SKALA LINIOWA"

    for i, m in enumerate(METRICS):
        fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
        
        is_log_axis = use_log and m["log_capable"]
        data = []
        for c in m["cols"]:
            vals = df[c].dropna().values
            if is_log_axis:
                vals = vals[vals > 0]
            data.append(vals)

        bp = ax.boxplot(
            data, tick_labels=ALGORITHMS, patch_artist=True, widths=0.5,
            medianprops=dict(color="black", linewidth=2.0),
            flierprops=dict(marker="o", markerfacecolor="red", markersize=4, alpha=0.5)
        )
        for patch, color in zip(bp["boxes"], COLORS):
            patch.set_facecolor(color)
            patch.set_alpha(0.75)

        base_title = (
            m["title"]
            .replace("Średni ", "Rozkład: ")
            .replace("Średnie ", "Rozkład: ")
            .replace("Średnia ", "Rozkład: ")
        )
        title_suffix = " (skala log)" if is_log_axis else ""
        full_title = f"{base_title}{title_suffix}\n(SC vs MC, n={n_total}, OPTIMAL n={n_opt}) [{scale_label}]"
        
        ax.set_title(full_title, fontsize=12, fontweight="bold", pad=10)
        ax.set_ylabel(m["ylabel"], fontsize=10)
        ax.tick_params(axis='x', rotation=45, labelsize=9)

        if is_log_axis:
            ax.set_yscale("log")

        ax.grid(axis="y", which="both" if is_log_axis else "major", linestyle="--", alpha=0.5)
        ax.set_axisbelow(True)

        plt.tight_layout()
        
        safe_name = m["title"].replace(" ", "_").replace("(", "").replace(")", "").lower()
        out_path = os.path.join(out_dir, f"wykres_boxplot_{i+1}_{safe_name}.png")
        plt.savefig(out_path, dpi=300)
        plt.close(fig)
        print(f"[ZAPISANO] {out_path}")


def main():
    if not os.path.exists(CSV_FILE):
        print(f"Błąd: Nie znaleziono pliku '{CSV_FILE}'. Uruchom najpierw TEST w main.py.")
        wait_for_exit()
        return

    df = pd.read_csv(CSV_FILE)
    
    # Przeliczanie czasu Optimal z ms na minuty (1 minuta = 60 000 ms)
    optimal_time_ms_cols = ["Optimal SC Time (ms)", "Optimal MC Time (ms)"]
    optimal_time_min_cols = ["Optimal SC Time (min)", "Optimal MC Time (min)"]
    
    for col_ms, col_min in zip(optimal_time_ms_cols, optimal_time_min_cols):
        if col_ms in df.columns:
            df[col_min] = df[col_ms] / 60000.0

    if df.empty:
        print(f"Plik '{CSV_FILE}' jest pusty.")
        wait_for_exit()
        return

    prepare_results_directories()
    print_thesis_summary_table(df)

    print("\n--- Generowanie wykresów: SKALA STANDARDOWA (LINIOWA) ---")
    plot_bar_averages(df, STANDARD_DIR, use_log=False)
    plot_boxplots(df, STANDARD_DIR, use_log=False)

    print("\n--- Generowanie wykresów: SKALA LOGARYTMICZNA ---")
    plot_bar_averages(df, LOG_DIR, use_log=True)
    plot_boxplots(df, LOG_DIR, use_log=True)

    print(f"\nGotowe! Zapisano oba zestawy pojedynczych wykresów w:\n  1) {os.path.abspath(STANDARD_DIR)}\n  2) {os.path.abspath(LOG_DIR)}")
    wait_for_exit()


if __name__ == "__main__":
    main()