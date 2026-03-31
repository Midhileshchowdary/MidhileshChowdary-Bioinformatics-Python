n=int(input("Enter the value of n : "))
value=1
for i in range (1,n+1):
    for j in range(i):
        print(f"{value} ",end="")
        value+=1
    print()