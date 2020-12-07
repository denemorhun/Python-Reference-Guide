#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def f1(input_f):
    print(f"this is f1")
    def f2():
        print("this is before the func_call")
        input_f()
        print("this is after the functional call")
    return f2
    
@f1
def f3():
    print("this is f3")

# assign f1 to x and call x()
# x=f1(f3)
# x()

# f3 becomes a wrapper and its not available in original form
f3()