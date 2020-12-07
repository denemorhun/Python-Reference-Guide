# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str="No Title"
    author: str="No Authorr"
    pages: int=0
    price: float=field(default=10.0)

b1 = Book()
print(b1)

b2 = Book("War and Peace", "Leo Tolstoy", 1225)
b3 = Book("The Catcher in the Rye", "JD Salinger", 234)
print(b2, b3)