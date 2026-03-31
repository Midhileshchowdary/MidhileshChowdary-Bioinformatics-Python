class Stack:
    def __init__(self):
        self.Stack=[]
    def push(self,data):
        self.Stack.append(data)
        print("Element is appended.")
    def isempty(self):
        if len(self.Stack)==0:
            return True
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            self.Stack.pop()
            print("Element is Removed")
    def peek(self):
        Len=len(self.Stack)
        print(f"Peek element is {self.Stack[Len-1]}")
    def Rev(self):
        self.Stack.reverse()
        for i in self.Stack:
            print(i)
    def display(self):
        print(self.Stack)
    def size(self):
        Len=len(self.Stack)
        print(f"Size of Stack {Len}")
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.display()
stack.pop()
stack.display()
stack.peek()
stack.Rev()
stack.size()
