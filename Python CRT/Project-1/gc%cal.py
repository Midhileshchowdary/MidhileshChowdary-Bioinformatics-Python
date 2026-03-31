sequence=input("Enter the DNA sequence : ")
count,GC_count=0,0
for base in sequence:
    if base=='C' or base=='G':
        GC_count+=1
for base in sequence:
    if base=='T' or base=='G' or base=='C' or base=='A':
        count+=1
    else:
        print("error in sequence")
GC_percent=(GC_count)/(count)*100
print(f"GC Percentage : {GC_percent}")
if GC_percent > 60:
    print("Classification : High GC")
elif GC_percent >= 40 and GC_percent<=60:
    print("Classification : Moderate GC")
else:
    print("Classification : Low GC")
