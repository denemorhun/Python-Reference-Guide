#!/usr/bin/env python3

"""
Counterfeit Currency 

A counterfeit currency printer is operating in country XYZ, and all of the banks must try to identify the bad currency. Every note has a serial number that can be used to determine whether it is valid. The serial number also can be used to determine the denomination of the note. A valid serial number will have the following characteristics: 
1. There are 10 to 12 characters 
2. The first 3 characters are distinct uppercase English letters 
3. The next 
4. characters represent the year the note was printed and will always be between 1900 and 2019 inclusive. 
4. The next characters represent the currency denomination and may be any one of (10.20, 50, 100, 200, 500, 1000) 
5. The last character is an uppercase English letter 

Given an array of serial numbers, determine the value of the valid currency For example, serial numbers for notes are shown below. 
"""


import os, sys
from sys import is_finalizing

def countCounterFeit(serialNumber):

    # initialize
    valid_denominators = [10, 20, 50, 100, 200, 500, 1000]
    total = 0

    for serial in serialNumber:

        is_serial_valid = True

        # check whether length requirments are met
        if len(serial) > 10 or len(serial) < 12:
        
            # Validate 3 Letter code
            # splice the first three chars
            letter_code = serial[:3]
        
            # verify first three chars are uppercase and type char
            if not letter_code.isupper() or not letter_code.isalpha():
                is_serial_valid = False
                print("First three chars not uppercase or chars")

            # verify first three chars are distinct
            if len(letter_code) != len(set(letter_code)):
                is_serial_valid = False
                print("First three chars not distinct")

            # Validate year
            # Splice chars 3 to 7 for year
            year = serial[3:7]

            # Verify year consists of digits
            if not year.isnumeric():
                is_serial_valid = False
                print("Year has none digit value")
            else:
                year = int(year)
                # Verify year falls within requirements
                if year < 1900 or year > 2019:
                    is_serial_valid = False
                    print("Year falls out of range")

            # Verify denominator is valid
            # Remove last character
            denom = serial[:-1:]

            # remove first 7 characters
            denom = denom[7:len(denom)]

            if not denom.isnumeric():
                is_serial_valid = False
                print("Denom is not numeric")
            else:
                denom = int(denom)

            if denom not in valid_denominators:
                print("Denom is invalid")
                is_serial_valid = False

            # Verify last char is char
            last_char = serial[-1]
    
            if not last_char.isalpha() or not last_char.isupper():
                is_serial_valid = False
                print("last character is not upper case or char")

            if is_serial_valid is True:
                total += int(denom)

            print(f"Result: {serial} is valid, total {total}" if is_serial_valid else f"Result: {serial} is invalid\n")

    return total

if __name__ == '__main__': 

    fptr = open(os.path.join(sys.path[0], "counterfeitinput.txt"))
    serialNumber = []
    for serialNumber_item in iter(fptr.readline, ''):
        serialNumber.append(serialNumber_item.strip())

    result = countCounterFeit(serialNumber)

    print(result)

