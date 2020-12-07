#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    input_string = "aaaaaabbbbbb"
    a = set("We're gonna need a bigger boat.")
    
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    c = set("aaaaaa")
    d = set(input_string)
    # print the letters in set, should be unique
    print_set("a" + str(a))
    print_set("b" + str(b))
    print_set("c" + str(c))
    print("d-c" + str(d-c))
    # we can also see d | c, d & c, 

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
