'''
Find the Duplicate Number

You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

Example 1:

Input: nums = [1,2,3,2,2]

Output: 2

Example 2:

Input: nums = [1,2,3,4,4]

Output: 4
Follow-up: Can you solve the problem without modifying the array nums and using 
O(1) extra space?
'''
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


# Sorting
def findDuplicate(nums: List[int]) -> int:
    merge_sort(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]
    return -1

# Hash Set
def findDuplicate(nums: List[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

# ============================
# Test Case [1,2,3,2,2] -> 2
# ============================
if __name__ == "__main__":
    res = findDuplicate([1,2,3,2,2])

    print(res)