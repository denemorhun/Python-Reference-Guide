''' Given an array-  divide odd and even numbers '''

import collections
import os
import datetime
import sys
from collections import Counter

def divide_even_odd(numbers):

    if numbers is None:
        return None

    list_even = []
    list_odd = []

    for number in numbers:
        if number % 2 == 0:
            list_even.append(number)
        else:
            list_odd.append(number)

    return [list_even, list_odd]

def main():
    input =  [1 , 4, 6, 3, 99, 55, 33, 22]

    print(divide_even_odd(input))


if __name__ == '__main__': main()
