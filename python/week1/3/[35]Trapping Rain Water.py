'''
Trapping Rain Water

You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:

Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
'''
from typing import List

# Prefix & Suffix Arrays
def trap(height: List[int]) -> int:
    n = len(height)
    if n == 0:
        return 0
    
    leftMax = [0] * n
    rightMax = [0] * n
    
    leftMax[0] = height[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], height[i])
    
    rightMax[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], height[i])
    
    res = 0
    for i in range(n):
        res += min(leftMax[i], rightMax[i]) - height[i]
    return res

# Two Pointers
def trap(height: List[int]) -> int:
    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res

# ============================
# Test Case [0,2,0,3,1,0,1,3,2,1] -> 9
# ============================
if __name__ == "__main__":
    height = [0,2,0,3,1,0,1,3,2,1]
    res = trap(height)

    print(res)