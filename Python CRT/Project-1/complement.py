seq = input("enter the sequence: ")
seq_com = ""
complement = ""
for i in range(len(seq)):
    if seq[i] == "A":
        complement += 'T'
    elif seq[i] == 'G':
        complement += 'C'
    elif seq[i] == 'T':
        complement += 'A'
    elif seq[i] == 'C':
        complement += 'G'
rev = complement[::-1]
print(rev == seq)