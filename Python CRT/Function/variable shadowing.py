
'''
---------------------Variable Shadowing---------------------
local variable  dominant over global variable  when both have same variable name is declared
'''

Greet="Good Morning"
def Display():
    Greet="Good Afternoon"
    print(Greet) # within function ------local variable-------
Display()
print(Greet) #-----Global variable-------