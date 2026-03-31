'''
    write a python program to read stringf as input form user and print the count of
    1. uppercase vowels
    2. lower case vowels
    3. uppercase consonents
    4. lower case consonents
'''
Str=input("Enter the string : ")
u_vowels,l_vowels,u_consonents,l_consonents=0,0,0,0
for ch in Str:
    if(ch.isalpha and ch.isupper):
        if ch in 'AEIOU':
            u_vowels+=1
        else:
            u_consonents+=1
    if(ch.isalpha and ch.islower):
        if ch in 'aeiou':
            l_vowels+=1
        else:
            l_consonents+=1
print(f"Lower case vowel count : {l_vowels} ")
print(f"upper case vowel count : {u_vowels} ")
print(f"Lower case consonents count : {l_consonents} ")
print(f"upper case vowel count : {u_vowels} ")


Str=input("Enter the string : ")
u_vowels,l_vowels,u_consonents,l_consonents=0,0,0,0
for ch in Str:
    if((ch>='A' and ch>='Z')):
        if ch in 'AEIOU':
            u_vowels+=1
        else:
            u_consonents+=1
    if((ch>='a' and ch>='z')):
        if ch in 'aeiou':
            l_vowels+=1
        else:
            l_consonents+=1
print(f"Lower case vowel count : {l_vowels} ")
print(f"upper case vowel count : {u_vowels} ")
print(f"Lower case consonents count : {l_consonents} ")
print(f"upper case vowel count : {u_vowels} ")