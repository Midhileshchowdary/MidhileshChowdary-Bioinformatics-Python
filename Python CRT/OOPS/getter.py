class Employee:
    def __init__(self,empname,empID,designation,salary,deptname):
        self.empname=empname
        self.empID=empID
        self.designation=designation
        self.salary=salary
        self.deptname=deptname
    def Get_details(self): #setter
        print(self.empname)
        print(self.empID)
        print(self.designation)
        print(self.salary)
        print(self.deptname)
E1=Employee("Scott","EMP101","Data Analyst",25000,"Deployment")
E1.Get_details()
