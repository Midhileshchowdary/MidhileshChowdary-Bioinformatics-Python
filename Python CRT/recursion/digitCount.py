'''
count number of digits in a given number
'''
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)
n=8903
print(count_digits(n))