'''
Edit Distance

You are given two strings word1 and word2, each consisting of lowercase English letters.

You are allowed to perform three operations on word1 an unlimited number of times:

Insert a character at any position
Delete a character at any position
Replace a character at any position
Return the minimum number of operations to make word1 equal word2.

Example 1:

Input: word1 = "monkeys", word2 = "money"

Output: 2

Explanation:
monkeys -> monkey (remove s)
monkey -> monkey (remove k)

Example 2:

Input: word1 = "neatcdee", word2 = "neetcode"

Output: 3

Explanation:
neatcdee -> neetcdee (replace a with e)
neetcdee -> neetcde (remove last e)
neetcde -> neetcode (insert o)
'''

# Dynamic Programming (Bottom-Up)
def minDistance(word1: str, word2: str) -> int:
    n = len(word1)
    m = len(word2)

    dp = [[0] * (m+1) for _ in range(n+1)] # word1[:i]와 word2[:j] 부분 문자열을 일치시키기 위해 필요한 최소 편집 거리

    for i in range(n+1):
        for j in range(m+1):
            if(i == 0 or j == 0):
                dp[i][j] = i + j
            else:
                if(word1[i-1] == word2[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
    
    return dp[n][m]

# Recursion
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)

    def dfs(i, j): # word1[i:]와 word2[j:] 부분 문자열을 일치시키기 위해 필요한 최소 편집 거리
        if i == m:
            return n - j
        if j == n:
            return m - i
        if word1[i] == word2[j]:
            return dfs(i + 1, j + 1)
        res = min(dfs(i + 1, j), dfs(i, j + 1))
        res = min(res, dfs(i + 1, j + 1))
        return res + 1

    return dfs(0, 0)

# ============================
# Test Case "monkeys", "money" -> 2
# ============================
if __name__ == "__main__":
    res = minDistance("monkeys", "money")
    
    print(res)