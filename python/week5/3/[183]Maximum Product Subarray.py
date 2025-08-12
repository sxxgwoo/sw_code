'''
Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product within the array and return it.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

Example 1:

Input: nums = [1,2,-3,4]

Output: 4

Example 2:

Input: nums = [-2,-1]

Output: 2
'''
from typing import List

# Brute Force
def maxProduct(nums: List[int]) -> int:
    res = nums[0]

    for i in range(len(nums)):
        cur = nums[i]
        res = max(res, cur)
        for j in range(i + 1, len(nums)):
            cur *= nums[j]
            res = max(res, cur)
            
    return res

# Sliding Window
def maxProduct(nums: List[int]) -> int:
    A = []
    cur = []
    res = float('-inf')

    for num in nums:
        res = max(res, num)
        if num == 0:
            if cur:
                A.append(cur)   # 0이 등장하면 그 전까지 쌓은 subarray cur를 A에 저장
            cur = []
        else:
            cur.append(num)

    if cur:
        A.append(cur)

    for sub in A:
        negs = sum(1 for i in sub if i < 0)
        prod = 1
        need = negs if negs % 2 == 0 else negs - 1
        negs = 0
        j = 0

        for i in range(len(sub)):
            prod *= sub[i]
            if sub[i] < 0:
                negs += 1
                while negs > need:
                    prod //= sub[j]
                    if sub[j] < 0:
                        negs -= 1
                    j += 1
            if j <= i:
                res = max(res, prod)

    return res

# ============================
# Test Case [1,2,-3,4] -> 4
# ============================
if __name__ == "__main__":
    res = maxProduct([1,2,-3,4])
    
    print(res)