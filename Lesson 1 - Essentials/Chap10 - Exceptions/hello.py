#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys 

def main():
    try:
        print('Hello, World.')
        x = 5 + "ooo"
    except ValueError: 
        print("I caught a value error")
        x = 2
    except ZeroDivisionError: 
        x =0 
    except:
        print(f"unknown error: {sys.exc_info()[1]}")
    else:
        print("good job")

if __name__ == '__main__': main()
