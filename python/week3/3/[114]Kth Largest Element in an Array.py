'''
Kth Largest Element in an Array

Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?

Example 1:

Input: nums = [2,3,1,5,4], k = 2

Output: 4

Example 2:

Input: nums = [2,3,1,1,5,5,4], k = 3

Output: 4
'''
from typing import List

# Sorting
def merge(lst1, lst2):
    i = j = 0
    res = []

    while i < len(lst1) and j < len(lst2):
        if(lst1[i] > lst2[j]):
            res.append(lst2[j])
            j += 1
        else:
            res.append(lst1[i])
            i += 1
    
    if(i == len(lst1)):
        res.extend(lst2[j:])
    if(j == len(lst2)):
        res.extend(lst1[i:])

    return res

def mergeSort(lst):
    if(len(lst) <= 1):
        return lst
    mid = len(lst) // 2
    res1 = mergeSort(lst[:mid])
    res2 = mergeSort(lst[mid:])

    return merge(res1, res2)

def findKthLargest(nums: List[int], k: int) -> int:
    res = mergeSort(nums)

    return res[-k]

# Quick Select
def findKthLargest(nums: List[int], k: int) -> int:
    k = len(nums) - k
    
    def quickSelect(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k: 
            return quickSelect(l, p - 1)
        elif p < k:
            return quickSelect(p + 1, r)
        else:
            return nums[p]

    return quickSelect(0, len(nums) - 1)

# ============================
# Test Case [2,3,1,1,5,5,4], 3 -> 4
# ============================
if __name__ == "__main__":
    res = findKthLargest([2,3,1,1,5,5,4], 3)
    
    print(res)