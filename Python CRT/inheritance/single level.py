class vehicle:
    def __init__(self):
        print("I'm Vehicle class constructor.")
    @staticmethod
    def Start():
        print("Vehicle is started.")
class Car(vehicle):
    def __init__(self):
        super().__init__()
        print("I'm the car class constructor.")
    @staticmethod
    def Start():
        print("Car is started.")
C1=Car()
C1.Start()


