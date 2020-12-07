# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __call__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # the __call__ method can be used to call the object like a function
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        print(f"{self.title} by {self.author}, costs {self.price}")

# TODO: call the object as if it were a function


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# b3 = Book()
# b3(("War", "Tzu", 39.95))

b1(b1.title, b1.author, b1.price)

b1("1984", "George Orwell", 39.99)
print(b1)