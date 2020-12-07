# implementing queues with Python
class Queue(object):
    def __init__(self):
        # create an empty list
        self.items = []

    def put(self, item):
        self.items.insert(0, item)

    # remove the first element inserted
    def pop(self):
        if not self.is_empty():
            x = self.items[-1]
            del(self.items[-1])
            return x

    # Check if q is empty and return true
    def is_empty(self) -> bool:
        return len(self.items) == 0

    # check what the value to be popped is
    def peek(self):
        if not self.is_empty():
            return self.items[-1]


    def __len__(self):
        return self.size()

    def size(self):
        if not self.is_empty():
            return len(self.items)

