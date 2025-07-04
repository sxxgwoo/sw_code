# Minimum Size Subarray Sum
# return the minimum length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0
# Sliding Window Variable Size, Prefix Sums
from typing import List

# Solution 1
def minSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    res = float("inf")

    for i in range(n):
        curSum = 0
        for j in range(i, n):
            curSum += nums[j]
            if curSum >= target:
                res = min(res, j - i + 1)
                break
    
    return 0 if res == float("inf") else res

# Solution 2
def minSubArrayLen(target: int, nums: List[int]) -> int:
    l, total = 0, 0
    res = float("inf")

    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(r - l + 1, res)
            total -= nums[l]
            l += 1

    return 0 if res == float("inf") else res

# ============================
# Test Case 10, [2,1,5,1,5,3] -> 3
# ============================
if __name__ == "__main__":
    target = 10
    nums = [2,1,5,1,5,3]
    res = minSubArrayLen(target, nums)

    print(res)