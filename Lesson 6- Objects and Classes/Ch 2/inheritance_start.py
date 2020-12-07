# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance
class Publication():
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Book(Publication):
    def __init__(self, title, author, pages, price):
        self.author = author
        self.pages = pages
        super().__init__(title, price)

    def __str__(self):
        return f" Obj type: {type(self)}, Title: {self.title}, author: {self.author}, price: {self.price}, pages: {self.pages}"

class Periodical(Publication):
    def __init__(self, title, publisher, price, period):
        self.period = period
        self.publisher = publisher
        super().__init__(title, price)


    def __str__(self):
        return f" Obj type {type(self)}, title: {self.title}, publisher: {self.publisher}, price: {self.price}, period: {self.period}"

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

# print(b1.author)
print(b1)
print(m1)
print(n1)
# print(n1.publisher)
# print(b1.price, m1.price, n1.price)
