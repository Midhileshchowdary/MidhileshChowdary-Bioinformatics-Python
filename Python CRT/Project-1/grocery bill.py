'''
write a python program to declare a list of grocery items and read the input from user from 1 to 5
1. to display of the list of grocery items in sorted way
2. to take input from user and add items to the cart
3. to view the cart items
4. to update the quantity or item present in the cart
5. Geberate a bill including the item names, quantity, price, and if the final bill amount is greater than 1000 the user will get 
10% discount
if the user purchases any item more than 10kgs reduce the amount of 1kg from that particular items price.
if the user purchases any particular item give buy 1 get 1
add 25% gst to the overall bill and print the bill
'''
cart_item=[]
cart_quantity=[]
cart_price=[]
total_bill=0
grocery_items=['Rice','Masala','Mango','chia','sesame']
price=[100,300,100,150,250]
while(True):
    print("*************** MENU ***************")
    print("1. Display the Grocery items")
    print("2. Select the item and Add to cart")
    print("3. View the items in the cart")
    print("4. Update the item or quantity")
    print("5. Generate Bill")
    print("6. Exit")
    print("------------------------------------")
    
    Choice=int(input("Enter your choice : "))
    if(Choice>=1 and Choice<=6):
        if(Choice==1):
            sortedlist=sorted(grocery_items)
            print(f"The Grocery List ----{sortedlist}")
        elif(Choice==2):
            Required_items=int(input("Enter the number of items required: "))
            i=1
            while(i<=Required_items):
                item= input(" Enter the item required: ")
                if item in grocery_items:
                    cart_item.append(item)
                    quantity=int(input("Enter in KG: "))
                    cart_quantity.append(quantity)
                    index= grocery_items.index(item)
                    cart_price.append(price[index])
                else:
                    print("Not Available")
                i+=1
        elif(Choice==3):
            if(len(cart_item)>0):
                print("The items in the cart are: ")
                print(cart_item)
            else:
                print("Cart Is Empty!!!")
        elif(Choice==4):
            print("1. Update Item")
            print("2. Update Quantity")
            Choose=int(input("Enter your choice : "))
            if(Choose>=1 and Choose<=2):
                if(Choose==1):
                    item1= input(" Enter the item that you want to replace: ")
                    item2= input(" Enter the item that you want to add: ")
                    if item1 in cart_item:
                        if item2 in grocery_items:
                            index1=cart_item.index(item1)
                            index2=grocery_items.index(item2)
                            cart_item[index1]=item2
                            cart_price[index1]=price[index2]
                            print("Item Updated")
                        else:
                            print("the item that you want to add is not present in the Grocery List")
                    else: 
                        print("The item that you want to replace is not present in cart")
                elif(Choose==2):
                    item3= input(" Enter the item that you want to change the quantity: ")
                    if item3 in cart_item:
                        index3=cart_item.index(item3)
                        new_quantity=int(input("Enter the new quantity in KG: "))
                        cart_quantity[index3]=new_quantity
                        print("Quantity updated.")
                    else:
                        print("Item not in cart")
        elif(Choice==5):
            print("--------------BILL--------------")
            for i in range(len(cart_item)):
                itm=cart_item[i]
                qty=cart_quantity[i]
                pr=cart_price[i]
                amount=pr*qty
                print(f"{itm} -- {qty}KG = {amount}")
                if qty>10:
                    print("1kg dicount")
                    amount-=pr
                offer_quantity= qty*2
                print("Buy 1 get 1 Free : ",offer_quantity)
                total_bill+=amount
                if total_bill>1000:
                    print("10% Discount applicable..")
                    total_bill-=total_bill*0.10
                else:
                    print("No Discount")
                print("the total bill without Gst :",total_bill)
                total_bill+=total_bill*0.25
                print("the total bill with Gst :",total_bill)
                print("Thankyou")
                break
        else:
            print("Thank You")
            break
    else:
        print("Invalid - Input")