""" Two Names, One Shirt """

class shirt:

    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True

# create couple of shirts

red = shirt()
# olivia refers to this shirt as crimson, but it's the same object
crimson = red 

# they would have the same object ids
# print(id(red))
# print(id(crimson))

red.make_dirty()

print(red.clean)
print(crimson.clean)

red.make_clean()

print(red.clean)
print(crimson.clean)
