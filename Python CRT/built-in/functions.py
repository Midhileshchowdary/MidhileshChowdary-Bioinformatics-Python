# write a python program to read a string as input from user and print
#1.count of uppercase letters
#2. count of lower case letters
#3. count of numeric value 
#4. count of special charaters
Str=input("Enter the string : ")
Uppercase_alpha=0
lowercase_alpha=0
Numeric=0
spl_char=0
for ch in Str:
    if ch.isupper():
        Uppercase_alpha+=1
    elif ch.islower():
        lowercase_alpha+=1
    elif ch.isdigit():
        Numeric+=1
    else:
        spl_char+=1
print(f"Count of Upper case letters : {Uppercase_alpha}")
print(f"Count of Lower case letters : {lowercase_alpha}")
print(f"Count of Numeric values : {Numeric}")
print(f"Count of Special letters : {spl_char}")