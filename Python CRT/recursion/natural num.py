#1 to n
n = int(input("Enter the n value: "))
def Natural_Num(n):
    if n == 0:
        return
    Natural_Num(n - 1)  
    print(n)
Natural_Num(n)
#method call
N= int(input("Enter the n value: "))
i=0
def NaturalNum(N,i):
    i=i+1
    if N==0:
        return
    NaturalNum(N-1,i)
    print(f" {i} Method call")
NaturalNum(N,i)
#1 to n
def NaturalNum(N):
    if N==0:
        return
    NaturalNum(N-1)
    print(N)
NaturalNum(N)
#n to 1
def NaturalNum(N):
    if N!=0:
        print(N)
        return NaturalNum(N-1)
NaturalNum(N)
