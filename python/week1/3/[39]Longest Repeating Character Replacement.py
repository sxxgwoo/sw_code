'''
Longest Repeating Character Replacement

You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4

Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
'''

# Brute Force
def characterReplacement(s: str, k: int) -> int:
    res = 0
    for i in range(len(s)):
        count, maxf = {}, 0
        for j in range(i, len(s)):
            count[s[j]] = 1 + count.get(s[j], 0)
            maxf = max(maxf, count[s[j]])
            if (j - i + 1) - maxf <= k:
                res = max(res, j - i + 1)
    return res

# Sliding Window
def characterReplacement(s: str, k: int) -> int:
    res = 0
    charSet = set(s)

    for c in charSet:
        count = l = 0
        for r in range(len(s)):
            if s[r] == c:
                count += 1

            while (r - l + 1) - count > k:
                if s[l] == c:
                    count -= 1
                l += 1
                
            res = max(res, r - l + 1)
    return res

# ============================
# Test Case "AAABABB", 1 -> 5
# ============================
if __name__ == "__main__":
    s = "AAABABB"
    k = 1
    res = characterReplacement(s,k)

    print(res)