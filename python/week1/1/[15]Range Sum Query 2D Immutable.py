# Range Sum Query 2D - Immutable
# 문제 설명: 2차원 배열 matrix가 주어지면, 주어진 범위의 합을 반환하는 함수를 작성하세요.
# 입력: matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
# 출력: 8
# 설명: 주어진 범위의 합은 8입니다.

from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        """
        Build a 2D prefix‐sum (summed-area) table `ps` such that
        ps[i+1][j+1] = sum of all matrix[x][y] for 0 <= x <= i, 0 <= y <= j.
        """
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        # ps has dimensions (m+1) x (n+1), initialized to 0
        self.ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += matrix[i][j]
                # ps(i+1, j+1) = row_sum of this row + ps above
                self.ps[i+1][j+1] = row_sum + self.ps[i][j+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Return sum of elements in the rectangle
        with upper‐left (row1, col1) and lower‐right (row2, col2).
        Using inclusion–exclusion on ps:
            A = ps[row2+1][col2+1]
            B = ps[row1][col2+1]
            C = ps[row2+1][col1]
            D = ps[row1][col1]
        sum = A - B - C + D
        """
        A = self.ps[row2+1][col2+1]
        B = self.ps[row1][col2+1]
        C = self.ps[row2+1][col1]
        D = self.ps[row1][col1]
        return A - B - C + D
    
# test case
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
numMatrix = NumMatrix(matrix)
print(numMatrix.sumRegion(2, 1, 4, 3)) # 8
print(numMatrix.sumRegion(1, 1, 2, 2)) # 11
print(numMatrix.sumRegion(1, 2, 2, 4)) # 12