#write a Python Program to read the integer value as input from the user & check whether it is a digit or number
Num=int(input("Enter the number: "))
#using if-else
if(Num>=-9 and Num<=9):
    print(f"{Num} is a digit")
else: print(f"{Num} is a number")
#using ternary operator
res="digit" if(Num>=-9 and Num<=9) else "Number"
print(f"{Num} is a {res}")