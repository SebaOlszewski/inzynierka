import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_solve_data(csv_file):
    # Load data
    df = pd.read_csv(csv_file)
    
    # Create results folder if it doesn't exist
    results_folder = "results"
    os.makedirs(results_folder, exist_ok=True)
    
    # Plot moves per solve for each method with average line
    plt.figure(figsize=(15, 5))
    plt.plot(df['Index'], df['LBL Moves'], label='LBL Moves', color='green')
    plt.axhline(df['LBL Moves'].mean(), color='darkgreen', linestyle='dashed', label='LBL Avg')
    plt.xlabel('Solve ID')
    plt.ylabel('Moves')
    plt.title('LBL Solve Moves per Solve')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.savefig(os.path.join(results_folder, "LBL_Moves.png"))
    plt.close()
    
    plt.figure(figsize=(15, 5))
    plt.plot(df['Index'], df['Blind Moves'], label='Blind Moves', color='blue')
    plt.axhline(df['Blind Moves'].mean(), color='darkblue', linestyle='dashed', label='Blind Avg')
    plt.xlabel('Solve ID')
    plt.ylabel('Moves')
    plt.title('Blind Solve Moves per Solve')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.savefig(os.path.join(results_folder, "Blind_Moves.png"))
    plt.close()
    
    plt.figure(figsize=(15, 5))
    plt.plot(df['Index'], df['CFOP Moves'], label='CFOP Moves', color='red')
    plt.axhline(df['CFOP Moves'].mean(), color='darkred', linestyle='dashed', label='CFOP Avg')
    plt.xlabel('Solve ID')
    plt.ylabel('Moves')
    plt.title('CFOP Solve Moves per Solve')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.savefig(os.path.join(results_folder, "CFOP_Moves.png"))
    plt.close()
    
    # Plot solve time comparison in milliseconds with average line
    plt.figure(figsize=(15, 5))
    plt.plot(df['Index'], df['LBL Time (ms)'], label='LBL Time', color='green')
    plt.axhline(df['LBL Time (ms)'].mean(), color='darkgreen', linestyle='dashed', label='LBL Avg')
    plt.plot(df['Index'], df['CFOP Time (ms)'], label='CFOP Time', color='red')
    plt.axhline(df['CFOP Time (ms)'].mean(), color='darkred', linestyle='dashed', label='CFOP Avg')
    plt.plot(df['Index'], df['Blind Time (ms)'], label='Blind Time', color='blue')
    plt.axhline(df['Blind Time (ms)'].mean(), color='darkblue', linestyle='dashed', label='Blind Avg')
    plt.xlabel('Scramble ID')
    plt.ylabel('Time (ms)')
    plt.title('Solve Time per Algorithm')
    plt.ylim(0)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.savefig(os.path.join(results_folder, "Solve_Times.png"))
    plt.close()

    



# Example usage
plot_solve_data("solve_data.csv")
