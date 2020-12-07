#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import math 

def main():
    seq1 = range(11)
    seq2 = [x*2 for x in seq1]

    # get all x not divisible by three:
    seq3 = [x for x in seq1 if x % 3 != 0]
    print_list(seq2)
    print_list(seq3)

    # get all the squared for x
    seq4 = [(x, x**2) for x in range(10) if is_power_of_two(x)]
    print_list(seq4)

    # get a set 
    seq5 = set(x for x in 'superduper' if x not in 'pd')
    print(seq5)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

def is_power_of_two(n):
    return (n != 0) and (n & (n-1) == 0)

if __name__ == '__main__': main()
