#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7
print('x is {}'.format(x))
print(type(x))

y = 'seven'
print('y is ', y.count('e'))
print(type(y))

# using type
tup1 = (1, 2.4, "three", 4)
print(type(tup1[0]))

dic = {"one":1, "two":2, "three":3}

print(type(dic))

# how about using ID to compare objects? 
tup2 = (1, 2.4, "three", 4)

id1 = tup1[0]
id2 = tup2[0]
tup2 = (1, 2.4, "three", 4)

# use it to compare
if id1 is id2:
    print("The same {} {}",  id1, id2 )
else:
    print("Not same {} {}",  id1, id2 )