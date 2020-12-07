# deque objects are like double-ended queues

import collections
from collections import deque as dq
import string

def main():
    
    # TODO: initialize a deque with lowercase letters
    lcase = dq(string.ascii_lowercase)
    for elem in lcase:
        print(elem.upper(), end=',', flush=True)
    # TODO: deques support the len() function

    print ('\nlength of the dq', len(lcase))

    enum_list = []
    # TODO: deques can be iterated over
    for elem in lcase:
        enum_list.append(elem)
       
    print(*enumerate(enum_list))

    # TODO: manipulate items from either end

    lcase.append('1')
    lcase.appendleft('0')

    x = lcase.pop()
    y = lcase.popleft()

    print('number of elem d', lcase.count('d'))
    print('number of elem a', lcase.count('a'))
    print(x, y)

    # TODO: rotate the deque
    lcase.rotate(20)
    print(*lcase)

if __name__ == "__main__":
    main()
