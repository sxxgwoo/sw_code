'''
Transpose Matrix

You are given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [
    [2,1],
    [-1,3]
]

Output: [
    [2,-1],
    [1,3]
]

Example 2:

Input: [
    [1,0,5],
    [2,4,3]
]

Output: [
    [1,2],
    [0,4],
    [5,3]
]
'''
from typing import List

# Iteration 1
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    ROWS, COLS = len(matrix), len(matrix[0])
    res = [[0] * ROWS for _ in range(COLS)]

    for r in range(ROWS):
        for c in range(COLS):
            res[c][r] = matrix[r][c]

    return res

# Iteration 2
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    ROWS, COLS = len(matrix), len(matrix[0])

    if ROWS == COLS:
        for r in range(ROWS):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        return matrix

    res = [[0] * ROWS for _ in range(COLS)]

    for r in range(ROWS):
        for c in range(COLS):
            res[c][r] = matrix[r][c]

    return res

# ============================
# Test Case [[1,0,5],[2,4,3]] -> [[1,2],[0,4],[5,3]]
# ============================
if __name__ == "__main__":
    res = transpose([[1,0,5],[2,4,3]])
    
    print(res)