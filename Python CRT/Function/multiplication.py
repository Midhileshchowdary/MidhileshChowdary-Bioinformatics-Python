# write py prog to build a function which prints the multiplication table of n 
def multiplication(Num):
    i=1
    for i in range (1,11):
        print(f"{Num} * {i} =",Num*i)
        i=i+1
multiplication(5)
