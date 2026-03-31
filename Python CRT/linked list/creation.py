class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_font(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def show(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")
l1=LinkedList()
l1.insert_font(5)
l1.insert_font(15)
l1.insert_font(20)
l1.show()