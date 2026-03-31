'''Num=100
print("Program Execution begins")
print(Num)
try:
    print(Num/0)
except ZeroDivisionError:
    print("Dividing with zero Gives an Infinite")
print("Program execution ends")'''

Num=100
print("Program Execution begins")
print(Num)
try:
    print(Num/10)
finally:
    print("Dividing with zero Gives an Infinite")
print("Program execution ends")