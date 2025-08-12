'''
Longest Turbulent Subarray

You are given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.

Example 1:

Input: arr = [2,4,3,2,2,5,1,4]

Output: 4

Explanation: The longest turbulent subarray is [2,5,1,4].

Example 2:

Input: arr = [1,1,2]

Output: 2
'''
from typing import List


# Sliding Window
def maxTurbulenceSize(arr: List[int]) -> int:
    l, r, res, prev = 0, 1, 1, ""

    while r < len(arr):
        if arr[r - 1] > arr[r] and prev != ">":
            res = max(res, r - l + 1)
            r += 1
            prev = ">"
        elif arr[r - 1] < arr[r] and prev != "<":
            res = max(res, r - l + 1)
            r += 1
            prev = "<"
        else:
            r = r + 1 if arr[r] == arr[r - 1] else r
            l = r - 1
            prev = ""

    return res

# Dynamic Programming (Bottom-Up)
def maxTurbulenceSize(arr: List[int]) -> int:
    n = len(arr)
    if n == 1:
        return 1
    
    # dp[i][0]: 인덱스 i에서 끝나는 부분배열 중 직전이 > 관계인 turbulent 부분배열의 길이
    # dp[i][1]: 인덱스 i에서 끝나는 부분배열 중 직전이 < 관계인 turbulent 부분배열의 길이
    dp = [[1] * 2 for _ in range(n)] 

    max_len = 1
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            dp[i][1] = dp[i - 1][0] + 1
        elif arr[i] < arr[i - 1]:
            dp[i][0] = dp[i - 1][1] + 1

        max_len = max(max_len, dp[i][0], dp[i][1])

    return max_len

# ============================
# Test Case [2,4,3,2,2,5,1,4] -> 4
# ============================
if __name__ == "__main__":
    res = maxTurbulenceSize([2,4,3,2,2,5,1,4])
    
    print(res)