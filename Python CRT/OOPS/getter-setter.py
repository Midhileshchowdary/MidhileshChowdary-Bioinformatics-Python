class Mobile:
    def __init__(self,P,C,B):
        self.Price=P
        self.Colour=C
        self.Brand=B
        print("Object is created")
    #Mutator
    def Set_Details(self):
        self.Colour="Blue"
    #Accessor
    def Get_Details(self):
        print(f"Colour : {self.Colour}")
        print(f"Price : {self.Price}")                      
        print(f"Brand : {self.Brand}")
M1=Mobile(12000,'Black','Samsung')
M1.Get_Details()
print("After Modifying the data : ")
M1.Set_Details()
M1.Get_Details()
