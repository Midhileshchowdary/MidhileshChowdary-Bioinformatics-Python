'''
write a python program to take name as input including prefix(MR or Miss)
print the gender classification of the name on basis of prefix 


'''
Str=input(" enter the name: ")
male=[]
if Str.startswith("Mr."):
    print("Male")
elif Str.startswith("Ms."):
    print("Female")
else:
    print("Erong input")
    