#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))

    print(sys.platform)
    # darwin

    print(os.name)
    # posix

    print(os.getenv('PATH'))
    # /bin:/usr/sbin:/sbin:/Library/Frameworks/Python.framework/Versions/3.8/bin

    print(os.getcwd())
    # Current directory: /Users/dorhun/Desktop/Trainings/Python

if __name__ == '__main__': main()
