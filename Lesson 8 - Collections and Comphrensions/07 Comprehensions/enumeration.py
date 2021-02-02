#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():

    print('Play around with enumerate')

    animals = ['dog', 'cat', 'mouse', 'horse']

    # # normal for loop 
    # for animal in animals:
    #     print(animal)

    # # enumerated animal loop
    # for numeric, animal in enumerate(animals, start=1):
    #     print(animal, numeric)

    for i, animal in enumerate(animals, start=1):
        if i % 2 == 0:
            print(i, animal)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
