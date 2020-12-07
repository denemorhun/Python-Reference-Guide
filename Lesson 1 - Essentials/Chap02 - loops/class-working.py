#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Dog:

    sound = 'Woof'
    walking = 'walks like a dog'

    def bark(self):
        print(self.sound)

    def walk(self):
        print(self.walking)

        

def main():

    hera = Dog()
    hera.bark()

if __name__ == '__main__': main()
