'''
-----------------Anonymous or Lambda function-----------------
1. A function without name 
SYNTAX:--> lambda argument_list : expression

        example:-

        lambda x,y:x+y

        x,y----> argument list
        : -----> represents begining of the function
'''
#single argument
res=lambda a:print(a)
res(10)
res=lambda a:print(a)
res("Hello")
# double argument
add=lambda x,y:(x+y)
print(add(2,5))
