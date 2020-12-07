#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
def generate(start=1, stop=10, step=1):

    i = start
    # generator
    while i <= stop:
        yield i
        i += step
        
def main():

    # for value in generate(start,stop,step):
    for value in generate():
        print(value)

if __name__ == '__main__': main()