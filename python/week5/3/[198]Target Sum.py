'''
Target Sum

You are given an array of integers nums and an integer target.

For each number in the array, you can choose to either add or subtract it to a total sum.

For example, if nums = [1, 2], one possible sum would be "+1-2=-1".

If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".

Return the number of different ways that you can build the expression such that the total sum equals target.

Example 1:

Input: nums = [2,2,2], target = 2

Output: 3

Explanation: There are 3 different ways to sum the input numbers to get a sum of 2.
+2 +2 -2 = 2
+2 -2 +2 = 2
-2 +2 +2 = 2
'''
from typing import List
from collections import defaultdict

# Recursion
def findTargetSumWays(nums: List[int], target: int) -> int:

    def backtrack(i, total):
        if i == len(nums):
            return total == target

        return (backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i]))

    return backtrack(0, 0)

# Dynamic Programming (Bottom-Up)
def findTargetSumWays(nums: List[int], target: int) -> int:
    n = len(nums)
    dp = [defaultdict(int) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for total, count in dp[i].items():
            dp[i + 1][total + nums[i]] += count
            dp[i + 1][total - nums[i]] += count

    return dp[n][target]

# ============================
# Test Case [2,2,2], 2 -> 3
# ============================
if __name__ == "__main__":
    res = findTargetSumWays([2,2,2], 2)
    
    print(res)