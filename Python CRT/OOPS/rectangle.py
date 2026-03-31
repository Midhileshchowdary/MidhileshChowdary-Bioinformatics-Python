'''
write py program to create a rectangle class and initialize the variables length and bredth using constructor and access the values using mutator 
methods 
'''
class rectangle:
    def __init__(self,L,B):
        self.Length=L
        self.Bredth=B
    def Set_Details(self):
        self.Length=5
        self.Bredth=4
    def Get_Details(self):
        print(f"Length : {self.Length}")
        print(f"Bredth : {self.Bredth}")
R1=rectangle(3,2)
R1.Get_Details()
print("After Modifying ")
R1.Set_Details()
R1.Get_Details()

                                                                                                                                    