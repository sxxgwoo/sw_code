'''
Generate Parentheses
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]

Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
You may return the answer in any order.
'''
from typing import List

# Brute Force
def generateParenthesis(n: int) -> List[str]:
    res = []

    def valid(s: str):
        open = 0
        for c in s:
            open += 1 if c == '(' else -1
            if open < 0:
                return False
        return not open

    def dfs(s: str):
        if n * 2 == len(s):
            if valid(s):
                res.append(s)
            return
        
        dfs(s + '(')
        dfs(s + ')')
    
    dfs("")
    return res

# Dynamic Programming
def generateParenthesis(n):
    res = [[] for _ in range(n+1)]
    res[0] = [""]
    
    for k in range(n + 1):
        for i in range(k):
            for left in res[i]:
                for right in res[k-i-1]:
                    res[k].append("(" + left + ")" + right)
    
    return res[-1]

# ============================
# Test Case n = 3 -> ["((()))","(()())","(())()","()(())","()()()"]
# ============================
if __name__ == "__main__":
    res = generateParenthesis(3)

    print(res)