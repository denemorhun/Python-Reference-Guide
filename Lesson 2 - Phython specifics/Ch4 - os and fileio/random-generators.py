#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import random
import os

def main():

    print(os.urandom(25).hex())
    # posix

    x = random.randint(1, 100)
    print(x) 

    y = list(range(10)) 
    random.shuffle(y)
    print(y)

if __name__ == '__main__': main()
