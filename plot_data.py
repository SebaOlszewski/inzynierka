# plot_results.py
import os
import shutil
import matplotlib
# Wyłączenie GUI – generowanie plików w tle bez otwierania okienek
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

CSV_FILE = "solve_data.csv"
RESULTS_DIR = "results"
STANDARD_DIR = os.path.join(RESULTS_DIR, "results_standard")
LOG_DIR = os.path.join(RESULTS_DIR, "results_log")

COLORS = ["#2b5c8f", "#d95f02", "#2ca02c", "#8c564b"]  # LBL, BLIND, CFOP, OPTIMAL
ALGORITHMS = ["LBL", "BLIND", "CFOP", "OPTIMAL"]

METRICS = [
    {
        "title": "Średni czas ułożenia kostki",
        "ylabel": "Czas [ms]",
        "cols": ["LBL Time (ms)", "Blind Time (ms)", "CFOP Time (ms)", "Optimal Time (ms)"],
        "fmt": "{:.2f} ms",
        "log_capable": True
    },
    {
        "title": "Średnia liczba wykonanych ruchów",
        "ylabel": "Liczba ruchów (HTM)",
        "cols": ["LBL Moves", "Blind Moves", "CFOP Moves", "Optimal Moves"],
        "fmt": "{:.1f}",
        "log_capable": True
    },
    {
        "title": "Średnie wykorzystanie procesora (CPU)",
        "ylabel": "Obciążenie CPU [%]",
        "cols": ["LBL CPU Usage", "Blind CPU Usage", "CFOP CPU Usage", "Optimal CPU Usage"],
        "fmt": "{:.1f}%",
        "log_capable": False
    },
    {
        "title": "Szczytowe zużycie pamięci RAM",
        "ylabel": "Pamięć [MB]",
        "cols": ["LBL Memory Used (MB)", "Blind Memory Used (MB)", "CFOP Memory Used (MB)", "Optimal Memory Used (MB)"],
        "fmt": "{:.3f} MB",
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
    print("\n" + "=" * 102)
    print("                   STATYSTYKI OPISOWE DO TABELI W PRACY MAGISTERSKIEJ")
    print("=" * 102)
    print(f"{'Parametr':<32} | {'N':<5} | {'Średnia':<10} | {'Odch. std':<10} | {'Mediana':<10} | {'Min':<10} | {'Max':<10}")
    print("-" * 102)

    for m in METRICS:
        for alg, col in zip(ALGORITHMS, m["cols"]):
            series = df[col].dropna()
            n_count = len(series)
            std_val = series.std() if n_count > 1 else 0.0
            label = f"{alg} - {m['ylabel']}"
            print(
                f"{label:<32} | {n_count:<5} | {series.mean():<10.3f} | {std_val:<10.3f} | "
                f"{series.median():<10.3f} | {series.min():<10.3f} | {series.max():<10.3f}"
            )
        print("-" * 102)


def plot_bar_averages(df, out_dir, use_log=False):
    """Generuje siatkę 2x2 wykresów słupkowych (w skali standardowej lub logarytmicznej)."""
    fig, axes = plt.subplots(2, 2, figsize=(13, 9), dpi=300)
    n_total = len(df)
    n_opt = len(df["Optimal Moves"].dropna())
    scale_label = "SKALA LOGARYTMICZNA" if use_log else "SKALA LINIOWA"
    fig.suptitle(
        f"Porównanie średnich wyników LBL, BLIND, CFOP (n={n_total}) oraz OPTIMAL (n={n_opt}) [{scale_label}]",
        fontsize=12.5, fontweight="bold", y=0.98
    )

    for ax, m in zip(axes.flat, METRICS):
        means = [df[c].dropna().mean() for c in m["cols"]]
        is_log_axis = use_log and m["log_capable"]

        bars = ax.bar(
            ALGORITHMS, means,
            color=COLORS, edgecolor="black", linewidth=1.0, alpha=0.88, width=0.55
        )

        title_suffix = " (skala log)" if is_log_axis else ""
        ax.set_title(m["title"] + title_suffix, fontsize=12, fontweight="bold", pad=10)
        ax.set_ylabel(m["ylabel"], fontsize=10)
        ax.grid(axis="y", which="both" if is_log_axis else "major", linestyle="--", alpha=0.5)
        ax.set_axisbelow(True)

        if is_log_axis:
            ax.set_yscale("log")
            positive_means = [v for v in means if v > 0]
            min_v = min(positive_means) if positive_means else 1e-3
            max_v = max(positive_means) if positive_means else 1.0
            ax.set_ylim(min_v * 0.35, max_v * 4.5)

            for bar, mu in zip(bars, means):
                if mu > 0:
                    ax.text(
                        bar.get_x() + bar.get_width() / 2.0, mu * 1.22,
                        m["fmt"].format(mu),
                        ha="center", va="bottom", fontsize=9, fontweight="bold"
                    )
        else:
            max_height = max(means + [1e-6])
            ax.set_ylim(0, max_height * 1.18)

            for bar, mu in zip(bars, means):
                y_pos = mu + (max_height * 0.02)
                ax.text(
                    bar.get_x() + bar.get_width() / 2.0, y_pos,
                    m["fmt"].format(mu),
                    ha="center", va="bottom", fontsize=9, fontweight="bold"
                )

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    out_path = os.path.join(out_dir, "wykres_1_srednie_slupkowy.png")
    plt.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[ZAPISANO] {out_path}")


def plot_boxplots(df, out_dir, use_log=False):
    """Generuje siatkę 2x2 wykresów pudełkowych (w skali standardowej lub logarytmicznej)."""
    fig, axes = plt.subplots(2, 2, figsize=(13, 9), dpi=300)
    n_total = len(df)
    n_opt = len(df["Optimal Moves"].dropna())
    scale_label = "SKALA LOGARYTMICZNA" if use_log else "SKALA LINIOWA"
    fig.suptitle(
        f"Rozkład parametrów układania kostki (Boxplot, n={n_total}, OPTIMAL n={n_opt}) [{scale_label}]",
        fontsize=12.5, fontweight="bold", y=0.98
    )

    for ax, m in zip(axes.flat, METRICS):
        is_log_axis = use_log and m["log_capable"]
        data = []
        for c in m["cols"]:
            vals = df[c].dropna().values
            if is_log_axis:
                vals = vals[vals > 0]
            data.append(vals)

        bp = ax.boxplot(
            data, tick_labels=ALGORITHMS, patch_artist=True, widths=0.45,
            medianprops=dict(color="black", linewidth=2.0),
            flierprops=dict(marker="o", markerfacecolor="red", markersize=5, alpha=0.6)
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
        ax.set_title(base_title + title_suffix, fontsize=12, fontweight="bold", pad=10)
        ax.set_ylabel(m["ylabel"], fontsize=10)

        if is_log_axis:
            ax.set_yscale("log")

        ax.grid(axis="y", which="both" if is_log_axis else "major", linestyle="--", alpha=0.5)
        ax.set_axisbelow(True)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    out_path = os.path.join(out_dir, "wykres_2_rozklad_boxplot.png")
    plt.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[ZAPISANO] {out_path}")


def plot_stability_over_trials(df, out_dir, use_log=False):
    """Generuje wykres przebiegu liczby ruchów i czasu dla kolejnych scrambli."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), dpi=300, sharex=True)
    scale_label = "SKALA LOGARYTMICZNA" if use_log else "SKALA LINIOWA"
    fig.suptitle(
        f"Stabilność algorytmów w kolejnych próbach testowych [{scale_label}]",
        fontsize=13.5, fontweight="bold", y=0.98
    )

    move_cols = ["LBL Moves", "Blind Moves", "CFOP Moves", "Optimal Moves"]
    time_cols = ["LBL Time (ms)", "Blind Time (ms)", "CFOP Time (ms)", "Optimal Time (ms)"]

    for alg, col, color in zip(ALGORITHMS, move_cols, COLORS):
        sub = df[["Index", col]].dropna()
        ax1.plot(
            sub["Index"], sub[col], marker="o", markersize=4,
            linewidth=1.5, color=color, label=f"{alg} (śr. {sub[col].mean():.1f})"
        )
    ax1.set_title(
        "Liczba wykonanych ruchów dla poszczególnych scrambli" + (" (skala log)" if use_log else ""),
        fontsize=11, fontweight="bold"
    )
    ax1.set_ylabel("Liczba ruchów")
    if use_log:
        ax1.set_yscale("log")
    ax1.grid(True, which="both" if use_log else "major", linestyle="--", alpha=0.5)
    ax1.legend(loc="upper right")

    for alg, col, color in zip(ALGORITHMS, time_cols, COLORS):
        sub = df[["Index", col]].dropna()
        ax2.plot(
            sub["Index"], sub[col], marker="s", markersize=4,
            linewidth=1.5, color=color, label=f"{alg} (śr. {sub[col].mean():.2f} ms)"
        )
    ax2.set_title(
        "Czas ułożenia dla poszczególnych scrambli" + (" (skala log)" if use_log else ""),
        fontsize=11, fontweight="bold"
    )
    ax2.set_xlabel("Numer próby (Index scrambla)")
    ax2.set_ylabel("Czas [ms]")
    if use_log:
        ax2.set_yscale("log")
    ax2.grid(True, which="both" if use_log else "major", linestyle="--", alpha=0.5)
    ax2.legend(loc="upper right")

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    out_path = os.path.join(out_dir, "wykres_3_stabilnosc_scrambli.png")
    plt.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[ZAPISANO] {out_path}")


def main():
    if not os.path.exists(CSV_FILE):
        print(f"Błąd: Nie znaleziono pliku '{CSV_FILE}'. Uruchom najpierw TEST w main.py.")
        wait_for_exit()
        return

    df = pd.read_csv(CSV_FILE)
    if df.empty:
        print(f"Plik '{CSV_FILE}' jest pusty.")
        wait_for_exit()
        return

    prepare_results_directories()
    print_thesis_summary_table(df)

    print("\n--- Generowanie wykresów: SKALA STANDARDOWA (LINIOWA) ---")
    plot_bar_averages(df, STANDARD_DIR, use_log=False)
    plot_boxplots(df, STANDARD_DIR, use_log=False)
    plot_stability_over_trials(df, STANDARD_DIR, use_log=False)

    print("\n--- Generowanie wykresów: SKALA LOGARYTMICZNA ---")
    plot_bar_averages(df, LOG_DIR, use_log=True)
    plot_boxplots(df, LOG_DIR, use_log=True)
    plot_stability_over_trials(df, LOG_DIR, use_log=True)

    print(f"\nGotowe! Zapisano oba zestawy wykresów w:\n  1) {os.path.abspath(STANDARD_DIR)}\n  2) {os.path.abspath(LOG_DIR)}")
    wait_for_exit()


if __name__ == "__main__":
    main()