#write a python program to read an integer value as input and print the number of even digits and odd digits present in that particular number
Num=int(input("Enter the number: "))
even=0
odd=0
while(Num!=0):
    a=Num%10
    if(a%2==0):
        even+=1
    else: odd+=1
    Num//=10
print(f"The even digit count is {even}. The odd digit count is {odd}")