#!/usr/bin/env python3
# Find the 2nd and 3rd largest item in an array
# sort it
# return the len - 2 for 2nd largest, etc. 

def find_2nd_highest(arr):

    arr = sorted(arr)

    print("2nd highest number is:", arr[len(arr)-2])
    print("3rd highest number is:", arr[len(arr)-3])

def find_2nd_smallest(arr):

    arr = sorted(arr)

    print("2nd smallest item in list is", arr[1])

def main():

    arr1 = [1, 2, 7, 3, -3, 0, 55]
    arr2 = [1, 2, 7, 3, -3, 0, 55, 88]
    find_2nd_highest(arr1)
    find_2nd_highest(arr2)

    find_2nd_smallest(arr1)

if __name__ == '__main__': main()
