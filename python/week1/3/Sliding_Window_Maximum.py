# Sliding Window Maximum
# return a list that contains the maximum element in the window at each step
# Sliding Window Variable Size
from typing import List

# Solution 1
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    output = []

    for i in range(len(nums) - k + 1):
        maxi = nums[i]
        for j in range(i, i + k):
            maxi = max(maxi, nums[j])
        output.append(maxi)

    return output

# Solution 2
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    leftMax = [0] * n
    rightMax = [0] * n

    leftMax[0] = nums[0]
    rightMax[n - 1] = nums[n - 1]

    for i in range(1, n):
        if i % k == 0:
            leftMax[i] = nums[i]
        else:
            leftMax[i] = max(leftMax[i - 1], nums[i])

        if (n - 1 - i) % k == 0:
            rightMax[n - 1 - i] = nums[n - 1 - i]
        else:
            rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - 1 - i])

    output = [0] * (n - k + 1)

    for i in range(n - k + 1):
        output[i] = max(leftMax[i + k - 1], rightMax[i])

    return output

# ============================
# Test Case [1,2,1,0,4,2,6], 3 -> [2,2,4,4,6]
# ============================
if __name__ == "__main__":
    nums = [1,2,1,0,4,2,6]
    k = 3
    res = maxSlidingWindow(nums, k)

    print(res)