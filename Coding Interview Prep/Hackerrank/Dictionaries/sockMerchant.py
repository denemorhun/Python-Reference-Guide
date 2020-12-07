'''Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

output:

number of pairs

------------
Sample Input
------------
9
10 20 20 10 10 30 50 10 20

Sample Output
------------
3
------------

    #my approach
    # create dict array with all the unique values
    # store each unique numberid as a key
    # do an integer divide by // 2 on values
    # increment num_pairs by v // 2

'''

#!/bin/python3

import math
import os
import random
import re
import sys
import collections
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    # put the contents of the array into a dict with unique keys
    sock_ids = Counter(ar)
    num_pairs=0
    
    # loop through the dict counting occurrences,
    # if > 2, do integer division // and add value

    for v in sock_ids.values():
            num_pairs += v // 2

    print(sock_ids.values())
   
    return num_pairs

if __name__ == '__main__':

    ar = (9, 10, 20, 20, 10, 10, 30, 50, 10, 20) # 3 pairs
    ar2 = (1, 1, 1, 1, 1, 1, 2, 2, 2, 2) # 5 pairs
    ar3 = (2, 3) # 0 pairs

    result = sockMerchant(len(ar), ar)
    result2 = sockMerchant(len(ar2), ar2)
    result3 = sockMerchant(len(ar3), ar3)
    print ('Number of pairs {} '.format(result3))