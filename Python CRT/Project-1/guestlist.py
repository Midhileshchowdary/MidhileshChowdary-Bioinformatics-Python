'''
write a python program to:
1. Add confirmed guests to a list. 
2. Remove a guest who cancels
3. Check if a friend is in the list
4. Sort and print the final list 
'''
Guest_List=[]
while(True):
    print("*************** MENU ***************")
    print("1. Add the Guest")
    print("2. Remove the Guest who cancels")
    print("3. Check if the Guest is attending party or not.")
    print("4. View the Final Guest List.")
    print("5. Exit")
    print("------------------------------------")
    Choice=int(input("Enter your choice : "))
    if(Choice>=1 and Choice<=5):
        if(Choice==1):
            GuestName=input("Enter the Guest Name : ")
            Guest_List.append(GuestName)
            print(f"{GuestName} is added to the Guest List....!")
        elif(Choice==2):
            CancelGuest=input("Enter the Cancel Guest Name :")
            if CancelGuest in Guest_List:
                Guest_List.remove(CancelGuest)
                print(f"{CancelGuest} is removed from the Guest List....!")
            else: 
                print(f"{CancelGuest} is not in the Guest List....!")
        elif(Choice==3):
            CheckGuest=input("Enter the Check Guest Name :")
            if CheckGuest in Guest_List:
                print(f"{CheckGuest} is attending the Party....!")
            else:
                print(f"{CheckGuest} is not attending the Party....!")
        elif(Choice==4):
            if(len(Guest_List)==0):
                print("Guest List is Empty" )
            else: 
                Guest_List.sort()
                print("Hurray Here's Your Final Guest List!!!!")
                print(Guest_List)
        else:
            print("Enjoy Your Party....")
            break
    else:
        print("Invalid - Input")