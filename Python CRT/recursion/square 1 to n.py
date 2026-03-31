# write py prog to print square num from 1 to n using recursion

N=int(input("Enter number : "))
def Square(N):
    if N==0:
        return
    Square(N-1)
    print(N*N)
Square(N)
