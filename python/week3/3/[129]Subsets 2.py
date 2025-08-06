'''
Subsets II

You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,1]

Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

Example 2:

Input: nums = [7,7]

Output: [[],[7], [7,7]]
'''
from typing import List

# Brute Force
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

    n = len(lst) // 2

    lst1 = mergeSort(lst[:n])
    lst2 = mergeSort(lst[n:])

    return merge(lst1, lst2)

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = set()

    def backtrack(i, subset):
        if i == len(nums):
            res.add(tuple(subset))
            return

        subset.append(nums[i])
        backtrack(i + 1, subset)
        subset.pop()
        backtrack(i + 1, subset)

    nums = mergeSort(nums)
    backtrack(0, [])
    return [list(s) for s in res]

# Backtracking
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = []
    nums = mergeSort(nums)

    def backtrack(i, subset):
        if i == len(nums):
            res.append(subset[::])
            return

        subset.append(nums[i])
        backtrack(i + 1, subset)
        subset.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1, subset)

    backtrack(0, [])
    return res

# ============================
# Test Case [1,2,1] -> [[],[1],[1,2],[1,1],[1,2,1],[2]]
# ============================
if __name__ == "__main__":
    res = subsetsWithDup([1,2,1])
    
    print(res)