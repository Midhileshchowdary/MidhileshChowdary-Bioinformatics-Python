'''
1. take two grocery lists.
2. combine them into one
3. remove duplicates
4. sort and print the final list
'''
#List 1 
List1=[]
num=int(input("Size of the list : "))
for i in range(num):
    temp=input("Enter the item name :")
    List1.append(temp)
print(f"Elements of the list: {List1}")
#List 2
List2=[]
num=int(input("Size of the list : "))
for i in range(num):
    temp=input("Enter the item name :")
    List2.append(temp)
print(f"Elements of the list: {List2}")
completelist=List1+List2
print(f"Elements in the Final list: {completelist}")
New_List=[]
for i in completelist:
    if i not in New_List:
        New_List.append(i)
print(f"List without duplicates : {New_List}")
print("Sorted list:", sorted(New_List))