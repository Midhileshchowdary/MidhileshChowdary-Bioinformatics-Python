#write python program to remove the duplicate values from the list
List=[8,9,2,0,3,8,9,2,0,3]
print("Original List: ")
print(List)
New_List=[]
for i in List:
    if i not in New_List:
        New_List.append(i)
print(New_List)