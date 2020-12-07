#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():

    x = ('meow', 'grrr', 'purr','miyav')
    # parametrize the contents of tuple otherwise only 1 object is passed
    kitten(*x)
    # prints the whole contents with *
    print(*x)

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()
