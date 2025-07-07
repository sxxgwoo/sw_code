'''
Best Time to Buy and Sell Stock

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6

Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0

Explanation: No profitable transactions can be made, thus the max profit is 0.
'''
from typing import List

# Brute Force
def maxProfit(prices: List[int]) -> int:
    res = 0
    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i + 1, len(prices)):
            sell  = prices[j]
            res = max(res, sell - buy)
    return res

# Dynamic Programming
def maxProfit(prices: List[int]) -> int:
    maxP = 0
    minBuy = prices[0]

    for sell in prices:
        maxP = max(maxP, sell - minBuy)
        minBuy = min(minBuy, sell)
    return maxP

# ============================
# Test Case [10,1,5,6,7,1] -> 6
# ============================
if __name__ == "__main__":
    prices = [10,1,5,6,7,1]
    profit = maxProfit(prices)

    print(profit)