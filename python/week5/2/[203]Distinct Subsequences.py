'''
Distinct Subsequences
You are given two strings s and t, both consisting of english letters.

Return the number of distinct subsequences of s which are equal to t.

Example 1:

Input: s = "caaat", t = "cat"

Output: 3
Explanation: There are 3 ways you can generate "cat" from s.

(c)aa(at)
(c)a(a)a(t)
(ca)aa(t)
Example 2:

Input: s = "xxyxy", t = "xy"

Output: 5
Explanation: There are 5 ways you can generate "xy" from s.

(x)x(y)xy
(x)xyx(y)
x(x)(y)xy
x(x)yx(y)
xxy(x)(y)
'''
class Solution:
    # 1) Dynamic Programming (Top-Down: DFS + 메모이제이션)
    # dfs(i, j): s[i:]에서 t[j:]를 만들 수 있는 서로 다른 subsequence의 개수
    def numDistinct(self, s: str, t: str) -> int:
        # t가 s보다 길면 subsequence로 만들 수 없음
        if len(t) > len(s):
            return 0

        dp = {}  # 메모이제이션 딕셔너리

        def dfs(i, j):
            # t를 끝까지 매칭했다면 subsequence 1개 완성
            if j == len(t):
                return 1
            # s를 다 썼는데 t가 남았다면 subsequence 불가능
            if i == len(s):
                return 0
            # 이미 계산한 경우 그대로 반환
            if (i, j) in dp:
                return dp[(i, j)]

            # s[i]를 사용하지 않는 경우
            res = dfs(i + 1, j)

            # s[i] == t[j]라면 → s[i]를 사용하는 경우도 추가
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)

            dp[(i, j)] = res
            return res

        # s[0:], t[0:]에서 시작
        return dfs(0, 0)
    
    # 2) Dynamic Programming (Bottom-Up: 2D 테이블)
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp[i][j] = s[i:]에서 t[j:]를 만들 수 있는 subsequence 개수
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # t가 빈 문자열("")일 때는 항상 subsequence 1개 존재 (공집합)
        for i in range(m + 1):
            dp[i][n] = 1

        # 뒤에서부터 채워나감
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 기본적으로는 s[i]를 건너뛰는 경우
                dp[i][j] = dp[i + 1][j]
                # 만약 s[i] == t[j]라면, s[i]를 사용하는 경우도 추가
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        # 최종적으로 s[0:], t[0:]에서 가능한 subsequence 개수
        return dp[0][0]
    

if __name__ == "__main__":
    sol = Solution()
    s = "xxyxy"
    t = "xy"
    # 출력: 5
    # 가능한 subsequence:
    # (x)x(y)xy, (x)xyx(y), x(x)(y)xy, x(x)yx(y), xxy(x)(y)
    print(sol.numDistinct(s, t))