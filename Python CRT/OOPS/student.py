'''
write a py prog to create a student class and declare the properties as student name, student id, branch, percentage, age, paasing out year, certificate count,
create 10 objects and initialize the values using mutator method and access them using accessor method
(NoTE: You have to intialize the values without using constructors)
'''
class Student:
    def set_details(self,StuName,StuId,Branch,Percent,age,POY,Certificate):
        self.Student_Name=StuName
        self.StudentID=StuId
        self.Branch=Branch
        self.Percentage=Percent
        self.Age=age
        self.POY=POY
        self.Certificate=Certificate
    def set_modify_details(self):
        self.Student_Name=input("Enter Name")
        self.StudentID=input("Enter ID")
        self.Branch=input("Enter Branch")
        self.Percentage=input("Enter Percent")
        self.Age=input("enter age")
        self.POY=input("Enter POY")
        self.Certificates=input("Enter certificate")
    def get_details(self):
        print(f"Student Name : {self.Student_Name}")
        print(f"Student ID : {self.StudentID}")
        print(f"Branch : {self.Branch}")
        print(f"Student Percentage : {self.Percentage}")
        print(f"Student Age : {self.Age}")
        print(f"Year Of Passing : {self.POY}")
        print(f"Certificate Count : {self.Certificate}")
S1=Student()
S1.set_modify_details()
S1.set_details()
S1.get_details()
S1.set_modify_details()
S1.get_details()


