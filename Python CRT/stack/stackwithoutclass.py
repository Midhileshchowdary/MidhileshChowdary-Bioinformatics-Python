from collections import deque
stack=deque()
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushing",stack)
top=stack.pop()
print("Popped element: ",top)
print("Stack after popping",stack)
if not stack:
    print("stack is empty")
else:
    print("stack is not empty")
print("top element : ",stack[-1])