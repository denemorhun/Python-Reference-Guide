# try out the Python queue functions

from collections import deque

# TODO: create a new empty deque object that will function as a queue

queue = deque()

# TODO: add some items to the queue
queue.append(5)
queue.append(8)
queue.append(11)
queue.append(14)
queue.append(19)

# TODO: print the queue contents

print(queue)

# TODO: pop an item off the front of the queue
x = queue.popleft()
y = queue.pop()

print("results are here:")
print(queue)
print("popped item from left " + str(x))
print("popped item from right " + str(y))
print(queue)