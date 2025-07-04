# Longest Substring Without Repeating Characters
# length of the longest substring without duplicate characters
# Sliding Window Variable Size

# Solution 1
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

# Solution 2
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