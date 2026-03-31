# write a py program  to read astring as input from the user and split the string into 3 equal halves using slicing
s = input("Enter a string: ")
n = len(s) // 3  # Integer division ensures equal parts
first_part = s[:n]
second_part = s[n:2*n]
third_part = s[2*n:]
print("First part:", first_part)
print("Second part:", second_part)
print("Third part:", third_part)