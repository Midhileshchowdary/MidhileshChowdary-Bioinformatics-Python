# write a python program to reverse the list of numbers without using reverse method
Num=[11,99,22,88,33,77,44,100,55,66]
print(Num[::-1])
# write a python program to sort a list of numbers without using sort method.
for i in range (0,len(Num)):
    for j in range (i,len(Num)):
        if Num[i]>Num[j]:
            temp=Num[i]
            Num[i]=Num[j]
            Num[j]= temp
print(Num)