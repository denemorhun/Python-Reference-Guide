# Remove Dupes from sorted array

'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5.

Approach:

    Use the first pointer to point the position which element is being stored to, and the other pointer to iterate the elements. If the current element and the previous element are different, store the current element in the first pointer and move one. Make exception for the first element and in case element is only 0 or 1 size.
    '''

def removeDuplicates(nums):
   
    if len(nums) == 0:
        return 0

    # real solution

    # idx = 0
    # for i in range(len(nums)):
    #     print("i",i)
    #     if i==0 or nums[i] != nums[i-1]:
    #         nums[idx] = nums[i]
    #         idx += 1
    #         print("idx",idx)
    # return idx

    # dict and list solution

    nums = list(dict.fromkeys(nums))
    return len(nums)


if __name__ == '__main__':

    ar = [9, 10, 10, 10, 20, 20, 30, 50, 50, 50] # 3 pairs
    ar2 = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2] # 5 pairs
    ar3 = [1, 2, 2, 2, 2, 3,3,3,3,3] # 0 pairs

    result = (removeDuplicates(ar))

    print ('Length of array without dupes {} '.format(result))