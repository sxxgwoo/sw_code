'''
Rotate Array

You are given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7,8], k = 4

Output: [5,6,7,8,1,2,3,4]

Explanation:
rotate 1 steps to the right: [8,1,2,3,4,5,6,7]
rotate 2 steps to the right: [7,8,1,2,3,4,5,6]
rotate 3 steps to the right: [6,7,8,1,2,3,4,5]
rotate 4 steps to the right: [5,6,7,8,1,2,3,4]

Example 2:

Input: nums = [1000,2,4,-3], k = 2

Output: [4,-3,1000,2]

Explanation:
rotate 1 steps to the right: [-3,1000,2,4]
rotate 2 steps to the right: [4,-3,1000,2]
'''
from typing import List

# Extra Space
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    tmp = [0] * n
    for i in range(n):
        tmp[(i + k) % n] = nums[i]
        
    nums[:] = tmp

# Using Reverse
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n

    def reverse(l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

# ============================
# Test Case [1,2,3,4,5,6,7,8] -> [5,6,7,8,1,2,3,4]
# ============================
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8]
    k = 4
    rotate(nums,k)

    print(nums)