# Longest Repeating Character Replacement
# choose up to k characters of the string and replace them, return the length of the longest substring which contains only one distinct character
# Sliding Window Variable Size

# Solution 1
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

# Solution 2
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