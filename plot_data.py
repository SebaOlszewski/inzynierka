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
    plt.legend(loc='lower left')
    plt.savefig(os.path.join(results_folder, "LBL_Moves.png"))
    plt.close()
    
    plt.figure(figsize=(15, 5))
    plt.plot(df['Index'], df['Blind Moves'], label='Blind Moves', color='blue')
    plt.axhline(df['Blind Moves'].mean(), color='darkblue', linestyle='dashed', label='Blind Avg')
    plt.xlabel('Solve ID')
    plt.ylabel('Moves')
    plt.title('Blind Solve Moves per Solve')
    plt.legend(loc='lower left')
    plt.savefig(os.path.join(results_folder, "Blind_Moves.png"))
    plt.close()
    
    plt.figure(figsize=(15, 5))
    plt.plot(df['Index'], df['CFOP Moves'], label='CFOP Moves', color='red')
    plt.axhline(df['CFOP Moves'].mean(), color='darkred', linestyle='dashed', label='CFOP Avg')
    plt.xlabel('Solve ID')
    plt.ylabel('Moves')
    plt.title('CFOP Solve Moves per Solve')
    plt.legend(loc='lower left')
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
    plt.legend(loc='lower left')
    plt.savefig(os.path.join(results_folder, "Solve_Times.png"))
    plt.close()
    
    # Combined CPU Usage Graph
    plt.figure(figsize=(15, 5))
    plt.plot(df['Index'], df['LBL CPU Usage'], label='LBL CPU Usage (%)', color='green')
    plt.plot(df['Index'], df['CFOP CPU Usage'], label='CFOP CPU Usage (%)', color='red')
    plt.plot(df['Index'], df['Blind CPU Usage'], label='Blind CPU Usage (%)', color='blue')
    plt.xlabel('Solve ID')
    plt.ylabel('CPU Usage (%)')
    plt.title('CPU Usage per Algorithm')
    plt.legend(loc='lower left')
    plt.savefig(os.path.join(results_folder, "CPU_Usage.png"))
    plt.close()
    
    # Memory Usage Graphs
    plt.figure(figsize=(15, 5))
    plt.plot(df['Index'], df['LBL Memory Used (MB)'], label='LBL Memory Used (MB)', color='lime')
    plt.xlabel('Solve ID')
    plt.ylabel('Memory Used (MB)')
    plt.title('LBL Memory Usage')
    plt.legend(loc='lower left')
    plt.savefig(os.path.join(results_folder, "LBL_Memory_Usage.png"))
    plt.close()
    
    plt.figure(figsize=(15, 5))
    plt.plot(df['Index'], df['CFOP Memory Used (MB)'], label='CFOP Memory Used (MB)', color='salmon')
    plt.xlabel('Solve ID')
    plt.ylabel('Memory Used (MB)')
    plt.title('CFOP Memory Usage')
    plt.legend(loc='lower left')
    plt.savefig(os.path.join(results_folder, "CFOP_Memory_Usage.png"))
    plt.close()
    
    plt.figure(figsize=(15, 5))
    plt.plot(df['Index'], df['Blind Memory Used (MB)'], label='Blind Memory Used (MB)', color='cyan')
    plt.xlabel('Solve ID')
    plt.ylabel('Memory Used (MB)')
    plt.title('Blind Memory Usage')
    plt.legend(loc='lower left')
    plt.savefig(os.path.join(results_folder, "Blind_Memory_Usage.png"))
    plt.close()
    
    # Combined Memory Usage Graph
    plt.figure(figsize=(15, 5))
    plt.plot(df['Index'], df['LBL Memory Used (MB)'], label='LBL Memory Used (MB)', color='lime')
    plt.plot(df['Index'], df['CFOP Memory Used (MB)'], label='CFOP Memory Used (MB)', color='salmon')
    plt.plot(df['Index'], df['Blind Memory Used (MB)'], label='Blind Memory Used (MB)', color='cyan')
    plt.xlabel('Solve ID')
    plt.ylabel('Memory Used (MB)')
    plt.title('Memory Usage per Algorithm')
    plt.legend(loc='lower left')
    plt.savefig(os.path.join(results_folder, "Combined_Memory_Usage.png"))
    plt.close()



plot_solve_data("solve_data.csv")