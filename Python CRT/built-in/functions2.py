'''# write a py program to read the string as input from the user
# 1. reverse the string 
# 2. covert into lower case
# 3. convert into upper case
# 4. covert characters of string to lower case if it is in upper case
# 5. covert characters of string to upper case if it is in lower case
# 6. check if the string is starting with letter a 
# 7. print the count of character a from the given string
# 8. replace all p's to letter j
'''
Str=input("Enter the string : ")
print(Str[::-1])
print(Str.lower())
print(Str.upper())
print(Str.swapcase())
print(Str.startswith('P'))
print(Str.count('P'))
Str=Str.lower()
print(Str.replace('p','j'))
print(Str.capitalize())

Str="python programs"
print(Str.capitalize())
print(Str.title())
print(Str.casefold())
print(Str.startswith('P'))
print(Str.find('O'))
print("Hi".center(15,"*"))
