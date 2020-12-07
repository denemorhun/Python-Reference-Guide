#!/usr/bin/env python3
# Find the intersection of 2 arrays


def return_intersection(arr1, arr2):

    arr1 = set(arr1)
    arr2 = set(arr2)

    return list(arr1.intersection(arr2))

def return_difference(arr1, arr2):

    arr1 = set(arr1)
    arr2 = set(arr2)

    return list(arr1.difference(arr2))


def main():

    arr1 = [1, 2, 7, 3, -3, 0, 55]
    arr2 = [1, 7, -3, 0, 55, 88]

    print(return_intersection(arr1, arr2))

    print(return_difference(arr1, arr2))

if __name__ == '__main__': main()
