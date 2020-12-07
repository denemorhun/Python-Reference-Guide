'''
Given an array of DISTINCT integers, Validate a second array is a subset
Main idea here is to check matches in only 1 direction
'''

# return the two numbers from array that equal to target
def isValidSubsequence(array, sequence):

    isSub = False

    pos = 0

	# outer loop is the sequence
    for i in range (len(sequence)):
        isSub = False
		# inner loop is the Main array
        for j in range(pos, len(array)):
            if sequence[i] == array[j]:
				# once we hit a match set subSet to True
                isSub = True
				# move the position past last found match in main array
                pos = j+1
                break
            else:
                pos+=1
            
    return isSub


if __name__ == '__main__':

    # sorted array
    print (f'Sorted array values are {isValidSubsequence([1, 3, 5, 6, 10],[3, 10])} ')

    # non sorted array
    print (f' Non - Sorted array values are {isValidSubsequence([1, 3, 6, 5, 10],[3, 10])} ')
   
    # # array with negative values
    # print (f' Negative array values are {isValidSubsequence([1, 3, -6, 5, 10],[3, 10])} ')
   
    # # array with no succesful values - none
    print (f' Unsuccesful array values are {isValidSubsequence([1, 3, -6, 5, 10],[3, 11])} ')

    # # array that failed

    print (f' Should be succesful array values are {isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[22, 25, 6])} ')
   
    # # array with repetition number equaling targetSum i.e. 8 - none
