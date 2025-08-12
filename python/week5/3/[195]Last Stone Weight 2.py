'''
Last Stone Weight II

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Example 1:

Input: stones = [2,4,1,5,6,3]

Output: 1

Explanation:

We smash 2 and 1 which makes the array [1,4,5,6,3].
We smash 4 and 3 which makes the array [1,1,5,6].
We smash 5 and 6 which makes the array [1,1,1].
We smash 1 and 1 which makes the array [1].

Example 2:

Input: stones = [4,4,1,7,10]

Output: 2
'''
from typing import List

# Dynamic Programming (Bottom-Up)
def lastStoneWeightII(stones: List[int]) -> int:
    stoneSum = sum(stones)
    target = stoneSum // 2
    n = len(stones)

    dp = [[0] * (target + 1) for _ in range(n + 1)] # dp[i][t]는 i번째 돌까지 고려해서 무게 t를 만들 수 있을 때 가능한 최대 무게합

    for i in range(1, n + 1):
        for t in range(target + 1):
            if t >= stones[i - 1]:
                dp[i][t] = max(dp[i - 1][t], dp[i - 1][t - stones[i - 1]] + stones[i - 1])
            else:
                dp[i][t] = dp[i - 1][t]

    return stoneSum - 2 * dp[n][target]

# Recursion
def lastStoneWeightII(stones: List[int]) -> int:
    stoneSum = sum(stones)
    target = (stoneSum + 1) // 2

    def dfs(i, total):
        if total >= target or i == len(stones):
            return abs(total - (stoneSum - total))
        return min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))

    return dfs(0, 0)

# ============================
# Test Case [4,4,1,7,10] -> 2
# ============================
if __name__ == "__main__":
    res = lastStoneWeightII([4,4,1,7,10])
    
    print(res)