'''
Integer Break

You are given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

Example 1:

Input: n = 4

Output: 4

Explanation: 4 = 2 + 2, 2 x 2 = 4.

Example 2:

Input: n = 12

Output: 81

Explanation: 12 = 3 + 3 + 3 + 3, 3 x 3 x 3 x 3 = 81.
'''
# Dynamic Programming (Bottom-Up)
def integerBreak(n: int) -> int:
    dp = [0] * (n + 1)
    dp[1] = 1

    for num in range(2, n + 1):
        dp[num] = 0 if num == n else num
        for i in range(1, num):
            dp[num] = max(dp[num], dp[i] * dp[num - i])

    return dp[n]

# Recursion (Brute Force)
def integerBreak(n: int) -> int:
    def dfs(num):
        if num == 1:
            return 1
        res = 0 if num == n else num
        for i in range(1, num):
            val = dfs(i) * dfs(num - i)
            res = max(res, val)
        return res
    return dfs(n)

# ============================
# Test Case 12 -> 81
# ============================
if __name__ == "__main__":
    res = integerBreak(12)
    
    print(res)