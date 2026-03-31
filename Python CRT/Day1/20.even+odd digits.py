#write a python program to read an integer value as input and find the summation of even digits and odd digits present in that particular number
Num=int(input("Enter the number: "))
even=0
odd=0
while(Num!=0):
    a=Num%10
    if(a%2==0):
        even+=a
    else: odd+=a
    Num//=10
print(f"The sum of even digit is {even}. The sum of odd digit is {odd}")