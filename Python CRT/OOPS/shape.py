'''
write a py prog to create a shape class and declare the properties as lenghtm bredth, height
1) calculate the area of square using instance methods
2)check whether the sides of squares are equal or not using instance methods
3) calculate the perimeter of square using instance methods
4) find the diagnols of square using instance object
5) find the side length of square using instance methods
'''
class Shape:                            
    def __init__(self,l,b,h):
        self.length=l
        self.breadth=b
        self.height=h
    def area(self):
        print("Area of the shape : ",self.length*self.breadth)
    def square(self):
        print("The shape is square or not : ",self.length==self.breadth)
    def perimeter(self):
        print("The Perimeter of the shape  : ",(2 *(self.length+self.breadth)))
    def diagonal(self):
        print("The Diagnol of permimeter", (self.length**2 + self.breadth**2) ** 0.5 )
    def sidesquare(self):
        print( (self.length) if self.length==self.breadth else "Not Square" )                   
S1=Shape(5,5,1)
S1.area()
S1.square()  
S1.perimeter()
S1.diagonal()
S1.sidesquare()
print("Another Shape")
S2=Shape(5,6,1)  
S2.area()
S2.square()  
S2.perimeter()
S2.diagonal()
S2.sidesquare()