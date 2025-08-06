'''
Word Break II

You are given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "neetcode", wordDict = ["neet","code"]

Output: ["neet code"]

Example 2:

Input: s = "racecariscar", wordDict = ["racecar","race","car","is"]

Output: ["racecar is car","race car is car"]

Example 3:

Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]

Output: []
'''
from typing import List

# Backtracking
def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    wordDict = set(wordDict)

    def backtrack(i):
        if i == len(s):
            res.append(" ".join(cur)) # list
            return

        for j in range(i, len(s)):
            w = s[i:j + 1]
            if w in wordDict:
                cur.append(w)
                backtrack(j + 1)
                cur.pop()

    cur = []
    res = []
    backtrack(0)
    return res

# SH proof
def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    res = []
    real_res = []
    i = 0
    sent = ""

    if(len(s) == 0):
        return []

    for word in wordDict:
        if(word == s[:len(word)]):
            sent += word
            res1 = wordBreak(s[len(word):], wordDict)
            if(not res1):
                res.append(sent)
            sent += " "
            if(res1):
                for i in range(len(res1)):
                    res.append(sent + res1[i])
            sent = ""
    
    for i in range(len(res)):
        l = 0
        for c in range(len(res[i])):
            if(res[i][c] != " "):
                l += 1
        if(l == len(s)):
            real_res.append(res[i])
    
    return real_res

# ============================
# Test Case "racecariscar", ["racecar","race","car","is"] -> ["racecar is car", "race car is car"]
# ============================
if __name__ == "__main__":
    res = wordBreak("racecariscar", ["racecar","race","car","is"])
    
    print(res)