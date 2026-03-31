#write a python program to read the size of list as input from the user and take the list elements also as input from the user and
#find the length of the list, the maximum element or nmber in the list min  element, summation of elements in the list and print
# the sorted list in ascending order
size=int(input("Enter the size of list: "))
Num=[]
for i in range(size):
    temp=int(input(f"Enter the element at {i} index: "))
    Num.append(temp)
print(f"Given list: {Num}")
print("Length of the list:", len(Num))
print("Maximum element:", max(Num))
print("Minimum element:", min(Num))
print("Summation:", sum(Num))
print("Sorted list:", sorted(Num))

