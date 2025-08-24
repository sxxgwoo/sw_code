'''
Regular Expression Matching
You are given an input string s consisting of lowercase english letters, and a pattern p consisting of lowercase english letters, as well as '.', and '*' characters.

Return true if the pattern matches the entire input string, otherwise return false.

'.' Matches any single character
'*' Matches zero or more of the preceding element.
Example 1:

Input: s = "aa", p = ".b"

Output: false
Explanation: Regardless of which character we choose for the '.' in the pattern, we cannot match the second character in the input string.

Example 2:

Input: s = "nnn", p = "n*"

Output: true
Explanation: '*' means zero or more of the preceding element, 'n'. We choose 'n' to repeat three times.

Example 3:

Input: s = "xyz", p = ".*z"

Output: true
Explanation: The pattern ".*" means zero or more of any character, so we choose ".." to match "xy" and "z" to match "z".
'''
class Solution:
    # 1) Dynamic Programming Top-Down (재귀 DFS + 메모이제이션)
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        cache = {}  # 메모이제이션: (i, j) -> bool

        def dfs(i, j):
            # 패턴 p를 끝까지 다 확인한 경우 → 문자열 s도 끝까지 가야 true
            if j == n:
                return i == m

            # 이미 계산한 상태면 반환
            if (i, j) in cache:
                return cache[(i, j)]

            # 현재 위치에서 한 글자 매칭 여부 확인
            # (s[i] == p[j]) 또는 (p[j] == ".")
            match = i < m and (s[i] == p[j] or p[j] == ".")

            # 다음 문자가 '*'인 경우 → 두 가지 선택
            if (j + 1) < n and p[j + 1] == "*":
                # 1) '*'를 0번 사용하는 경우: dfs(i, j+2)
                # 2) '*'를 1번 이상 사용하는 경우: match일 때 dfs(i+1, j)
                cache[(i, j)] = (dfs(i, j + 2) or
                                 (match and dfs(i + 1, j)))
                return cache[(i, j)]

            # '*'가 아닌 경우, 단순 매칭 시 다음으로 진행
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            # 매칭 실패
            cache[(i, j)] = False
            return False

        # 시작 위치 (0,0)에서 탐색
        return dfs(0, 0)
    
    # 2) Dynamic Programming Bottom-Up (DP 테이블)
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] = s[i:]와 p[j:]가 매칭되는지 여부
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        # s와 p 모두 끝까지 갔을 때는 매칭 성공
        dp[len(s)][len(p)] = True

        # 뒤에서부터 채워나감
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                # 현재 문자가 매칭 가능한지 확인
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                # 다음 문자가 '*'인 경우
                if (j + 1) < len(p) and p[j + 1] == "*":
                    # 1) '*'를 0번 사용하는 경우 → dp[i][j+2]
                    dp[i][j] = dp[i][j + 2]
                    # 2) '*'를 1번 이상 사용하는 경우 → 현재 매치되면 dp[i+1][j]
                    if match:
                        dp[i][j] = dp[i + 1][j] or dp[i][j]
                # '*'가 아닌 경우 → 현재 문자가 매치되면 다음 칸으로 진행
                elif match:
                    dp[i][j] = dp[i + 1][j + 1]

        # 전체 문자열 s와 전체 패턴 p가 매칭되는지 여부 반환
        return dp[0][0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa", ".b"))    # False
    print(sol.isMatch("nnn", "n*"))   # True
    print(sol.isMatch("xyz", ".*z"))  # True