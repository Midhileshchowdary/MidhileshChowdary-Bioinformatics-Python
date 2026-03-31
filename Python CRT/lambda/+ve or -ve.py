'''
write a py program to check whether the number is positive or negative using lamda function
'''
# turneray operator:  syntax---> true if (condition ) else  false
res=lambda Num:print("positive") if (Num>0)  else print("Negative") if Num<0 else print("Zero")   # single line
x=int(input("Enter the number : "))
res(x) ## for taking input from user
res(0)

# multiple lines using functions
def Positive(Num):
    if(Num>0):
        print("+ve")
    else:
        if(Num==0):
            print("0")
        else:
            print("-ve")
Positive(4)