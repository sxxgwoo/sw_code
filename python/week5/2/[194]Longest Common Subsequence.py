'''
Longest Common Subsequence
Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
A common subsequence of two strings is a subsequence that exists in both strings.

Example 1:

Input: text1 = "cat", text2 = "crabt" 

Output: 3 
Explanation: The longest common subsequence is "cat" which has a length of 3.

Example 2:

Input: text1 = "abcd", text2 = "abcd"

Output: 4
Example 3:

Input: text1 = "abcd", text2 = "efgh"

Output: 0
'''
class Solution:
    # 1. Dynamic Programming (Top-Down, 재귀 + 메모이제이션)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}  # (i, j) 위치에서의 LCS 결과를 저장할 메모이제이션 딕셔너리

        def dfs(i, j):
            # 기저 조건: 어느 문자열이든 끝까지 다 본 경우 LCS 길이는 0
            if i == len(text1) or j == len(text2):
                return 0
            # 이미 계산된 경우 반환
            if (i, j) in memo:
                return memo[(i, j)]

            # 문자가 같으면 → 두 문자를 포함하는 공통 부분 수열 +1
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                # 다르면 → 한쪽을 건너뛴 경우 중 최댓값
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))

            return memo[(i, j)]

        # 시작점 (0,0)에서 LCS 계산 시작
        return dfs(0, 0)
    
    # 2. Dynamic Programming (Bottom-Up, 반복문)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = text1[i:] 와 text2[j:]의 LCS 길이
        dp = [[0 for j in range(len(text2) + 1)]
                 for i in range(len(text1) + 1)]

        # 뒤에서부터 채워나감
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    # 문자가 같으면 +1 하고 대각선(i+1, j+1) 참조
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # 문자가 다르면 오른쪽(j+1) vs 아래(i+1) 중 큰 값 선택
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # 전체 문자열(text1, text2)의 LCS 길이는 dp[0][0]
        return dp[0][0]
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonSubsequence("cat", "crabt"))   # 출력: 3 ("cat")
    print(sol.longestCommonSubsequence("abcd", "abcd"))   # 출력: 4
    print(sol.longestCommonSubsequence("abcd", "efgh"))   # 출력: 0