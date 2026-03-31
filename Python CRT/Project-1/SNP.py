seq1 = input("enter Sequence seq1: ")
seq2 = input("enter Sequence seq2: ")
if len(seq1)==len(seq2):
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            print(f"SNP at position {i}: {seq1[i]} -> {seq2[i]}")
else:
    print("Both sequences lengths are not same. Please enter sequences with same length")