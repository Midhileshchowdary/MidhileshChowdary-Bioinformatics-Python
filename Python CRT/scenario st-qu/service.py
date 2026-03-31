'''
to create a customer service by adding customer into the queue. one the customer is served he has to be removed from the queue
'''
from collections import deque
queue=deque()
queue.append('Customer 1')
queue.append('customer 2')
queue.append('Customer 3')
print("Customer list",queue)
first=queue.popleft()
print("Customer served and removed : ",first)
print("After removing served customer",queue)
if not queue:
    print("list is empty")
else:
    print("list is not empty")
print("next customer to be served : ",queue[0])