n=int(input("Enter the number : "))
steps=0
while n>1:
    if n % 3 ==0:
        n//=3
    elif n%2==0:
        n//=2
    else:
        n-=1
    steps+=1
print(steps)