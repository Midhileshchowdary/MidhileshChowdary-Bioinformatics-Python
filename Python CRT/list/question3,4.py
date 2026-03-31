#write a python program to read the list elemenets as input from user and print a  new list of numbers which are multiples of 5
Size=int(input("Enter the Size of the list : "))
list=[]
for i in range(Size):
    temp=int(input("Enter the number :"))
    list.append(temp)
print(f"Elements of the list: {list}")
new_list=[]
for i in list:
    if (i % 5 == 0):
        new_list.append(i)
print(new_list)
#write a python program to read the list elemenets as input from user and print and check whether the list elements are 
# multiple of 3 and 5 or not and print the list of elements which are multiples of 3 and 5.
Size=int(input("Enter the Size of the list : "))
list=[]
for i in range(Size):
    temp=int(input("Enter the number :"))
    list.append(temp)
print(f"Elements of the list: {list}")
new_list=[]
for i in list:
    if (i % 15 == 0):
        new_list.append(i)
print(new_list)