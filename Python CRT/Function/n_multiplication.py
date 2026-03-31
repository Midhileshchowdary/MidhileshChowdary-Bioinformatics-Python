# write py prog to build a function which prints the multiplication table from 1 to  n 
def n_multiplication(Num):
    i=1
    for i in range (1,Num+1):
        print(f"The Multiplication table of {i}")
        for j in range (1,11):
            print(f"{i} * {j} = ",i*j)
n_multiplication(3)