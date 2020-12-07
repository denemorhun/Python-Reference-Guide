#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

myArr = [1, 2, 3, 5]

for index, elem in enumerate(myArr):
    if (index+elem)%2 == 0:
        print(index,elem)

