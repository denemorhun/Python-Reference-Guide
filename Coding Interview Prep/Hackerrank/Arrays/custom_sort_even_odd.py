#!/usr/bin/env python3

"""
In an array, we can swap the elements at any two indices in a single operation called a move.
 
For example, if our array is a = [17, 4, 8], we can swap a[0] = 17 and a[2] = 8 to get a = 
[8, 4, 17] in a single move. We want to custom sort an array such that all of the even elements
are at the beginning of the array and all of the odd elements are at the end of the array.

Note : the order of elements within even or odd doesn't matter.

Constraints :
2 <= n <= 10^5
1 <= a[i] <= 10^9, where 0 <= i <= n
it is guaranteed that array a contains at least one even and one odd element.

"""

# Algorithm: Swapping is not required - counting the number of swaps is enough. 
# 
# 1. Count the number of evens in array (since evens are chosen to be in the beginning)
# 2. Scroll through the number of max evens in the array (which is less than array length)
# 3. If any odds are encountered, it's time for a swap
# 4. Increment swaps


import os, sys

def moves(arr):

    # min number of swaps needed
    swaps = 0
    countEven = 0
    
    # obtain number of evens to scroll through in second pass
    for number in arr:
        if isEven(number):
            countEven += 1
            print("countEven", countEven)
    
    for i in range(countEven):
        value = arr[i]

        # If an Odd value is encountered, a swap is needed
        if isOdd(value):
            swaps += 1

    return swaps

def isOdd(num):
    return (num % 2 == 1)

def isEven(num):
    return (num % 2 == 0)


if __name__ == '__main__': 

    fptr = open(os.path.join(sys.path[0], "custom_sort_even_odd.txt"))
    numbers = []
    for number_item in iter(fptr.readline, ''):
        numbers.append(int(number_item.strip()))

    result = moves(numbers)

    print(result)
