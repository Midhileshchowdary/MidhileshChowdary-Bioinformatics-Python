'''
4. Swap the First and Last Value of the Given List
Write a program that swaps the first and last elements of a given list and returns the updated list. The list may contain elements of any data
 type.
'''
List=[]
length=int(input("Enter the number of elements required in the string : "))
for i in range(length):
    temp=int(input("Enter the integer : "))
    List.append(temp)
List[0],List[-1]=List[-1], List[0]
print("After Swapping,",List)