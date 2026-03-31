import tkinter as tk
from tkinter import messagebox
import subprocess
import requests
from Bio import AlignIO
import matplotlib.pyplot as plt
from collections import Counter

# --- Fetch sequences from UniProt and save to FASTA ---
def fetch_sequences(ids, output_file="sequences.fasta"):
    with open(output_file, "w") as f:
        for pid in ids:
            url = f"https://www.uniprot.org/uniprot/{pid}.fasta"
            response = requests.get(url)
            if response.status_code == 200:
                f.write(response.text)
            else:
                print(f"Failed to fetch {pid}")
                messagebox.showerror("Fetch Error", f"Failed to fetch sequence for {pid}")

# --- Run MUSCLE alignment ---
def run_alignment(input_file="sequences.fasta", output_file="aligned.aln"):
    try:
        subprocess.run(["muscle", "-in", input_file, "-out", output_file], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Alignment Error", "Failed to run MUSCLE. Make sure muscle.exe is in the system PATH.")

# --- Plot conservation score ---
def plot_conservation(alignment_file="aligned.aln"):
    try:
        alignment = AlignIO.read(alignment_file, "clustal")
        length = alignment.get_alignment_length()
        conservation = []

        for i in range(length):
            column = alignment[:, i]
            count = Counter(column)
            score = count.most_common(1)[0][1] / len(column)
            conservation.append(score)

        plt.figure(figsize=(10, 4))
        plt.plot(conservation, color='green')
        plt.title("MSA Conservation Score")
        plt.xlabel("Alignment Position")
        plt.ylabel("Conservation (0 to 1)")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Visualization Error", f"Error reading alignment: {e}")

# --- GUI Setup ---
def run_pipeline():
    raw_input = entry.get().strip()
    if not raw_input:
        messagebox.showwarning("Input Error", "Please enter at least one UniProt ID.")
        return
    ids = [id.strip() for id in raw_input.split(",")]
    fetch_sequences(ids)
    run_alignment()
    plot_conservation()

root = tk.Tk()
root.title("MSA Visualizer - Bioinformatics")
root.geometry("500x150")

label = tk.Label(root, text="Enter UniProt Protein IDs (comma-separated):")
label.pack(pady=10)

entry = tk.Entry(root, width=60)
entry.pack()

button = tk.Button(root, text="Run MSA & Visualize", command=run_pipeline)
button.pack(pady=10)

root.mainloop()
