'''
py prog to take length of queue as input from the user and add the elements by using enque method and print the elements present in the queue and
remove the elements one by one from the queue and check whether the queue is empty or not and print the front peek and rear peek
'''
class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,n):
        for i in range (n):
           item=input("Enter element : ")           
           self.items.append(item)
    def is_empty(self):
        return len(self.items)==0
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        removed = self.items.pop(0)
        print(f"Dequeued: {removed}")
    def peek_front(self):
        if self.is_empty():
            print("Queue is empty")
        print(f"peek front : {self.items[0]}")
    def peek_rear(self):
        if self.is_empty():
            print("Queue is empty")
        print(f"peek rear : {self.items[-1]}")
    def display(self):
        print(f"elements : {self.items}")
queue=Queue()
length=int(input("enter size of queue : "))
queue.enqueue(length)
queue.display()
queue.peek_front()
queue.peek_rear()
queue.dequeue()
queue.display()
queue.dequeue()
queue.display()
queue.dequeue()
queue.display()