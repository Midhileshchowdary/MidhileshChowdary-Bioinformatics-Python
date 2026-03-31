'''write a python program taken from the user to chcek whether the taken input is anagram or not'''
str1=input("Enter the First String: ")
str2=input("Enter the Second String: ")
print(f"First String: {str1}")
print(f"Second String: {str2}")
str1=str1.replace(" "," ")
str2=str2.replace(" "," ")
if len(str1)==len(str2):
    if sorted(str1)==sorted(str2):
        print("Anagram")
    else:
        print("Not Anagram")
