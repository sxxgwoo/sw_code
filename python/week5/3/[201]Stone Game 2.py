'''
Stone Game II

Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:

Input: piles = [3,1,2,5,7]

Output: 10

Explanation: Alice takes first pile, then Bob takes the second pile, then Alice takes the next two piles and Bob takes the last remaining pile. This makes Alice's score 3 + 2 + 5 = 10, which is the maximum Alice can get.

Example 2:

Input: piles = [4,3,2,5,10]

Output: 11
'''
from typing import List

# Dynamic Programming (Bottom-Up)
def stoneGameII(piles: List[int]) -> int:
    n = len(piles)
    dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(2)]

    for i in range(n - 1, -1, -1):
        for M in range(1, n + 1):
            total = 0
            dp[1][i][M] = 0
            dp[0][i][M] = float("inf")

            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break
                total += piles[i + X - 1]

                dp[1][i][M] = max(dp[1][i][M], total + dp[0][i + X][max(M, X)])
                dp[0][i][M] = min(dp[0][i][M], dp[1][i + X][max(M, X)])

    return dp[1][0][1]

# Dynamic Programming (Top-Down)
def stoneGameII(piles: List[int]) -> int:
    dp = {}

    def dfs(alice, i, M):
        if i == len(piles):
            return 0
        if (alice, i, M) in dp:
            return dp[(alice, i, M)]

        res = 0 if alice else float("inf")
        total = 0
        for X in range(1, 2 * M + 1):
            if i + X > len(piles):
                break
            total += piles[i + X - 1]
            if alice:
                res = max(res, total + dfs(not alice, i + X, max(M, X)))
            else:
                res = min(res, dfs(not alice, i + X, max(M, X)))

        dp[(alice, i, M)] = res
        return res

    return dfs(True, 0, 1)

# ============================
# Test Case [3,1,2,5,7] -> 10
# ============================
if __name__ == "__main__":
    res = stoneGameII([3,1,2,5,7])
    
    print(res)
