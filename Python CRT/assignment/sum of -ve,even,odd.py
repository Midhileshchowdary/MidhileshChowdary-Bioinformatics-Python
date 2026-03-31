'''
6. Print Sum of Negative Numbers, Positive Even Numbers, and Positive Odd Numbers in a List
Write a program that takes a list of integers and calculates:

* The sum of all negative numbers
* The sum of all positive even numbers
* The sum of all positive odd numbers
  Display each sum clearly
'''
Num=[]
negativesum=0
evensum =0
oddsum = 0
len=int(input("Enter the number of elements required in the string : "))
for i in range(len):
    temp=int(input("Enter the integers: "))
    Num.append(temp)
for i in Num:
    if (i<0):
        negativesum += i
    elif (i>0 and i%2 == 0):
        evensum += i
    elif (i > 0 and i % 2 != 0):
        oddsum += i
print("Sum of negative numbers:", negativesum)
print("Sum of positive even numbers:", evensum)
print("Sum of positive odd numbers:", oddsum)