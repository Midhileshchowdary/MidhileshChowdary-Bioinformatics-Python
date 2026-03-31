amino_acid_weights = {
    'A': 89.1,   # Alanine
    'C': 121.2,  # Cysteine
    'D': 133.1,  # Aspartic acid
    'E': 147.1,  # Glutamic acid
    'F': 165.2,  # Phenylalanine
    'G': 75.1,   # Glycine
    'H': 155.2,  # Histidine
    'I': 131.2,  # Isoleucine
    'K': 146.2,  # Lysine
    'L': 131.2,  # Leucine
    'M': 149.2,  # Methionine
    'N': 132.1,  # Asparagine
    'P': 115.1,  # Proline
    'Q': 146.2,  # Glutamine
    'R': 174.2,  # Arginine
    'S': 105.1,  # Serine
    'T': 119.1,  # Threonine
    'V': 117.1,  # Valine
    'W': 204.2,  # Tryptophan
    'Y': 181.2   # Tyrosine
}
query = input("enter query Sequence: ").strip()
total_wt = 0.0
for i in query:
    if i in amino_acid_weights:
        total_wt = total_wt+amino_acid_weights[i]
    else:
        print("enter valid amino acids")
print(total_wt)