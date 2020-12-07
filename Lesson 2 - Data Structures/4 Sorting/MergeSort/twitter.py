#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countStudents' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY height as parameter.
#

def countStudents(height):
    # Write your code here

    srt = sorted(height)
    if srt == height:
        return 0
        cnt = 0
        i = 0
        while i < len(height):
            if height[i] != srt[i]:
                cnt+=1
            i+=1
        return cnt
    print(cnt)

    if __name__ == '__main__':
       fptr = open(os.environ['OUTPUT_PATH'], 'w')
    height_count = int(input().strip())
    height = []
    for _ in range(height_count):
        height_item = int(input().strip())
        height.append(height_item)
    result = countStudents(height)
    fptr.write(str(result) + '\n')
    fptr.close()
