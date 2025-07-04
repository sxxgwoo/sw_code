# Permutation in String
# return true if s2 contains a permutation of s1
# Sliding Window Variable Size

def merge(left, right):
    res = ""
    i = j = 0

    while i < len(left) and j < len(right):
        if(left[i] < right[j]):
            res += left[i]
            i += 1
        else:
            res += right[j]
            j += 1
    
    res += left[i:]
    res += right[j:]

    return res

def merge_sort(s):
    if(len(s) <= 1):
        return s
    
    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])

    return merge(left, right)

# Solution 1
def checkInclusion(s1: str, s2: str) -> bool:
    s1 = merge_sort(s1)

    for i in range(len(s2)):
        for j in range(i, len(s2)):
            subStr = s2[i : j + 1]
            subStr = merge_sort(subStr)
            if subStr == s1:
                return True
    return False

# Solution 2
def checkInclusion(s1: str, s2: str) -> bool:
    count1 = {}
    for c in s1:
        count1[c] = 1 + count1.get(c, 0)
    
    need = len(count1)
    for i in range(len(s2)):
        count2, cur = {}, 0
        for j in range(i, len(s2)):
            count2[s2[j]] = 1 + count2.get(s2[j], 0)
            if count1.get(s2[j], 0) < count2[s2[j]]:
                break
            if count1.get(s2[j], 0) == count2[s2[j]]:
                cur += 1
            if cur == need:
                return True
    return False

# ============================
# Test Case "abc", "lecabee" -> true
# ============================
if __name__ == "__main__":
    s1 = "abc"
    s2 = "lecabee"
    res = checkInclusion(s1,s2)

    print(res)