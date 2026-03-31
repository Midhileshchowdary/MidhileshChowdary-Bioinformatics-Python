
'''
read a password as input from user and check whether it is valid or invalid
atleast 1 uppercase 1 lower case, numeric, spl
'''
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
if (Uppercase_alpha>=1 and  lowercase_alpha>=1 and Numeric>=1 and spl_char>=1):
    print("valid")
else:
    print("Invalid")

