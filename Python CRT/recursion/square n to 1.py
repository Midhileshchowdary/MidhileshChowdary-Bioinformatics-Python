# write py prog to print square num from n to 1 using recursion

N=int(input("Enter numbers "))
def NaturalNum(N):
    if N!=0:
        print(N*N)
        return NaturalNum(N-1)
NaturalNum(N)