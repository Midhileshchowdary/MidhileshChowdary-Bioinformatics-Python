class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def AddNode(self,data):
        N_node=Node(data)
        N_node.next=self.head
        self.head=N_node
    def delete_front(self):
        if self.head:
            self.head=self.head.next
    def Display_List(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
L1=LinkedList()
L1.AddNode(25.89)
L1.AddNode(99.56)
L1.AddNode(76.54)
L1.AddNode(100)
L1.Display_List()
L1.delete_front()
L1.Display_List()