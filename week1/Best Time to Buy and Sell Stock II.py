'''
Best Time to Buy and Sell Stock II
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. However, you can buy it then immediately sell it on the same day. Also, you are allowed to perform any number of transactions but can hold at most one share of the stock at any time.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]

Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3. Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]

Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4.
'''

class Solution:

    # 1) greedy
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        # sell_list=[]
        # buy_list=[]
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
                # sell_list.append(prices[i])
                # buy_list.append(prices[i-1])

        return profit

    # 2) Recursion
    # def maxProfit(self, prices: list[int]) -> int:
    #     # i: 현재 날짜 인덱스, bought: 현재 주식을 보유 중인지 여부
    #     def rec(i, bought):
    #         # 종료 조건: 마지막 날 이후에는 더 이상 거래 불가
    #         if i == len(prices):
    #             return 0  # 더 이상 수익 없음

    #         # ① 아무 행동도 하지 않고 다음 날로 넘어가는 경우
    #         res = rec(i + 1, bought)

    #         # ② 주식을 보유하고 있다면 → 팔 수 있음
    #         if bought:
    #             # 현재 가격에 주식을 팔고, 다음 날부터 주식 없음 상태로 재귀 호출
    #             res = max(res, prices[i] + rec(i + 1, False))
    #         else:
    #             # 주식을 보유하고 있지 않다면 → 살 수 있음
    #             # 현재 가격을 지불하고 주식을 사고, 다음 날부터 주식 있음 상태로 재귀 호출
    #             res = max(res, -prices[i] + rec(i + 1, True))

    #         return res

    #     # 첫날부터 시작, 주식은 아직 보유하지 않은 상태
    #     return rec(0, False)
    

    
    
if __name__ == "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))