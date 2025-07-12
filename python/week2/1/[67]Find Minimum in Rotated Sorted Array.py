# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Problem description
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

# Solution 1: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

def findMin(nums: List[int]) -> int:
    """
    회전된 정렬 배열에서 최소값을 찾는 O(log n) 이진 탐색
    """
    left, right = 0, len(nums) - 1
    
    # left < right 구간에 최소값이 숨어 있음
    while left < right:
        mid = (left + right) // 2
        # 중간값이 우측 끝값보다 크다면, 최소값은 mid 오른쪽에 있음
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # 그렇지 않으면 mid가 포함된 왼쪽 구간에 최소값이 있음
            right = mid
    
    # left == right 가 최소값 인덱스
    return nums[left]

# Test cases
print(findMin([3,4,5,1,2])) # 1
print(findMin([4,5,6,7,0,1,2])) # 0
print(findMin([11,13,15,17])) # 11