'''
write py prog to read year as input from user and check weather it is leap year or not
'''
year=int(input("Enter year :"))
if((year%4==0 and year%100!=0)or (year % 400==0)):
    print("Leap Year")
else:
    print("Not a leap year")