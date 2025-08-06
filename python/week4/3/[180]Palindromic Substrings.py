'''
Palindromic Substrings

Given a string s, return the number of substrings within s that are palindromes.

A palindrome is a string that reads the same forward and backward.

Example 1:

Input: s = "abc"

Output: 3

Explanation: "a", "b", "c".

Example 2:

Input: s = "aaa"

Output: 6

Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.
'''

# Brute Force
def countSubstrings(s: str) -> int:
    res = 0
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            l, r = i, j
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
            res += (l >= r)
            
    return res

# Two Pointers
def countSubstrings(s: str) -> int:
    res = 0
    
    for i in range(len(s)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

        # even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
    
    return res

# ============================
# Test Case "aaa" -> 6
# ============================
if __name__ == "__main__":
    res = countSubstrings("aaa")
    
    print(res)