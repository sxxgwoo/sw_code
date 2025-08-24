'''
Unique Paths
There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

You may assume the output will fit in a 32-bit integer.

Example 1:



Input: m = 3, n = 6

Output: 21
Example 2:

Input: m = 3, n = 3

Output: 6
'''
class Solution:
    # 1. sw math
    def uniquePaths(self, m: int, n: int) -> int:
        # 팩토리얼 함수 정의
        def fac(k):
            res = 1
            for i in range(1, k + 1):
                res *= i
            return res
        # 경로의 개수 = (m+n-2) C (m-1) = (m+n-2)! / ( (m-1)! * (n-1)! )
        return int(fac(m + n - 2) / (fac(m - 1) * fac(n - 1)))
    
    # 2. Dynamic Programming (Top-Down)
    def uniquePaths(self, m: int, n: int) -> int:
        # -1로 초기화된 메모 테이블 생성
        memo = [[-1] * n for _ in range(m)]

        # DFS + 메모이제이션
        def dfs(i, j):
            # 도착점 (오른쪽 아래 끝)에 도달한 경우 1 경로
            if i == (m - 1) and j == (n - 1):
                return 1
            # 범위를 벗어난 경우는 경로 없음
            if i >= m or j >= n:
                return 0
            # 이미 계산된 경우 그대로 반환
            if memo[i][j] != -1:
                return memo[i][j]

            # 오른쪽과 아래쪽 이동한 경로 수를 더함
            memo[i][j] = dfs(i, j + 1) + dfs(i + 1, j)
            return memo[i][j]

        # 시작점 (0,0)에서 시작
        return dfs(0, 0)

        return dfs(0, 0)
    # 3. Dynamic Programming (Bottom-Up)
    def uniquePaths(self, m: int, n: int) -> int:
        # dp 배열 크기를 (m+1) x (n+1)로 크게 잡음
        # 바깥 테두리를 0으로 두어 IndexError 방지
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 목표 지점에 도달한 경우 경로의 수 = 1
        dp[m - 1][n - 1] = 1

        # 뒤에서부터 거꾸로 경로 수를 계산
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 현재 칸의 경로 수 = (아래쪽 + 오른쪽 칸의 경로 수)
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]

        # 출발점에서의 총 경로 수 반환
        return dp[0][0]
    
if __name__ == "__main__":
    sol = Solution()
    m = 3
    n = 6
    print(sol.uniquePaths(m,n))