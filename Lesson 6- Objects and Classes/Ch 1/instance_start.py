# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        # add properties
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret"

    def __str__ (self):
        return f"The book {self.title} written by {self.author} has {self.pages} and is {self.price}"

    # create instance methods

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - self._discount
        return self.price

    def setDiscount(self, percent):
        self._discount = self.price*(percent/100)
        
# create some book instances
b1 = Book("War and Peace", "leo tolstoy", 700, 9.99)
b2 = Book("The Catcher in the Rye", "Salzinger", 150, 10.99)

# print the price of book1
print(b1.price)
print(b1.getPrice())

# try setting the discount
print("Normal price", b2.getPrice())
b2.setDiscount(20)
print("After discount is applied", b2.getPrice())

# TODO: properties with double underscores are hidden by the interpreter
# print(b2.__secret)

# if we append _Book in front of it we can access the secret
print(b2._Book__secret)