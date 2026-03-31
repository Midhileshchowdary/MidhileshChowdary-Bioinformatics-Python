class Father:
    def __init__(self):
        pass
    @staticmethod
    def work():
        print("Hardworking father")
class Son(Father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def work():
        print("Enjoy")
Father.work()
Son.work()