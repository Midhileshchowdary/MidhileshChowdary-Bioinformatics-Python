class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node=Node(10)
print(node.data)
node1=Node(20)
print(node1.data)
node2=Node(30)
print(node2.data)
current=node
current.next=node1
node1.next=node2
while current:
    print(current.data,end="->")
    current=current.next
print("None")