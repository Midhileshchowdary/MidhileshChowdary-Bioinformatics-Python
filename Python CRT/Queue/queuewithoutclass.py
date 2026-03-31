from collections import deque
queue=deque()
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueuing",queue)
first=queue.popleft()
print("Dequeued element : ",first)
print("Queue after deqqueuing",queue)
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")
print("Front element : ",queue[0])