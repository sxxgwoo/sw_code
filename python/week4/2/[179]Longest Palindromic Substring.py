'''
Longest Palindromic Substring
Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

Example 1:

Input: s = "ababd"

Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.

Example 2:

Input: s = "abbc"

Output: "bb"
'''
class Solution:
    # 1. Two Pointers 방식
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0   # 결과 팰린드롬의 시작 인덱스
        resLen = 0   # 결과 팰린드롬의 길이

        # 문자열의 각 인덱스를 중심으로 팰린드롬 확장 시도
        for i in range(len(s)):

            # -------------------------
            # 1) 홀수 길이 팰린드롬 탐색
            #    예: "aba" → 중심: i
            # -------------------------
            l, r = i, i  # 중심이 같은 두 포인터
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 현재 팰린드롬이 기존 결과보다 길면 업데이트
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                # 양쪽으로 확장
                l -= 1
                r += 1

            # -------------------------
            # 2) 짝수 길이 팰린드롬 탐색
            #    예: "abba" → 중심: i, i+1
            # -------------------------
            l, r = i, i + 1  # 중심이 인접한 두 포인터
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 현재 팰린드롬이 기존 결과보다 길면 업데이트
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                # 양쪽으로 확장
                l -= 1
                r += 1

        # 저장한 시작 인덱스와 길이를 바탕으로 최종 결과 반환
        return s[resIdx : resIdx + resLen]
    
    # 2. Dynamic Programming 방식
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0  # 가장 긴 팰린드롬의 시작 인덱스와 길이
        n = len(s)

        # dp[i][j] = s[i:j+1]이 팰린드롬인지 여부를 저장하는 2차원 테이블
        dp = [[False] * n for _ in range(n)]

        # i를 뒤에서 앞으로 순회 (작은 부분 문자열부터 채워야 dp[i+1][j-1] 참조 가능)
        for i in range(n - 1, -1, -1):
            # j는 i부터 끝까지 순회 (부분 문자열의 끝 인덱스)
            for j in range(i, n):
                # s[i]와 s[j]가 같고,
                # 1) 길이가 3 이하인 경우(0, 1, 2) → 무조건 팰린드롬
                # 2) 길이가 4 이상이면 dp[i+1][j-1]이 True여야 함 (내부 문자열이 팰린드롬)
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True  # s[i:j+1]은 팰린드롬
                    # 현재 길이가 기존 최대 길이보다 크면 결과 갱신
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1

        # 저장된 시작 인덱스와 길이를 이용해 가장 긴 팰린드롬 부분 문자열 반환
        return s[resIdx : resIdx + resLen]

        
if __name__ == "__main__":
    sol = Solution()
    s = "ababd"
    print(sol.longestPalindrome(s))