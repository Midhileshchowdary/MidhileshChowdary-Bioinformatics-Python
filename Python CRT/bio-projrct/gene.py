
'''
write a py prog to count how many genes belong to each family from the given dataand visualixe it using bar chart
'''
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
data = {
    "GeneID": [f"G{i}" for i in range(1, 19)],
    "Family": [
        "Kinase", "Ligase", "Kinase", "Polymerase", "Kinase", "Ligase",
        "Transferase", "Kinase", "Transferase", "Polymerase", "Ligase",
        "Kinase", "Transferase", "Polymerase", "Ligase", "Kinase",
        "Transferase", "Kinase"
    ]
}

df = pd.DataFrame(data)
# Count genes in each family
family_counts = df['Family'].value_counts()
# Plot bar chart
plt.figure(figsize=(8, 5))
family_counts.plot.bar(color='pink', edgecolor='black')
plt.title("Gene count in Each Family")
plt.xlabel("Gene Family")
plt.ylabel("Number of Genes")
plt.tight_layout()
plt.show()
