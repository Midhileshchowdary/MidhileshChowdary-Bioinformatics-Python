#write python program to read an integer value as input from user and find number of digits present in that particular number
Num=int(input("Enter Number : "))
temp= Num
count=0
while(Num!=0):
    Num=Num//10
    count+=1 #count=count+1
print(f"{temp} has {count} digits")