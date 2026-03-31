'''
1. input list of numbers
2. create 2 lists one for even and one for odd
3. display both lists
'''
List=[]
size=int(input("Enter the size of list : "))
for i in range(size):
    temp=int(input(f"Enter the number :"))
    List.append(temp)
even=[]
odd=[]
for i in List:
    if i %2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"Original List: {List}")
print(f"Even List: {even}")
print(f"Odd List: {odd}")