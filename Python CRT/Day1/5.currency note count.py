#write a python program to read the amount as input from the user and print the number of notes required in indian currency dimension?
a=int(input("Enter the amount:"))
print (f"2000---",a//2000)
a=a%2000
print (f"500---",a//500)
a=a%500
print (f"200---",a//200)
a=a%200
print (f"100---",a//100)
a=a%100
print (f"50---",a//50)
a=a%50
print (f"20---",a//20)
a=a%20
print (f"10---",a//10)
a=a%10
print (f"5---",a//5)
a=a%5
print (f"2---",a//2)
a=a%2
print (f"1---",a//1)