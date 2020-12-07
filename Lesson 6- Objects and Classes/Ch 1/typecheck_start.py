# Python Object Oriented Programming by Joe Marini course example
# Checking class types and instances


class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title + str(type(self))


class Newspaper:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name + str(type(self))


# Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# TODO: use type() to inspect the object type

print(b1)
print(b2)
print(n1)
print(n2)


# TODO: compare two types together

if type(b1) == type(n2):
    print("books and newspapers are the same")
else:
    print("books are not newspapers")

print(type(b1) == type(b2))
print(type(n1) == type(n2))
print(type(n1) == type(b1))

# TODO: use isinstance to compare a specific instance to a known type

print("B1 is a book " if isinstance (b1, Book) else "b1 is not a book")
print("B1 is an object " if isinstance (b1, object) else "b1 is not an object")
