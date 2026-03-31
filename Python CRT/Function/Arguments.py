'''
 Arguments types ---- 2 
 1. Actual Arguments
 2. Formal Arguments
 ---> Actual Arguments Types:-
    A) Positional Arguments
    B) Keyword Arguments 
    C) Default Arguments 
    D) Variable Length Arguments
    E) Keyword Variable Length Arguments
 '''
#------------Arguments--------------
def add(x,y):  # FORMAL ARGUMENTS --- Definition parameters
    c=x+y
    print(c)
add(10,20) #10,20 ACTUAL ARGUMENTS --- Call Parameters
#--------------Positional Arguments------
def pw(x,y):
    z=x**y
    print(z)
pw(5,2)
#--------------Keyword Arguments------
def show(name,age):
    print(name,age)
show(name="Kumar",age=62)
#------------Default Arguments-------
def show(name,age=27):
    print(name,age)
show(name="Kumar",age=62)
#-----------Variable Length Arguments-------
def Display(*x):
    x=x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]
    print(x)
Display(10,10,10,10,10,10,10)
#-----------Variable Length Arguments-------
def add (**num):
    z=num('a')+num('b')+num('c')
    print(z)
add(a=5,b=2,c=1)