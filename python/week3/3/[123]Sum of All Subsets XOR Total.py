'''
Sum of All Subsets XOR Total

The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.

You are given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

Example 1:

Input: nums = [2,4]

Output: 12

Explanation: The four subsets of [2,4] are

The empty subset has an XOR total of 0.
[2] has an XOR total of 2.
[4] has an XOR total of 4.
[2,4] has an XOR total of (2 XOR 4 = 6).
The sum of all XOR totals is 0 + 2 + 4 + 6 = 12.

Example 2:

Input: [3,1,1]

Output: 12

Explanation: The eight subsets of [3,1,1] are

The empty subset has an XOR total of 0.
[3] has an XOR total of 3.
[1] has an XOR total of 1.
[1] has an XOR total of 1.
[3,1] has an XOR total of (3 XOR 1 = 2).
[3,1] has an XOR total of (3 XOR 1 = 2).
[1,1] has an XOR total of (1 XOR 1 = 0).
[3,1,1] has an XOR total of (3 XOR 1 XOR 1 = 3).
The sum of all XOR totals is 0 + 3 + 1 + 1 + 2 + 2 + 0 + 3 = 12.
'''
from typing import List

# Recursion
def subsetXORSum(nums: List[int]) -> int:
    def dfs(i, total):
        if i == len(nums):
            return total
        return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)

    return dfs(0, 0)

# Backtracking
def subsetXORSum(nums: List[int]) -> int:
    res = 0

    def backtrack(i, subset):
        nonlocal res
        xorr = 0
        for num in subset:
            xorr ^= num
        res += xorr

        for j in range(i, len(nums)):
            subset.append(nums[j])
            backtrack(j + 1, subset)
            subset.pop()
    
    backtrack(0, [])
    return res

# ============================
# Test Case [3,1,1] -> 12
# ============================
if __name__ == "__main__":
    res = subsetXORSum([3,1,1])
    
    print(res)