# MEDIUM

'''
["a","b","ba","bca","bda","bdca"]

return longest string chain. 

Start with the longest and delete a char and walk backwards. 
Get the first item in the array of strings
check if the next item substing is in the first sting
if not move to next item
'''

def longestStrChain(words) -> int:
   
    if input is None:
        return None

    dp = {}
    for w in sorted(words, key=len):
        dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
    return max(dp.values())

if __name__ == '__main__':

    input = ["a","b","ba","bca","bda","bdca"]

    result = longestStrChain(input)

    print (f'longest string {result} ')