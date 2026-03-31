#write a python program to read the list elements as input from user & display the list elements using for loop
size=int(input("Enter the size of list : "))
program_lang=[]
#reading list elements as input
for i in range(size):
    temp=input("enter a programming language :")
    program_lang.append(temp)
print(f"Elements of the list: {program_lang}")