# without parameters example 1
class Mobile:
    def __init__(self):
        print("Mobile Constructor called..")
realme=Mobile()

# without parameters example 2
class Mobile:
    def __init__(self):
        self.model='Realme X'
        self.price=25000
    def show_model(self):
        print("Model : ",self.model)
        print("Price : ",self.price)
realme=Mobile()
realme.show_model()

# with parameter
class Mobile:
    def __init__(self,Colour): # constructor format fixed
        self.Colour=Colour
def Display_Details(self):
    print(f"Mobile Colour : {self.Colour}")
M1=Mobile("Cyan Blue")
Display_Details(M1)