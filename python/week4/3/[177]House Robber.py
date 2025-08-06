'''
House Robber

You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:

Input: nums = [1,1,3,3]

Output: 4

Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:

Input: nums = [2,9,8,3,6]

Output: 16

Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.
'''
from typing import List

# Dynamic Programming (Bottom-Up)
def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
    
    return dp[-1]

# Dynamic Programming (Top-Down)
def rob(nums: List[int]) -> int:
    memo = [-1] * len(nums)

    def dfs(i):
        if i >= len(nums):
            return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
        return memo[i]
    
    return dfs(0)

# ============================
# Test Case [2,9,8,3,6] -> 16
# ============================
if __name__ == "__main__":
    res = rob([2,9,8,3,6])
    
    print(res)