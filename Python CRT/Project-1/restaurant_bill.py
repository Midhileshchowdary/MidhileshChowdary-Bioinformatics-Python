'''
1. write a py program to display a menu of food items (list)
2. create a tuple of prices with respect to food items list
3. read the input from the user for ordering the food including the quantity 
    if it exists in the menu ---- confirm order
    if not print a message order something else 
4. while billing, phone number, feedback,read tip amount
5. add 18% gst to the bill and print the bill (if bill>0) 
'''
print("*************** MENU ***************")
List=['Dosa','Idli','Puri','vada','upma']
price= (20,10,30,40,30)
print(List)
Required_items=int(input("Enter the number of items required: "))
i=1
total_bill=0
while(i<=Required_items):
    item= input(" Enter the item required: ")
    if item in List:
        quantity=int(input("number of items: "))
        index= List.index(item)
        bill=price[index]*quantity
        print("CONFIRM ORDER")
        if (bill>0):
            bill+=bill*(18/100)
            print(bill)
            total_bill+=bill
    else:
        print("Order Something else")
    i+=1
phone=int(input("Enter phone number : "))
count=0
while(phone!=0):
    phone=phone//10
    count+=1
if(count==10):
    print("THANK YOU")
else:
    print("Wrong number")
feedback=input("Give feedback : ")
tip= int(input("Enter the tip amount : "))
total_bill+=tip
print("the total bill is :",total_bill)
