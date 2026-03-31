'''
write a py prog to read the month number as input from user and check weather it is valid month or not
'''
Month=int(input("Enter the month number :"))
if (Month>=1 and Month<=12):
    print ("Valid month number")
else:
    print("In-Valid month number")
