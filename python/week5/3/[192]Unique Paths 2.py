'''
Unique Paths II

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * (10^9).

Example 1:

Input: obstacleGrid = [[0,0,0],[0,0,0],[0,1,0]]

Output: 3

Explanation: There are three ways to reach the bottom-right corner:

Right -> Right -> Down -> Down
Right -> Down -> Right -> Down
Down -> Right -> Right -> Down

Example 2:

Input: obstacleGrid = [[0,0,0],[0,0,1],[0,1,0]]

Output: 0
'''
from typing import List

# Dynamic Programming (Bottom-Up)
def uniquePathsWithObstacles(grid: List[List[int]]) -> int:
    M, N = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[M - 1][N - 1] == 1:
        return 0
    dp = [[0] * (N + 1) for _ in range(M + 1)]

    dp[M - 1][N - 1] = 1

    for r in range(M - 1, -1, -1):
        for c in range(N - 1, -1, -1):
            if grid[r][c] == 1:
                dp[r][c] = 0
            else:
                dp[r][c] += dp[r + 1][c]
                dp[r][c] += dp[r][c + 1]

    return dp[0][0]

# Dynamic Programming (Space Optimized)
def uniquePathsWithObstacles(grid: List[List[int]]) -> int:
    M, N = len(grid), len(grid[0])
    dp = [0] * (N + 1)
    dp[N - 1] = 1

    for r in range(M - 1, -1, -1):
        for c in range(N - 1, -1, -1):
            if grid[r][c]:
                dp[c] = 0
            else:
                dp[c] += dp[c + 1]

    return dp[0]

# ============================
# Test Case [[0,0,0],[0,0,0],[0,1,0]] -> 3
# ============================
if __name__ == "__main__":
    res = uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,1,0]])
    
    print(res)