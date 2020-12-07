'''
Given an array of DISTINCT integers, Validate a second array is a subset
Main idea here is to check matches in only 1 direction
'''

# return the two numbers from array that equal to target
def isValidSubsequence(array, sequence):

   # sequence index
    i = 0
    # array index
    j = 0 

    while i < len(sequence) and j < len(array):
        if sequence[i] == array[j]:
			# once we hit a match move index of sequence to next
            i+=1
        # move the index of main array regardless of match
        j+=1
            
    # if we have reached the end of the sequence, it's valid
    return i == len(sequence)
    

if __name__ == '__main__':

    # sorted array
    print (f' Sorted array values are {isValidSubsequence([1, 3, 5, 6, 10],[3, 10])} ')

    # non sorted array
    print (f' Non - Sorted array values are {isValidSubsequence([1, 3, 6, 5, 10],[3, 10])} ')
   
    # array with negative values
    print (f' Negative array values are {isValidSubsequence([1, 3, -6, 5, 10],[3, 10])} ')
   
    # array with no succesful values - none
    print (f' Unsuccesful array values are {isValidSubsequence([1, 3, -6],[3, 11])} ')

    # array that failed

    print (f' Should be succesful array values are {isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[22, 25, 6])} ')
   
    # array with repetition number equaling targetSum i.e. 8 - none

    # array with no succesful values - none
    print (f' Unsuccesful array values are {isValidSubsequence([1, 1, 6,1],[1,1,1,6])} ')

    # array with identical values - none
    print (f' identical array values {isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[5, 1, 22, 25, 6, -1, 8, 10])} ')
