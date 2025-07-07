'''
Find K Closest Elements

You are given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:

Input: arr = [2,4,5,8], k = 2, x = 6

Output: [4,5]

Example 2:

Input: arr = [2,3,4], k = 3, x = 1

Output: [2,3,4]
'''
from typing import List

# Two Pointers
def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    l, r = 0, len(arr) - 1
    while r - l >= k:
        if abs(x - arr[l]) <= abs(x - arr[r]):
            r -= 1
        else:
            l += 1
    
    return arr[l: r + 1]

# Binary Search + Two Pointers
def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    l, r = 0, len(arr) - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid

    l, r = l - 1, l
    while r - l - 1 < k:
        if l < 0:
            r += 1
        elif r >= len(arr):
            l -= 1
        elif abs(arr[l] - x) <= abs(arr[r] - x):
            l -= 1
        else:
            r += 1

    return arr[l + 1:r]

# ============================
# Test Case [2,4,5,8], 2, 6 -> [4,5]
# ============================
if __name__ == "__main__":
    arr = [2,4,5,8]
    k = 2
    x = 6
    res = findClosestElements(arr, k, x)

    print(res)
