''' write py prog to check  the user entered string is a panagram or not'''
str=input("Enter the string: ").upper()
str=str.replace(" "," ")
print(f"User entered string: {str}")
str=sorted(str)
str="".join(str)
print(str)
if str in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print("Panagram")
else:
    print("Not a panagram")