Num=[]
for i in range(1,11):
    Num.append(i)
print(Num)
#list comprehension method
New=[i for i in range(1,11)]
print(New)
'''
write py prog to print even numbers from 1 to n using list comprehension
'''
n=int(input("Enter the number"))
New=[i for i in range(1,n) if i%2==0]
print(New)