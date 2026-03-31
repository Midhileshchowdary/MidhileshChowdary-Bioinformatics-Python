# write py prog to check whether the user given number is prime or not using functions (return... keyword)
def prime(Num):
    count=0
    for i in range(1,Num+1):
        if(Num%i==0):
            count+=1
    if (count==2):
        print(f"{Num} is  prime number")
    elif(count==1):
        print(f"{Num} is neither prime nor composite.")
    else:
        print(f"{Num} is not a prime number")
prime(5)
prime(6)
prime(1)
# write py prog to build a function which prints the multiplication table of n 