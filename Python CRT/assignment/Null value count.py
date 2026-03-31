'''
1. Count the Number of Null Elements in a List
Write a program that takes a list containing various data types, including None values. Your task is to count how many None values 
are present in the list and return the count.
'''
List=[]
Length=int(input("Enter the number of elements :"))
count=0
for i in range(Length):
    temp=input("Enter the element :")
    List.append(temp)
for i in List:
    if i == " ":
        count+=1
print(f"The count of NULL values present in the List is : {count}")