'''
Missing Number

Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:

Input: nums = [1,2,3]

Output: 0

Explanation: Since there are 3 numbers, the range is [0,3]. The missing number is 0 since it does not appear in nums.

Example 2:

Input: nums = [0,2]

Output: 1
'''
from typing import List

# SH proof
def missingNumber(nums: List[int]) -> int:
    n = len(nums) + 1
    res = [0 for _ in range(n)]

    for i in nums:
        res[i] = 1
    
    for i in range(n):
        if(res[i] == 0):
            return i
        
# Hash set
def missingNumber(nums: List[int]) -> int:
    num_set = set(nums)
    n = len(nums)
    for i in range(n + 1):
        if i not in num_set:
            return i

# ============================
# Test Case [0,2] -> 1
# ============================
if __name__ == "__main__":
    res = missingNumber([0,2])
    
    print(res)