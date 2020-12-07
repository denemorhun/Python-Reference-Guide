# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects

class Book:
    def __init__(self, title, price, Author=None):
        self.title = title
        self.price = price

        self.Author = Author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append((chapter))

    def getBookPageCount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount

        return f"Page count is {result}"

class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f'{self.fname} {self.lname}'

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

    def __str__(self):
        return f'{self.name} {self.pagecount}'


aq = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, aq)

print(b1.Author)

# we can cast the object 
b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 1", 143))

for chapter in b1.chapters:
    print(chapter)

print(b1.getBookPageCount())



