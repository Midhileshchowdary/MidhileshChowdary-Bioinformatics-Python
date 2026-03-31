#write a python program to read 2 integer values as input from the user swap them
num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
print("Num1 = ",num1)
print("Num2 = ",num2)
print("After Swapping = ")
num1, num2 = num2, num1
print("Num1 = ",num1)
print("Num2 = ",num2)
Temp=num1
num1=num2
num2=Temp
print("Num1 = ",num1)
print("Num2 = ",num2)