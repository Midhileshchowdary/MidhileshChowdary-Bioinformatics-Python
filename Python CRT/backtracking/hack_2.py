#Scenario Based question HWI
t=int(input("Enter the number: "))
for _ in range(t):
    values=input("Enter the stones").split()
    a= int(values[0])
    b=int(values[1])
    c=int(values[2])
    x = int(values[3])
    y = int(values[4])
    if a + b + c != x+y:
        print("No")
    elif max(x,y)> max(a+b, b+a,c+a):
        print("NO")
    else:
        print("Yes")