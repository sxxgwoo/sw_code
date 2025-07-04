# container with most water
# maximum amount of water a container can store
# Two Pointers
from typing import List

# Solution 1
def maxArea(heights: List[int]) -> int:
    res = 0
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            res = max(res, min(heights[i], heights[j]) * (j - i))
    return res

# Solution 2
def maxArea(heights: List[int]) -> int:
    l, r = 0, len(heights) - 1
    res = 0

    while l < r:
        area = min(heights[l], heights[r]) * (r - l)
        res = max(res, area)
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    return res

# ============================
# Test Case [1,7,2,5,4,7,3,6] -> 36
# ============================
if __name__ == "__main__":
    heights = [1,7,2,5,4,7,3,6]
    res = maxArea(heights)

    print(res)