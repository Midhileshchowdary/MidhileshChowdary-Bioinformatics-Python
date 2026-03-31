'''
Count the DNA Bases Like a Pro
② Scenario: You're helping your lab analyze a DNA sample.Your finst task? count how many times each base (A, T,C, G)appears in a ONA string.
9 Your task;
Write a program that:
checks if the string has only valid bases (A, T, C, G).Then counts how many of each base there are.
Enter the "ATGCGATAAGCTTAA"
& Expected output:{'A':6,'T':4,'G':2,'C':2}
'''
DNA="ATGCGATAAGCTTAA"
Dict={'A':0,'T':0,'C':0,'G':0}
A_count,T_count,C_count,G_count=0,0,0,0
for base in DNA:
    if base=='A':
        A_count+=1
    elif base=='T':
        T_count+=1
    elif base=='C':
        C_count+=1
    elif base=='G':
        G_count+=1
    else:
        print("error in sequence")
Dict['A']=A_count
Dict['T']=T_count
Dict['C']=C_count
Dict['G']=G_count
print(Dict)
#another method
seq=input("Enter the sequence ")
countbase={'A':seq.count('A'),'T':seq.count('T'),'C':seq.count('C'),'G':seq.count('G')}
print(countbase)