'''
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3

Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
'''

# Brute Force
def lengthOfLongestSubstring(s: str) -> int:
    res = 0
    for i in range(len(s)):
        charSet = set()
        for j in range(i, len(s)):
            if s[j] in charSet:
                break
            charSet.add(s[j])
        res = max(res, len(charSet))
    return res

# Sliding Window
def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

# ============================
# Test Case "zxyzxyz" -> 3
# ============================
if __name__ == "__main__":
    s = "zxyzxyz"
    res = lengthOfLongestSubstring(s)

    print(res)