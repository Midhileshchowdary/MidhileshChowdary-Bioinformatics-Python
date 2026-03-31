'''
1. Take a list of toy names (some repeated)
2. Remove duplicate
3. Sort and display the final list to pack
'''
Toy_List=[]
num=int(input("Size of the list : "))
for i in range(num):
    temp=input("Enter the toy name :")
    Toy_List.append(temp)
print(f"Elements of the list: {Toy_List}")
new_list=[]
for i in Toy_List:
    if i not in new_list:
        new_list.append(i)
new_list.sort()
print(new_list)