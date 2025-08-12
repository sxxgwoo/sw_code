'''
Partition Equal Subset Sum

You are given an array of positive integers nums.

Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

Example 1:

Input: nums = [1,2,3,4]

Output: true

Explanation: The array can be partitioned as [1, 4] and [2, 3].

Example 2:

Input: nums = [1,2,3,4,5]

Output: false
'''
from typing import List

# Recursion
def canPartition(nums: List[int]) -> bool:
    if sum(nums) % 2:
        return False

    def dfs(i, target):
        if i >= len(nums):
            return target == 0
        if target < 0:
            return False

        return dfs(i + 1, target) or dfs(i + 1, target - nums[i])

    return dfs(0, sum(nums) // 2)

# Dynamic Programming (Hash Set)
def canPartition(nums: List[int]) -> bool:
    if sum(nums) % 2:
        return False

    dp = set()
    dp.add(0)
    target = sum(nums) // 2

    for i in range(len(nums) - 1, -1, -1):
        nextDP = set()
        for t in dp:
            if (t + nums[i]) == target:
                return True
            nextDP.add(t + nums[i])
            nextDP.add(t)
        dp = nextDP
    return False

# ============================
# Test Case [1,5,11,5] -> True
# ============================
if __name__ == "__main__":
    res = canPartition([1,5,11,5])
    
    print(res)