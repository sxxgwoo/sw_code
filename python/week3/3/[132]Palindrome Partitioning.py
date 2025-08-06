'''
Palindrome Partitioning

Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

You may return the solution in any order.

Example 1:

Input: s = "aab"

Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"

Output: [["a"]]
'''
from typing import List

# SH proof
def isPalindrome(s):
    if(len(s) <= 1):
        return True
    
    for i in range(len(s) // 2 + 1):
        if(s[i] != s[len(s) - 1 - i]):
            return False
    
    return True

def partition(s: str) -> List[List[str]]:
    if(len(s) == 1):
        return [[s]]

    res = set()

    if(isPalindrome(s[:])):
        res.add(tuple([s[:]]))
    
    n = len(s)
    for i in range(1,n):
        res1 = partition(s[:i])
        res2 = partition(s[i:])

        if(res1 and res2):
            for j in res1:
                for k in res2:
                    lst = list(j) + list(k)
                    res.add(tuple(lst))
    
    res3 = []
    for st in res:
        res3.append(list(st))
    
    return res3

# Backtracking
def isPali(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True

def partition(s: str) -> List[List[str]]:
    res, part = [], []

    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            if isPali(s, i, j):
                part.append(s[i : j + 1])
                dfs(j + 1)
                part.pop()

    dfs(0)
    return res

# ============================
# Test Case "aab" -> [["a","a","b"],["aa","b"]]
# ============================
if __name__ == "__main__":
    res = partition("aab")
    
    print(res)