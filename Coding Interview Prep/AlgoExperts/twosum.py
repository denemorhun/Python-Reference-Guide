# 2 sum in an array

'''
Given an array of DISTINCT integers, return pair that sums up to a target

assume one pass, and 1 solution, and no repetitions. 


Approach:
We can do this with 2 for loops, which is very inefficient. We could cycle through the array and check if x in first loop equals (target - y ) in second loop. 
'''

# return the two numbers from array that equal to target
def get_numbers(array, targetSum):
   
    if len(array) == 0:
        return []

    print(f"Target sum: {targetSum}")

    # check if value x = target - y, and y is already in a hashtable
    # if we don't use the hashtable, scenarios such as 1, 2, 5, 4, 6 fail, 
    # 5, 5 is returned.

    my_dict = dict.fromkeys(array)
    print(my_dict)

    for x in array:
        if  (targetSum - x) in my_dict.keys() :#and targetSum-x != x:
            return [x, targetSum - x]
            
    return []

if __name__ == '__main__':

    # sorted array
    print (f'Sorted array values are {get_numbers([1, 3, 5, 6, 10],16)} ')

    # non sorted array
    print (f'Non sorted array values are {get_numbers([1, 3, 5, 10, 6],16)} ')

    # array with negative values
    print (f'values are {get_numbers([1, 3, 5, -10, 26],16)} ')

    # array with no succesful values
    print (f'values are {get_numbers([1, 3, 5, -10, 27],16)} ')

    # array with repetition number equaling targetSum i.e. 8
    print (f'values are {get_numbers([1, 4, 5, 8],16)} ')
