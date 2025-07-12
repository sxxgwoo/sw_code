# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# Problem description
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Solution 1: Binary Search
# Time Complexity: O(log(m·n))
# Space Complexity: O(1)

from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    가상 1차원 배열로 보고 이진 탐색을 수행하는 O(log(m·n)) 풀이
    """
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        # 1차원 인덱스를 2차원 인덱스로 변환
        row = mid // n
        col = mid % n
        val = matrix[row][col]
        
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Test cases
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # True
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # False