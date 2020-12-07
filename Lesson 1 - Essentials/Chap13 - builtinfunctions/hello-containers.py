#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from collections import Counter 
x = (1,2,3,4,5)
a = (11,22,33,44,55)

y = list(reversed(x))
sumof = sum(y)

print(x)
print(y)
print(sumof)
print(max(y))

# check if any is not 0, hence true
print(any(y))
print(all(y))

y = (0,0,0)
print (any(y))
print (all(y))

print(*zip(x, a))

x = ['cat', 'dog', 'rabbit', 'raptor', 'raptor', 'raptor']
print(*enumerate(x))

seen = Counter(x)
print(*seen, *seen.values())