'''
problem : 
'''
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
#------data----
data = {
    "ProteinID": [f"P{i}" for i in range(1, 13)],
    "Sequence": [
        "MAGDTPLKNQV", "AAAGGTTCCSS", "MLVITGVAGGL", "WQQVVSSGGA",
        "FFTLLVVAAK", "GGGGSSSAAA", "CCDDDEEEFF", "MMNNPPQQRR",
        "KKTTSSTTGG", "VVVVAAAAFFF", "LLLIIIHHHHH", "SSSTTTGGGAA"
    ]
}
df=pd.DataFrame(data)
#-------composition----
all_seq="".join(df["Sequence"])
counts=Counter(all_seq)
labels,sizes=zip(*sorted(counts.items()))
#----------visual------------
cmap=plt.colormaps.get_cmap("tab20")
colors= [cmap(i) for i in range(len(labels))]

plt.figure(figsize=(9,9))
wedges, _,autotexts=plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=[0.05]*len(labels),
    startangle=140,
    autopct=lambda pct: f"{pct:.1f}%\n({int(pct/100*sum(sizes))})",
    textprops=dict(color="black",fontsize=10)
)
plt.legend(
    wedges,
    [f"{aa}:{cnt}" for aa, cnt in counts.items()],
    title="Amino Acis (count)",
    bbox_to_anchor=(1,0.5),
    loc="center left",
    fontsize=9
)
plt.title("Amino Acid composition from 12 proteins.",fontsize=14,fontweight="bold",color="darkblue")
plt.tight_layout()
plt.show()