
# try out the Python stack functions
# https://www.w3schools.com/python/python_lists.asp

# TODO: create a new empty stack

stack = []
# TODO: push items onto the stack using append function
stack.append("orange")
stack.append("apple")
stack.append("blackcurrant")

# TODO: print the stack contents
print(stack)

# TODO: pop an item off the stack
stack.remove("blackcurrant")
x = stack.pop()

print(x)