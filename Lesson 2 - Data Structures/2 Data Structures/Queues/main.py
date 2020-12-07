# Driver code

from queue import Queue

if __name__ == '__main__':

    q = Queue()
    q.put(5)
    q.put(8)
    q.put(11)
    q.put(14)
    q.put(19)

    # TODO: print the queue contents
    print(q.items)

    x = q.pop()
    print(x)

    print(q.items)

    print("Next item to be popped is:", q.peek())

    print("The size of the queue is:", q.size())

    # # TODO: pop an item off the front of the queue
    # x = queue.popleft()
    # y = queue.pop()

    # print("results are here:")
    # print(queue)
    # print("popped item from left " + str(x))
    # print("popped item from right " + str(y))
    # print(queue)