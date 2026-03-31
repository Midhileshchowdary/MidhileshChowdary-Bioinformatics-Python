'''
read string as input from user and replace all vowels with 0
'''
str=input("Enter the string : ")
result=""
for ch in str:
        if ch in 'AEIOUaeiou': result+= '0'
        else: result+=ch
print(result)
