#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import math 

def main():


    directions = ['left','right','up','down']
    directions = sorted(directions)
    # for i in range(len(directions)):
    #     print(i, directions[i])

    print("enumarate version")
    for i,j in enumerate(directions):
        print(i,j)

    print(", can be used to create a tuple")

    for i in enumerate(directions):
        print(i)

    directions = enumerate(directions)

    for i,j in directions:
        print(j)


def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
