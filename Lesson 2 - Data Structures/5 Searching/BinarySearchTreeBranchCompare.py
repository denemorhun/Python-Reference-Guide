# the root index starts at ONE, and the left child 
# index is always twice its parent index, and 
# the right index is the twice parent index plus one.

# https://helloacm.com/comparing-left-and-right-branch-of-a-complete-binary-tree/

def solution(arr):
    # Type your solution here 
    if len(arr) == 0:
        return ""
    elif not arr:
        return ""

    def sum(arr,idx):
        if(idx - 1 < len(arr)):
            if (arr[idx - 1] == -1):
                return 0
            return arr[idx - 1] + sum(arr, idx * 2) + sum(arr, idx * 2 + 1)
        return 0
    
    left = sum(arr, 2)
    right = sum(arr, 3)
    return "" if left == right else "Left" if left > right else "Right" 
    