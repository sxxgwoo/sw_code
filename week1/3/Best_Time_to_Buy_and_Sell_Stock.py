# Best Time to Buy and Sell Stock
# maximum profit
# Sliding Window Variable Size
from typing import List

# Solution 1
def maxProfit(prices: List[int]) -> int:
    res = 0
    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i + 1, len(prices)):
            sell  = prices[j]
            res = max(res, sell - buy)
    return res

# Solution 2
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