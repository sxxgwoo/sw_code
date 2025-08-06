'''
Combination Sum II

You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

Input: candidates = [9,2,2,4,6,1,5], target = 8

Output: [
[1,2,5],
[2,2,4],
[2,6]
]
Example 2:

Input: candidates = [1,2,3,4,5], target = 7

Output: [
[1,2,4],
[2,5],
[3,4]
]
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

def combinationSum2(candidates, target):
    res = set()
    candidates = mergeSort(candidates)

    def generate_subsets(i, cur, total):
        if total == target:
            res.add(tuple(cur))  
            return
        if total > target or i == len(candidates):
            return

        cur.append(candidates[i])
        generate_subsets(i + 1, cur, total + candidates[i])
        cur.pop()

        generate_subsets(i + 1, cur, total)

    generate_subsets(0, [], 0)
    return [list(combination) for combination in res]

# Backtracking
def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates = mergeSort(candidates)

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if total > target or i == len(candidates):
            return
        
        cur.append(candidates[i])
        dfs(i + 1, cur, total + candidates[i])
        cur.pop()
        
        while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1
        dfs(i + 1, cur, total)
        
    dfs(0, [], 0)
    return res

# ============================
# Test Case [1,2,3,4,5], 7 -> [[1,2,4], [2,5], [3,4]]
# ============================
if __name__ == "__main__":
    res = combinationSum2([1,2,3,4,5], 7)
    
    print(res)