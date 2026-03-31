class Graduation:
    def __init__(self):
        pass    
    @staticmethod
    def Graduate():
        print("Congratulations you are a graduate now.")
#first sub class
class BI(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("You are BI Graduate")
#Second sub class
class CSE(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("You are Cse Graduate")
#Third sub class
class IT(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("You are IT Graduate")
Graduation.Graduate()
BI.Graduate()
CSE.Graduate()
IT.Graduate()