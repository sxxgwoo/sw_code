'''
Extra Characters in a String

You are given a string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

Note that the same word in the dictionary may be reused multiple times.

Example 1:

Input: s = "neetcodes", dictionary = ["neet","code","neetcode"]

Output: 1

Explanation: The optimal way is to break s into two substrings: "neet" from index 0 to 3 and "code" from index 4 to 7. There is one character which is at index 8.

Example 2:

Input: s = "neetcodde", dictionary = ["neet","code","neetcode"]

Output: 5

Explanation: The optimal way is to break s into one substring: "neet" from index 0 to 3. The characters at indices from 4 to 8 are extra.
'''
from typing import List

# Dynamic Programming (Top-Down) Using Hash Set
def minExtraChar(s: str, dictionary: List[str]) -> int:
    words = set(dictionary)
    dp = {len(s): 0}

    def dfs(i):
        if i in dp:
            return dp[i]
        res = 1 + dfs(i + 1)
        for j in range(i, len(s)):
            if s[i:j + 1] in words:
                res = min(res, dfs(j + 1))
        dp[i] = res
        return res

    return dfs(0)

# Dynamic Programming (Bottom-Up) Using Hash Set
def minExtraChar(s: str, dictionary: List[str]) -> int:
    words = set(dictionary)
    n = len(s)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        dp[i] = 1 + dp[i + 1]
        for j in range(i, n):
            if s[i:j + 1] in words:
                dp[i] = min(dp[i], dp[j + 1])
    return dp[0]

# ============================
# Test Case "leetscode", ["leet","code","leetcode"] -> 1
# ============================
if __name__ == "__main__":
    res = minExtraChar("leetscode", ["leet","code","leetcode"])
    
    print(res)