#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():

    directions = ['left','right','up','down']
    directions = sorted(directions)

    print("enumarate version")
    for i,j in enumerate(directions):
        print(i,j)

    print("Enumerate can be used to create a tuple")
    directions = enumerate(directions)
    for i in directions:
        print(i)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
