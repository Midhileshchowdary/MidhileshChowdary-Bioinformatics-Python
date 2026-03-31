a=10
b=5
try:
    d=a/b
    print(d)
    print('Inside try')
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print('Inside else')
finally:
    print('Inside Finally')
print("Rest of code")