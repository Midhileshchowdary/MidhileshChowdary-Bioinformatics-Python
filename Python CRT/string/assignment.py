# write  a python program to read the string as input from use
#1. print the string as a list of individual characters
# 2. find the length of the string
#3.  find the minimum element after conveerting string into list
#4. find the no. of spaces present in the string without using functions and methods

String= input("Enter the string: ")
char_list=[]
for ch in String:
    char_list.append(ch)
print("List of individual characters:", char_list)
print("Length of the string:", len(String))
min_char = String[0]
for ch in String:
    if ch < min_char:
        min_char = ch
print("Minimum character in the string:", min_char)
space_count = 0
for ch in String:
    if ch == ' ':
        space_count += 1
print("Number of spaces in the string:", space_count)
