'''
Contains Duplicate II

You are given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k, otherwise return false.

Example 1:

Input: nums = [1,2,3,1], k = 3

Output: true

Example 2:

Input: nums = [2,1,2], k = 1

Output: false
'''
from typing import List

# Brute Force
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k + 1)):
            if nums[L] == nums[R]:
                return True
    return False

# Hash Map
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    mp = {}

    for i in range(len(nums)):
        if nums[i] in mp and i - mp[nums[i]] <= k:
            return True
        mp[nums[i]] = i
        
    return False

# ============================
# Test Case [1,2,3,1] -> true
# ============================
if __name__ == "__main__":
    nums = [1,2,3,1]
    k = 3
    flag = containsNearbyDuplicate(nums,k)

    print(flag)