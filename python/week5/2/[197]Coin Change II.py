'''
Coin Change II
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.

You may assume that you have an unlimited number of each coin and that each value in coins is unique.

Example 1:

Input: amount = 4, coins = [1,2,3]

Output: 4
Explanation:

1+1+1+1 = 4
1+1+2 = 4
2+2 = 4
1+3 = 4
Example 2:

Input: amount = 7, coins = [2,4]

Output: 0
'''
class Solution:
    # 1) Dynamic Programming (Bottom-Up, 2D 테이블)
    # dp[i][a] = i번째 코인부터 사용해서 금액 a를 만드는 "조합 수"
    # 점화식:
    #  - a >= coin[i] 이면: dp[i][a] = dp[i+1][a] (i코인 안씀) + dp[i][a-coin[i]] (i코인 사용)
    #  - a <  coin[i] 이면: dp[i][a] = dp[i+1][a] (i코인 못씀 → 다음 코인으로)
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        coins.sort()  # 정렬(필수는 아니지만 일관성/가독성)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # 금액 0을 만드는 방법은 "아무 코인도 쓰지 않는 1가지" (모든 i에 대해 1)
        for i in range(n + 1):
            dp[i][0] = 1

        # 뒤에서부터(마지막 코인부터) 올라오며 채움
        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    # i코인을 쓰지 않는 경우 + i코인을 1개 쓰고 남은 금액(a - coins[i])에서 다시 i코인 포함 허용
                    dp[i][a] = dp[i + 1][a] + dp[i][a - coins[i]]
                else:
                    # **원 코드에서 빠졌던 부분**: i코인을 못 쓰니, 그냥 다음 코인(i+1)만 고려
                    dp[i][a] = dp[i + 1][a]

        return dp[0][amount]
    
    # 2) Dynamic Programming (Top-Down, DFS + 메모이제이션)
    # dfs(i, a): i번째 코인부터 사용해서 금액 a를 만드는 "조합 수"
    # 선택지:
    #  - i코인을 쓰지 않음 → dfs(i+1, a)
    #  - i코인을 씀(가능하면) → dfs(i, a - coins[i]) (무한히 사용 가능하므로 i 유지)
    def change(self, amount: int, coins: list[int]) -> int:
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        def dfs(i, a):
            # 금액을 정확히 만들었으면 1가지 방법 완성
            if a == 0:
                return 1
            # 코인을 다 봤는데도 금액이 남았다면 불가능
            if i >= len(coins):
                return 0
            # 메모 히트 시 반환
            if memo[i][a] != -1:
                return memo[i][a]

            # i코인을 쓰지 않는 경우는 항상 가능
            res = dfs(i + 1, a)

            # i코인을 쓸 수 있으면(금액이 충분) i코인을 사용한 경우도 더해줌
            if a >= coins[i]:
                res += dfs(i, a - coins[i])

            memo[i][a] = res
            return res

        return dfs(0, amount)
    
    # 3. Dynamic Programming optimal
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[a] += dp[a - coins[i]] if coins[i] <= a else 0
        return dp[amount]

if __name__ == "__main__":
    sol = Solution()
    amount = 4
    coins = [1, 2, 3]
    # 예시: 4를 만드는 조합 수 → 4 (1+1+1+1, 1+1+2, 2+2, 1+3)
    print(sol.change(amount, coins))