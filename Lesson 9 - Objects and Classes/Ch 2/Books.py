# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Price: ", self.price)

#title=input()
#author=input()
#price=input()
title = "The Alchemist"
author = "Paulo"
price = "248"
new_novel=MyBook(title,author,price)
new_novel.display()

