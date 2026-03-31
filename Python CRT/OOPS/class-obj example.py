'''
write a py program to create a mobile class and declare the states of mobile as colour,price,brand,seies,version,features,storage,battery capacity
RAM,processor
create 10 objects and iniatlise using constructor print the details of the individual object using function.
'''
class Mobile:
    def __init__(self,Colour,Price,Brand,Series,Version,Features,Storage,BatteryCapacity,Ram,Processor): # constructor format fixed
        self.Colour=Colour
        self.Price=Price
        self.Brand=Brand
        self.Series=Series
        self.Version=Version
        self.Features=Features
        self.Storage=Storage
        self.BatteryCapacity=BatteryCapacity
        self.Ram=Ram
        self.Processor=Processor
def Display_Details(self):
    print(f"Mobile Colour : {self.Colour}")
    print(f"Mobile Price : {self.Price}")
    print(f"Mobile Brand : {self.Brand}")
    print(f"Mobile Series : {self.Series}")
    print(f"Mobile Version : {self.Version}")
    print(f"Mobile Features : {self.Features}")
    print(f"Mobile Storage : {self.Storage}")
    print(f"Mobile BatteryCapacity : {self.BatteryCapacity}")
    print(f"Mobile Ram : {self.Ram}")
    print(f"Mobile Processor : {self.Processor}")
    print("-------------------")
M1=Mobile("Cyan Blue",25000,"IQOO","Z7","1","50MP","512GB","5000MPH","8GB","Snapdragon")
M2=Mobile("Black",35000,"Vivo","T5","2","Dualcam","512GB","5000MPH","8GB","Intel")
M3=Mobile("White",45000,"Samsung","S27","3","ai","512GB","5000MPH","8GB","Meditech")
M4=Mobile("Grey",55000,"GooglePixel","7A","4","pixelcam","512GB","5000MPH","8GB","Snapdragon")
M5=Mobile("Blue",65000,"Nokia","10","5","50MP","512GB","5000MPH","8GB","Intel")
M6=Mobile("Peach",15000,"Oppo","A3","6","50MP","512GB","5000MPH","8GB","Meditech")
M7=Mobile("Pink",75000,"Redmi","9PR0","7","50MP","512GB","5000MPH","8GB","Snapdragon")
M8=Mobile("RoseGold",95000,"Oneplus","12A","8","50MP","512GB","5000MPH","8GB","Snapdragon")
M9=Mobile("Silver",35000,"Realme","M1","9","50MP","512GB","5000MPH","8GB","Snapdragon")
M10=Mobile("cement",15000,"Xiomi","12","10","50MP","512GB","5000MPH","8GB","Snapdragon")
Display_Details(M1)
Display_Details(M2)
Display_Details(M3)
Display_Details(M4)
Display_Details(M5)
Display_Details(M6)
Display_Details(M7)
Display_Details(M8)
Display_Details(M9)
Display_Details(M10)