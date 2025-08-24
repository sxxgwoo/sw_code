'''
Perfect Squares
You are given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer. For example, 1, 4, 9, 16, 25... are perfect squares.

Example 1:

Input: n = 13

Output: 2
Explanation: 13 = 4 + 9.

Example 2:

Input: n = 6

Output: 3
Explanation: 6 = 4 + 1 + 1.
'''
class Solution:
    # 1. sw sol (DFS + 메모이제이션, 모든 제곱수를 미리 계산)
    def numSquares(self, n: int) -> int:
        # 1부터 n까지의 제곱수 리스트 생성 (예: [1, 4, 9, 16, ...])
        sqaured = []
        for i in range(1, n + 1):
            sqaured.append(i * i)

        memo = {}  # 메모이제이션 딕셔너리

        def dfs(n):
            # 기저 조건: n이 0이면 제곱수 필요 없음
            if n == 0:
                return 0
            # 이미 계산한 값이면 메모에서 반환
            if n in memo:
                return memo[n]

            res = 1e9  # 큰 값으로 초기화
            # 모든 제곱수 후보를 순회
            for sq in sqaured:
                if n - sq >= 0:  # 제곱수를 뺄 수 있는 경우만
                    res = min(res, 1 + dfs(n - sq))  # 1개 추가 + 남은 수의 최소 개수

            memo[n] = res  # 메모에 저장
            return res

        minsqaured = dfs(n)
        # 1e9 이상이면 불가능하다고 판단하여 -1 반환
        return -1 if minsqaured >= 1e9 else minsqaured
    
    # 2. Dynamic Programming (Top-Down: DFS + 메모이제이션)
    def numSquares(self, n: int) -> int:
        memo = {}  # 메모이제이션

        def dfs(target):
            # 기저 조건: target이 0이면 제곱수 필요 없음
            if target == 0:
                return 0
            if target in memo:
                return memo[target]

            res = target  # 최악의 경우 (모두 1^2로 구성 → target 개 필요)
            # target 이하의 제곱수들을 탐색
            for i in range(1, target + 1):
                if i * i > target:  # 제곱수가 target보다 크면 중단
                    break
                res = min(res, 1 + dfs(target - i * i))

            memo[target] = res
            return res

        return dfs(n)
    
    # 3. Dynamic Programming (Bottom-Up)
    def numSquares(self, n: int) -> int:
        # dp[k] = k를 만들기 위한 최소 제곱수 개수
        dp = [n] * (n + 1)  # 최악의 경우 n개(모두 1^2)
        dp[0] = 0  # 0을 만들 때는 제곱수 0개 필요

        # 1부터 n까지 차례로 최소값 계산
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:  # 제곱수가 target보다 크면 종료
                    break
                # 현재 target을 만들 수 있는 최소 제곱수 개수 갱신
                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]
    

if __name__ == "__main__":
    sol = Solution()
    n = 103
    # 103을 제곱수 합으로 만드는 최소 개수 출력
    print(sol.numSquares(n))  