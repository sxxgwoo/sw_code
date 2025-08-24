'''
Set Matrix Zeroes

Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Follow up: Could you solve it using O(1) space?

Example 1:

Input: matrix = [
    [0,1],
    [1,0]
    ]

Output: [
    [0,0],
    [0,0]
    ]
Example 2:

Input: matrix = [
    [1,2,3],
    [4,0,5],
    [6,7,8]
    ]

Output: [
    [1,0,3],
    [0,0,0],
    [6,0,8]
    ]
'''
from typing import List

# SH proof
def setZeroes(matrix: List[List[int]]) -> None:
    row = set()
    col = set()

    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if(matrix[i][j] == 0):
                row.add(i)
                col.add(j)
    
    for r in row:
        for j in range(n):
            matrix[r][j] = 0
    
    for c in col:
        for i in range(m):
            matrix[i][c] = 0

# Iteration (Space Optimized)
def setZeroes(matrix: List[List[int]]) -> None:
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True

    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0

# ============================
# Test Case [[1,2,3],[4,0,5],[6,7,8]] -> [[1,0,3],[0,0,0],[6,0,8]]
# ============================
if __name__ == "__main__":
    matrix = [[1,2,3],[4,0,5],[6,7,8]]
    setZeroes(matrix)
    
    print(matrix)