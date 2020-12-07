#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import os
import sys

def main():
    # f = open('lines.txt')
    f = open(os.path.join(sys.path[0], "lines.txt"))
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()
