'''
to read the length of the string as input from user and print all binary strings of length n 
'''
def generate_binary_no_backtrack(n):
    result = '0' * n
    print(result)

generate_binary_no_backtrack(3)
#with backtracking
print("with backtracking")
def generate_binary_backtrack(n, current=""):
    if len(current)==n:
        print(current)
        return
    #choose 0
    generate_binary_backtrack(n,current+'0')
    #choose 1
    generate_binary_backtrack(n,current+'1')
generate_binary_backtrack(3)