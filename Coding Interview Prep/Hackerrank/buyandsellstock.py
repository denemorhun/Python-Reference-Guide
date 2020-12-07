# EASY - best time to buy and sell stock

'''
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Solution:

 In this case, instead of looking for every peak following a valley, we can simply go on crawling over the slope and keep on adding the profit obtained from every consecutive transaction. In the end,we will be using the peaks and valleys effectively, but we need not track the costs corresponding to the peaks and valleys along with the maximum profit, but we can directly keep on adding the difference between the consecutive numbers of the array if the second number is larger than the first one, and at the total sum we obtain will be the maximum profit. This approach will simplify the solution. This can be made clearer by taking this example:

[1, 7, 2, 3, 6, 7, 6, 7]

Profit Graph

From the above graph, we can observe that the sum A+B+CA+B+C is equal to the difference DD corresponding to the difference between the heights of the consecutive peak and valley.

'''

import collections
import os
import datetime
import sys
from collections import Counter


def findMaxProfit(prices) -> int:

    # Python3 code to Check for  
    # balanced parentheses in an expression 

    if len(input) == 0: 
        return 0

    maxprofit = 0

    # aggragate all peaks and deduct the valleys
    for i in range(1,len(input)):
        print(f'i {i}')
        if prices[i] > prices[i-1]:
            maxprofit += prices[i] - prices[i-1]

    return maxprofit


if __name__ == '__main__':
    input = [1,2,3,4,5] # -> 7
    # input = [7,1,5,3,6,4] # -> 7

    print(findMaxProfit(input))