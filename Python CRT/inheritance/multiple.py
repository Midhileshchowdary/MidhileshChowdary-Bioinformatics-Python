#Multiple level inheritance
class Java:
    def __init__(self):
        pass
    @staticmethod
    def functionalities():
        print("Java used has  Cross-Platform Compatability")
class C:
    def __init__(self):
        pass
    @staticmethod
    def functionalities():
        print("C has a wide range of applications")
class Python(Java,C):
    def __init__(self):
        pass
    @staticmethod
    def functionalities():
        print("Python  has both wide range of applications and  Cross-Platform Compatability") 
Java.functionalities()
C.functionalities()
Python.functionalities()