#write a python  program to read a string as input from the user ( including spaces ) and print the string by trimming the spaces 
Input=input("Enter the string : ")
print(f"User entered string :{Input}")
Str_List=Input.split()
string=''.join(Str_List)
print(string)




