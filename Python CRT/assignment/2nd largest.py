'''
3. Find the Second Largest Number in a List
Given a list of integers, write a program to find and return the second largest unique number in the 
list. If no such number exists (due to insufficient unique values), handle it appropriately.
'''
List=[]
length=int(input("Enter the number of elements required in the string : "))
for i in range(length):
    temp=int(input("Enter the integer : "))
    List.append(temp)
if len(List)<2:
        print("More than 2 numbers required")
else:
        List.sort()
print("The second largest number in the List is :",List[-2])