'''
write a py program to read the list of characters  as input from the user and convert it into a word and print it
'''
Size=int(input("Enter the Size of the list : "))
list=[]
for i in range(Size):
    temp=input("Enter the characters :")
    list.append(temp)
print(list)
string=''.join(list)
print(string)
print(type(string))
