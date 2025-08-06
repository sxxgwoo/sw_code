'''
Climbing Stairs

You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:

Input: n = 2

Output: 2

Explanation: 1 + 1 = 2, 2 = 2

Example 2:

Input: n = 3

Output: 3

Explanation: 1 + 1 + 1 = 3, 1 + 2 = 3, 2 + 1 = 3
'''

# Dynamic Programming (Bottom-Up)
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Dynamic Programming (Top-Down)
def climbStairs(n: int) -> int:
    cache = [-1] * n    # i번째 계단에서 n번째 계단까지 올라가는 방법의 수
    def dfs(i):
        if i >= n:
            return i == n   # i와 n이 같으면 1을 반환
        if cache[i] != -1:
            return cache[i]
        cache[i] = dfs(i + 1) + dfs(i + 2)
        return cache[i]

    return dfs(0)

# ============================
# Test Case 3 -> 3
# ============================
if __name__ == "__main__":
    res = climbStairs(3)
    
    print(res)