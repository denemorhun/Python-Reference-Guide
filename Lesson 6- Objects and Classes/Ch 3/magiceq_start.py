# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, other):
  
        if (not isinstance(self, Book) or not isinstance(other, Book)):
            raise ValueError("Comparison is not a book to book.")
            pass
        else:
            return (self.title == other.title and self.author == other.author and self.price == other.price)


    # TODO: the __ge__ establishes >= relationship with another obj

    def __ge__(self, other):
  
        if (not isinstance(self, Book) or not isinstance(other, Book)):
            raise ValueError("Comparison is not a book to book.")
            pass
        else:
            return self.price >= other.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, other):
  
        if (not isinstance(self, Book) or not isinstance(other, Book)):
            raise ValueError("Comparison is not a book to book.")
            pass
        else:
            return self.price <= other.price

    def __str__(self):
        return f"title: {self.title} author: {self.author} price: {self.price}"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
print("b1 == b3", b1 == b3)
# print("b1 == denem", b1 == "denem")
print("b1 != b2", b1 != b2)
print("b1 == b2", b1 == b2)

# TODO: Check for greater and lesser value
print("b1 >= b3", b1 >= b3)
print("b1 >= b2", b1 >= b2)
print("b1 <= b2", b1 <= b2)

# TODO: Now we can sort them too


books = []
books.append(b1)
books.append(b2)
books.append(b3)
books.append(b4)

# method 1 sorted by price
for book in sorted(books):
    print(book)

print(*sorted(books))

# method 2 using list comprehension
books.sort()
print({book.title:book.price for book in books})