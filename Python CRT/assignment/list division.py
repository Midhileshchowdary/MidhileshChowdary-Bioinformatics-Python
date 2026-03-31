'''
7. Divide All Elements of a List by a Number
Write a program that accepts a list of numbers and a divisor. Divide each element of the list by the divisor and return a new list with the 
results. Ensure the divisor is not zero.
'''
Num=[]
Result=[]
len=int(input(("Enter the length of list : ")))
for i in range(len):
    temp=int(input("Enter the number :"))
    Num.append(temp)
while(True):
    divisor=int(input("Enter the divisor : "))
    if(divisor==0):
        print("Enter divisor value more than 0.")
    else:
        for i in Num:
            value=i//divisor
            Result.append(value)
        print(Result)
    break

