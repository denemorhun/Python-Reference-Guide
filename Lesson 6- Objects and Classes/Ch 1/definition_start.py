# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions

# Create a basic Book class


class Book():
    # constructor
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return "This book is called: " + self.title

# create instances of the class

book1 = Book("For whom the bell tolls")
book2 = Book("Brave New World")

#  print the class and property

print(book1)
print(book2)

print(book1.title)
print(book2.title)
