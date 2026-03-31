'''
5. Calculate the Average of Numbers in a Given List
Write a program to calculate and return the average (mean) of a list of numbers (integers or floats). If the list is empty, handle the case 
with a suitable message.
'''
Num=[]
result=0
length=int(input("Enter the number of elements required in the string : "))
for i in range(length):
    temp=int(input("Enter the integer : "))
    Num.append(temp)
if len(Num)==0:
    print("List is Empty")
else:
    for i in Num:
        result+=i
    Average=result/len(Num)
    print("The Average of the numbers in the list is :",Average)
