# 4Sum
# array of all the unique quadruplets suct that total summation is target
# Two Pointers, kSum
from typing import List

def merge(left, right):
    result = []
    i = j = 0

    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    if(len(arr) <= 1):
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# Solution 1
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    nums[:] = merge_sort(nums)
    res = set()

    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        res.add((nums[a], nums[b], nums[c], nums[d]))
    return list(map(list, res))

# Solution 2
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums[:] = merge_sort(nums)
    res, quad = [], []

    def kSum(k, start, target):
        if k == 2:
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            return

        for i in range(start, len(nums) - k + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            quad.append(nums[i])
            kSum(k - 1, i + 1, target - nums[i])
            quad.pop()

    kSum(4, 0, target)
    return res

# ============================
# Test Case [3,2,3,-3,1,0], 3 -> [[-3,0,3,3],[-3,1,2,3]]
# ============================
if __name__ == "__main__":
    nums = [3,2,3,-3,1,0]
    target = 3
    res = fourSum(nums,target)

    print(res)