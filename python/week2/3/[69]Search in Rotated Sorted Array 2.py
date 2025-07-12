'''
Search in Rotated Sorted Array II

You are given an array of length n which was originally sorted in non-decreasing order (not necessarily with distinct values). It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return true if target is in nums, or false if it is not present.

You must decrease the overall operation steps as much as possible.

Example 1:

Input: nums = [3,4,4,5,6,1,2,2], target = 1

Output: true

Example 2:

Input: nums = [3,5,6,0,0,1,2], target = 4

Output: false
'''
from typing import List

# Brute Force
def search(nums: List[int], target: int) -> bool:
    return target in nums

# Binary Search
def search(nums: List[int], target: int) -> bool:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return True

        if nums[l] < nums[m]:  # Left portion
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        elif nums[l] > nums[m]:  # Right portion
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
        else:
            l += 1

    return False

# ============================
# Test Case [3,4,4,5,6,1,2,2], 1 -> true
# ============================
if __name__ == "__main__":
    res = search([3,4,4,5,6,1,2,2], 1)

    print(res)