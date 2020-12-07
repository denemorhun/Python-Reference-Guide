''' '''

import collections
import os
import datetime
import sys
from collections import Counter

def isValid(input) -> bool:

    input = list(input)

    if list is None:
        return True

    if len(input) == 0: 
        return "True"
    else: 
        return "False"

def main():
    input = ""

    result = isValid(input)

    print("Yes" if result else "No")

if __name__ == '__main__': main()
