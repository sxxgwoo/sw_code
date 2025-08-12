'''
N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

Input: n = 3

Output: 2
Explanation:
T_3 = 0 + 1 + 1 = 2

Example 2:

Input: n = 21

Output: 121415
'''
class Solution:
    # 1. Dynamic Programming (Top-Down: 재귀 + 메모이제이션)
    def __init__(self):
        self.dp = {}  # 이미 계산한 값들을 저장해두는 딕셔너리 (메모이제이션)

    def tribonacci(self, n: int) -> int:
        # 기저 조건: n이 0이면 0, 1 또는 2이면 1 반환
        if n <= 2:
            return 1 if n != 0 else 0
        
        # 이미 계산된 값이 있으면 그대로 반환 (중복 계산 방지)
        if n in self.dp:
            return self.dp[n]

        # 재귀적으로 tribonacci 값 계산 후 저장
        self.dp[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.dp[n]

    # 2. Dynamic Programming (Bottom-Up: 반복문)
    def tribonacci(self, n: int) -> int:
        # 기저 조건 처리
        if n <= 2:
            return 1 if n != 0 else 0

        # DP 테이블 생성 (0으로 초기화)
        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1  # 초기 값 설정: T(1) = 1, T(2) = 1

        # 작은 값부터 차례대로 계산하여 저장
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]  # T(n) = T(n-1) + T(n-2) + T(n-3)

        return dp[n]  # 최종 결과 반환
      


if __name__=="__main__":
    sol = Solution()
    n = 21
    print(sol.tribonacci(n))
        