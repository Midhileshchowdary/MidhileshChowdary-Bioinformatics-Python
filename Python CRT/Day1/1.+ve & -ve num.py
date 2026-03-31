#Write a Python Program to read the integer value as input from the user & check whether it is a positive  or negative number
a= int(input("Enter the integer value : "))
#using if-else
if(a>0):
    print(f"{a} is a +ve number")
elif(a<0):
    print(f"{a} is a -ve number")
else: print(f"{a} is 0")
#using ternary operator
Res="+ve number" if(a>0) else "-ve number"
print(f"{a} is a {Res}")
    