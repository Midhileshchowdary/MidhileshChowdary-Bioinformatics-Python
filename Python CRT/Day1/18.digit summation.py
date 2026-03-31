#write a python program to read the integer value as input from user and find the summation of digits
Num=int(input("Enter the number: "))
temp= Num
digit_sum=0
while(Num!=0):
    digit_sum+=(Num%10)
    Num//=10
print(f"The sum of digits of {temp} is {digit_sum}.")