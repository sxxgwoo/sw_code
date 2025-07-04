# Rotate Array to the right by k steps
# Static Arrays
from typing import List

# Solution 1
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    tmp = [0] * n
    for i in range(n):
        tmp[(i + k) % n] = nums[i]
        
    nums[:] = tmp

# Solution 2
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