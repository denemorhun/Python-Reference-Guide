''' Two Sum Less Than K

' Given an array A of integers and integer K,
' return the maximum S such that there exists i < j 
' with A[i] + A[j] = S and S < K. 
' If no i, j exist satisfying this equation, return -1. 

   def twoSumLessThanK(A, K):
      ans = -1
      if len(A)==1:
         return -1
      for i in range(len(A)):
         for j in range(i+1,len(A)):
            temp = A[i]+ A[j]
            if temp<K:
               ans = max(ans,temp)
      return ans
ob1 = Solution()
print(ob1.twoSumLessThanK([34,23,1,24,75,33,54,8],60))

    '''

def get_max_sum(nums, target):
   
    if len(nums) == 1:
        return -1

    # sort the array first
    nums = sorted(nums)

    # Loop the array and get the value A[i] then we need to find a value A[j] such that A[i] + A[j] < K which means A[j] < K - A[i]. 
    #  two pointer solution
     
    ans = -1
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] < target:
            ans = max(ans, nums[i] + nums[j])
            i += 1
        else:
            j -= 1
            
    print("Best numbers are", nums[i-1], nums[j+1])
    return ans

if __name__ == '__main__':

    ar4 = [34,23,1,24,75,33,54,8]

    result = get_max_sum((ar4),60)

    print ('Max sum is {} '.format(result))