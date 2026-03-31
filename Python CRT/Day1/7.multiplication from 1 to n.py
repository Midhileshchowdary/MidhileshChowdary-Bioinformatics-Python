#write python program to print multiplication tables from 1 to n 
n=int(input("Enter Number:"))
for i in range (1,n+1):
    print(f"Multiplication Table of {i}:")
    for j in range (1,11):
        print(f"{i} * {j} =",i*j)
    
