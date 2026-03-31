seq1 = input("enter seq1: ")
seq2 = input("enter seq2: ")
List = []
if len(seq1) == len(seq2):
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            List.append(i)
    print(List)
else:
    print("Sequences lengths are not equal. please enter sequences with same length")