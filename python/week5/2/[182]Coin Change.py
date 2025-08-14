'''
Coin Change
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.

Example 1:

Input: coins = [1,5,10], amount = 12

Output: 3
Explanation: 12 = 10 + 1 + 1. Note that we do not have to use every kind coin available.

Example 2:

Input: coins = [2], amount = 3

Output: -1
Explanation: The amount of 3 cannot be made up with coins of 2.

Example 3:

Input: coins = [1], amount = 0

Output: 0
Explanation: Choosing 0 coins is a valid way to make up 0.
'''
# deque구현 간단한 Queue 클래스 구현 (FIFO)
class Queue:
    def __init__(self):
        self.data = []

    def append(self, val):
        self.data.append(val)

    def popleft(self):
        if self.data:
            return self.data.pop(0)  # O(n) 시간복잡도
        raise IndexError("pop from empty queue")

    def __len__(self):
        return len(self.data)

    def __bool__(self):
        return bool(self.data)
    
class Solution:
    # 1. BFS
    # def coinChange(self, coins: list[int], amount: int) -> int:
    #     if amount == 0:
    #         return 0
    #     q = Queue()
    #     q.append(0)
    #     # q = deque([0])
    #     seen = [False] * (amount + 1)
    #     seen[0] = True
    #     res = 0

    #     while q:
    #         res += 1
    #         for _ in range(len(q)):
    #             cur = q.popleft()
    #             for coin in coins:
    #                 nxt = cur + coin
    #                 if nxt == amount:
    #                     return res
    #                 if nxt > amount or seen[nxt]:
    #                     continue
    #                 seen[nxt] = True
    #                 q.append(nxt)

    #     return -1
    
    # 2. Dynamic Programming (Bottom-Up)
    def coinChange(coins: list[int], amount: int) -> int:
        # dp[a]: 금액 a를 만들기 위한 최소 동전 개수
        # 초기값을 amount+1(절대 나올 수 없는 큰 값)로 채워 "아직 계산 전/불가능"을 표현
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # 금액 0을 만드는 최소 개수는 0개(아무 동전도 사용 안 함)

        # a를 1부터 amount까지 증가시키며 최솟값을 채운다
        for a in range(1, amount + 1):
            # 가능한 모든 동전 c를 시도
            for c in coins:
                if a - c >= 0:
                    # c를 한 개 쓰고 남은 금액 a-c를 만드는 최소 개수 + 1(지금 사용한 c)
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # dp[amount]가 초기의 큰 값이면(=갱신 실패) 만들 수 없는 금액 → -1
        return dp[amount] if dp[amount] != amount + 1 else -1

    
    # 3. Dynamic Programming (Top-Down)
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins
    
if __name__ == "__main__":
    sol = Solution()
    # coins=[11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
    # amount=330
    # coins=[357,239,73,52]
    # amount=9832
    coins=[2,9]
    amount=5
    print(sol.coinChange(coins,amount))