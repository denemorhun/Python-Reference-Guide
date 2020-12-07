'''
#!/usr/bin/env python3
# Find the smallest absolute difference from 2 arrays
# Each array will only return 1 item
# for example: -5, 5, absolute difference is 10
# -1, -4, absolute difference is 3


# Soution #
# start by sorting the two arrays. 
# put a pointer at beginning of both arrays
# evaluate the abs difference of the pointer-numbers
# if the difference is 0, that is the closest pair
# if no 0's are found, increment the pointer of the smaller number
# Continue until we get a pair with difference of 0 or we reach length of array

# Assume we have unique solutions for smallest value

'''

def smallest_difference_between_lists(arrayOne, arrayTwo):

    # sort the arrays 
    arrayOne.sort()
    arrayTwo.sort()
    
    i, j = 0, 0

    # hash map that stores the values 
    differences = {}

    # keep searching till the indexes reach the length of the arrays
    while i < len(arrayOne) and j < len(arrayTwo):

        # Goal is to find the minimum difference between two numbers
        difference = abs(arrayOne[i] - arrayTwo[j])

        numberOne = arrayOne[i]
        numberTwo = arrayTwo[j]

        # current pair with the smallest difference
        pair = [numberOne, numberTwo]

        # since solutions are unique, we can use difference as keys.
        differences[difference] = pair

        # difference would be zero, smallest difference found
        if numberOne == numberTwo:
            return pair

        # Only increment the smaller numbers' index, to reduce the difference between the numbers. 
        elif numberOne < numberTwo:
            i += 1
        elif numberOne > numberTwo:
            j += 1
			
    # return the pair with the smallest difference from the dictionary
    return differences[min(differences)]

def main():

    arr1 = [-1, 5, 10, 20, 28, 3]
    arr2 = [26, 134, 135, 15, 17]
    print(smallest_difference_between_lists(arr1, arr2))

    print(smallest_difference_between_lists([10, 0, 20, 25, 2200], [1005, 1006, 1014, 1032, 1031]))

if __name__ == '__main__': main()
