# 2 sum in an array

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Approach:

    Use the first pointer to point the position which element is being stored to, and the other pointer to iterate the elements. If the current element and the previous element are different, store the current element in the first pointer and move one. Make exception for the first element and in case element is only 0 or 1 size.

    MUST BE SORTED.

    # do brute force first
    # i=0
    # j=1

    # for i in range(len(nums)):
    #     for j in range(len(nums)-1):
    #         if nums[i] + nums[j] == target:
    #             return [i+1,j+1]
    #         else:
    #             j +=1
    #     i += 1

    # return None
    '''

def getIndices(nums, target):
   
    if len(nums) == 0:
        return None

    # two pointer solution using a hashmap

    # convert the array into a hash map with enumeratioin
    nums = enumerate(nums)
    print(f"Target {target}")

    # create a dictionary with [number, index]    
    seen = {} 
    for index, num in nums:
       # calculate the complement for each number
        complement = target - num

        # if the complement is already in dict exit 
        if complement in seen:
            print(f'Num: {num}, idx: {index} | complement: {complement},idx: {seen[complement]}')
            #return the complement's index and the index of the number 
            return [seen[complement], index]
        else:
            # assign an index to the seen number and proceed
            seen[num] = index        

if __name__ == '__main__':

    ar = [9, 10, 10, 10, 20, 20, 30, 50, 50, 50] # 3 pairs
    ar2 = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2] # 5 pairs
    ar3 = [1, 2, 2, 2, 2, 3,3,3,3,3] # 0 pairs
    ar4 = [1,2,4,5,6,10,13,18]

    result = getIndices((ar4),16)

    print ('indices are {} '.format(result))