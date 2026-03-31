#write a python program to read an integer value as input and find number of 0's present in the user entered number.
Num=int(input("Enter the number: "))
temp=Num
count=0
while(Num!=0):
    a=Num%10
    if(a==0):
        count+=1
    Num//=10
print(f"The number of 0's in {temp} is {count}")