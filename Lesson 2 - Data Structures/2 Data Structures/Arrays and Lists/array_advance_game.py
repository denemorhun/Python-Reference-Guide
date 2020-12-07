#!/usr/bin/env python3

'''
# Given an array of non-negative integers
# Each number represents the maximum to advance in the array.
# Return whether we can reach the end of the array or not
# 
# Algorithm:
# Iterate through each entry in array.
# Track furthest we can reach from entry ( A[i] + i )
# If for some “i” before the end is the furthest that we can reach, we can’t reach the last index. Otherwise, the end is reached.
# i : index processed
# Furthest possible to advance from “i”: A[i] + i

[3,3,1,0,2,0,1]

Example: 

i = 0
furthest_reached = max(furthest_reached, A[0] + 0) = 3
'''

def array_advance_game(arr):

    i = 0
    furthest_reached = 0
    last_idx = len(arr) - 1


    while i <= furthest_reached and furthest_reached < last_idx:
        # Furthest possible to advance from “i”: A[i] + i
        furthest_reached = max (furthest_reached, arr[i] + i)
        print("furthest reached", furthest_reached, " at i", i)
        i += 1


    return True if furthest_reached >= last_idx else False

def main():

    arr1 = [3,3,1,0,2,0,1]
    arr2 = [3,2,0,0,2,0,1]
    arr3 = [0,0,0,0]
    arr4 = [2,4,1,1,0,2,3]

    print(arr1, array_advance_game(arr1))
    print(arr2, array_advance_game(arr2))
    print(arr3, array_advance_game(arr3))
    print(arr4, array_advance_game(arr4))


if __name__ == '__main__': main()
