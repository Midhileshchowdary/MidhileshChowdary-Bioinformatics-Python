class GrandFather:
    def __init__(self):
        pass
    @staticmethod
    def properties():
        print("100 acres of land.")
class Father(GrandFather):
    def __init__(self):
        super().__init__()
    @staticmethod
    def properties():
        print("50 acres of land.")
class Yourself(Father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def properties():
        print("Data Analyst")
GrandFather.properties()
Father.properties()
Yourself.properties()