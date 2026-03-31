'''
problem: given dna sequences, calculate gc content of each and plot it as a histogram
'''
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
data = {
    "GeneID": [f"G{i}" for i in range(1, 16)],
    "Sequence": [
        "ATGCGTAA", "GGGCGCGT", "ATATATAT", "CGCGATAT",
        "GCGTGCAT", "TTATTATA", "CCGGCCGG", "GATCGATC",
        "TATATATA", "GCGCGCGC", "ATGCATGC", "GGATCCGG",
        "CATCATGG", "TGCATGCA", "GGTACCGA"
    ]
}
df = pd.DataFrame(data)
#---gc content
def gc_content(seq):
    g = seq.count('G')
    c = seq.count('C')
    return (g + c) / len(seq) * 100
df["GC_Content"] = df["Sequence"].apply(gc_content)
plt.figure(figsize=(8, 5))
plt.hist(df["GC_Content"], bins=5, color='skyblue', edgecolor='black')
plt.title("GC Content Distribution")
plt.xlabel("GC Content (%)")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
