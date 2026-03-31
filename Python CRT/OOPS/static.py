class Mobile:
    def __init__(self):
        print("Object is created")
    @staticmethod
    def Display():
        print("I'm a Class Method")
        print("I will work irrespective of object creation")
Mobile.Display()
