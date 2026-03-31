#write a python program to print the reversed multiplication tables from n to 1
n=int(input("Enter Number:"))
for i in range (n,0,-1):
    print(f"Multiplication Table of {i}:")
    for j in range (1,11):
        print(f"{i} * {j} =",i*j)
    