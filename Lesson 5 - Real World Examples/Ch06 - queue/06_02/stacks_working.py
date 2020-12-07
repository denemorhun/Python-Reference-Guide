""" A Stack of Bills to Pay """

# create a list to use as the stack
stack = list()

# add some bills to the stack
stack.append('bill1')

# start again
stack.clear()

# what happens if you try to add duplicates, no issue
stack.append("bill1")
stack.append("bill1")
stack.append("bill1")
stack.append("bill1")

# remove the top bill to pay it
while len(stack) > 0:
    print(stack.pop())


# Populate the stack
stack.append("billa")
stack.append("billb")
stack.append("billc")

# now we've made the stack fifo
stack.reverse()

# remove bills from top to bottom
print(stack.pop())
print(stack.pop())

# add two more bills to the stack
stack.append('billd')
stack.append('bille')

# not pump out the whole stack -> it should be lifo
while len(stack) > 0:
    print(stack.pop())

# stack.pop() # causes Indexerror exception
