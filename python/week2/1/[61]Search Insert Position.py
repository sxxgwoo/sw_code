# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# Problem description
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Solution 1: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    """
    이진 탐색을 사용해 O(log n)에 처리하는 방법
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        # 중간값을 비교하여 탐색 범위를 좁힘
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # 찾지 못했으면 left가 “삽입 위치” 인덱스를 가리킴
    return left

# Test cases
print(searchInsert([1,3,5,6], 5)) # 2
print(searchInsert([1,3,5,6], 2)) # 1
print(searchInsert([1,3,5,6], 7)) # 4
print(searchInsert([1,3,5,6], 0)) # 0
print(searchInsert([1], 0)) # 0