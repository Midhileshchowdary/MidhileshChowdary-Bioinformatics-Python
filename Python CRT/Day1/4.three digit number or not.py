#write a python program to read the integer value as input from the user and check whether it is a three digit number or not
Num=int(input("Enter the number: "))
#using if-else
if -999 <= Num <= -100 or 100 <= Num <= 999:
    print(f"{Num} is a three-digit number.")
else:
    print(f"{Num} is not a three-digit number.")
#using ternary operator
res="a 3-digit number" if (100<=Num <=999 or -999<=Num<= -100 ) else "not a 3-digit number"
print(f"{Num} is {res}")