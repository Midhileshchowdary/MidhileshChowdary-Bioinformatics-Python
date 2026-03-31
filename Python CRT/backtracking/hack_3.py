'''str=input("ENTER THE ALPHABET STRING : ")
Str=str.lower()
List=Str.split()
count = {}
for i in Str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
for i in sorted(count):
    print(f"{i}: {count[i]}")
'''
s=input()
res=''
for ch in s:
    if ch not in res:
        res+=ch+str(s.count(ch))
print(res)