# write py prog to print lower case alphabets from a to z using recursion
def print_lowercase(ch=ord('a')):
    if ch > ord('z'):
        return
    print(chr(ch), end=' ')
    print_lowercase(ch + 1)

print_lowercase()
