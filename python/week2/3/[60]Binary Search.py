'''
Binary Search

You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3

Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
'''
from typing import List

# Iterative Binary Search
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        # (l + r) // 2 can lead to overflow
        m = l + ((r - l) // 2)  

        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1

# Recursive Binary Search
def binary_search(l: int, r: int, nums: List[int], target: int) -> int:
    if l > r:
        return -1
    m = l + (r - l) // 2
    
    if nums[m] == target:
        return m
    if nums[m] < target:
        return binary_search(m + 1, r, nums, target)
    return binary_search(l, m - 1, nums, target)

def search(nums: List[int], target: int) -> int:
    return binary_search(0, len(nums) - 1, nums, target)

# ============================
# Test Case [-1,0,2,4,6,8], 4 -> 3
# ============================
if __name__ == "__main__":
    res = search([-1,0,2,4,6,8], 4)

    print(res)