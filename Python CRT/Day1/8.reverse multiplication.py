#write a python program to print the reversed multiplication table of n
a=int(input("Enter Number:"))
for i in range (10,0,-1):
    print(f"{a} * {i}=",a*i)
    