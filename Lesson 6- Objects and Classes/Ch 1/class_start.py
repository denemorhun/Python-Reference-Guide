# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods

class Book:
    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # double-underscore properties are hidden from other classes
    # this list private to the Book class
    __booklist = None

    # create a static method
    @staticmethod
    def getBookList():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    # create a class method that returns booktype. 
    # This is different that self, which is an instantiation of the class
    # non-static method in java
    @classmethod
    def getBookType(cls):
        return cls.BOOK_TYPES
        
    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (booktype not in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} not found ")
        else:
            self.booktype = booktype

    def __str__(self):
        return f"Book is called {self.title} and booktype is {self.booktype}"


# access the class attribute
print("Booktypes are", Book.BOOK_TYPES)

# Create some book instances
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "PAPERBACK")
# b3 = Book('Title 4', 'Comic')

# TODO: Use the static method to access a singleton object
# create and return 
thebooks = Book.getBookList()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)


