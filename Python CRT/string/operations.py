#length
str="Python"
print(f"Length of {str} is {len(str)}")
#accessing without index
for i in str:
    print(i,end=" ")




#accessing with index
for i in range(len(str)):
    print(str[i],end=" ")

# Slicing
str1="Python Program"
print(str1[1:6])
print(str1[0:1])
print(str1[7:11])
print(str1[7:10])
print(str1[10::])
print(str1[2:6])
print(str1[::-1])
print(str1[-9::-1])
print(str1[-1:-8:-1])
print(str1[-4:-8:-1])
print(str1[-7:-12:-1])
print(str1[-1:-5:-1])
print(str1[-1:-4:-1])
#concatenation
a="Hello"
b="world"
c=a+b
print(c)
#repetition
"$"*7
str1="Students"
print(str1*5)
print(str1[0:4]*3)
#Membership operators
print('a' in 'apple')
print('a' not in 'apple')

print("apple" < "banana")
print("abc" == "ABC")