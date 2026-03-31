'''
write a py program to create a product class declare the states of the class as productname, productid, price,GST,mfdate,expdate
1) Create 5 objects initialize it using parameterized constructor and access them using instance method 
2) Declare mutator methods as set.objects given and change the values of their properties using mutators methods and print it 
'''
class Product:
    def __init__(self,Pname,Pid,Price,GST,mfdate,expdate):
        self.Product_Name=Pname
        self.Product_ID=Pid
        self.Product_Price=Price
        self.GST=GST
        self.Manufacture_Date=mfdate
        self.Expiry_date=expdate
        print("Details of Product :")
    def Set_Details(self):
        self.Product_Name="Dark Chocolate"
        self.Product_ID="cashew1"
        self.Product_Price=110
        self.GST="10%"
        self.Manufacture_Date="15/6/25"
        self.Expiry_date="16/6/26"
    def Get_Details(self):
        print(f"Product Name : {self.Product_Name}")
        print(f"ProductID : {self.Product_ID}")
        print(f"Product Price : {self.Product_Price}")
        print(f"GST : {self.GST}")
        print(f"Manufacture_Date : {self.Manufacture_Date}")
        print(f"Expiry_date : {self.Expiry_date}")
P1=Product("5-star","plain1",10,"5%","14/6/25","14/5/26")
P1.Get_Details()
print("--------------------")
print("After Modifying the details of product : ")
print("--------------------")
P1.Set_Details()
P1.Get_Details()
'''
write a py prog to create a student class and declare the properties as student name, student id, branch, percentage, age, paasing out year, certificate count,
create 10 objects and initialize the values using mutator method and access them using accessor method
(NoTE: You have to intialize the values without using constructors)
'''
