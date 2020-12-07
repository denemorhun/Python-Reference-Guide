#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = [ 1, 2, 3, 4, 5 ]

# x = range(5)

# start, and, step
# x = range(2,50,5)

# dictionary
x = {'one':1,'two':2,'three':3}

#for i in x:
   # print('i is {}'.format(i))

for k, v in x.items():
    print("key: {} values:  {}".format(k,v))