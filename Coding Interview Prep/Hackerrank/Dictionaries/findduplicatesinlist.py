# find duplicates in a given list

import collections
from collections import Counter

def findDupesInList(arr):

    if arr is None:
        return []

    count = {}

    i = 0 

    # if the value is in the hashmaps, increment
    # else, set it 1
    for item in arr:
        if item not in count.keys():
            count[item] = 1
        else:
            count[item] += 1
        
    for i, j in count.items():
        print(i, j)


if __name__ == '__main__':
        input = ['a', 'b', 'c', 'd', 'd', 'd']

        findDupesInList(input)
