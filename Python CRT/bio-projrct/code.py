'''
You'r given a dataset containing gene expression levels across multiple timepoints
your task is to:
calculate the variance of gxpression per gene
identify the top N most dynamic genes
Plot their expression profile using matplotlib

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('bio-project\expression_data.csv') #relative path
gene_ids=df["Gene_ID"]
expression_data=df.drop(columns=["Gene_ID"])
variances=expression_data.var(axis=1)
N=3
top_indices=np.argsort(-variances)[:N]
top_genes=gene_ids.iloc[top_indices]
top_expr=expression_data.iloc[top_indices]
timepoints=expression_data.columns.tolist()
plt.figure(figsize=(10,6))
for i in range(N):
    plt.plot(timepoints,top_expr.iloc[i],marker='o',label=top_genes.iloc[i])
plt.title(f"Top {N} Most dynamic genes (by variance)")
plt.xlabel("Time points")
plt.ylabel("Expression level")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()