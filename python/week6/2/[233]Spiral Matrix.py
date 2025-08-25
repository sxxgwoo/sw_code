'''
Spiral Matrix
Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.

Example 1:



Input: matrix = [[1,2],[3,4]]

Output: [1,2,4,3]
Example 2:



Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [1,2,3,6,9,8,7,4,5]
Example 3:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution:
    # 1. Optimal (방향 벡터 + steps 배열 이용)
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []

        # 시계 방향 순서로 이동 방향 정의
        # 오른쪽 → 아래 → 왼쪽 → 위
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # steps[0] = 가로 이동 횟수 (열 개수)
        # steps[1] = 세로 이동 횟수 (행 개수 - 1)
        # 이후 한 방향을 다 돌 때마다 steps[d&1]을 줄여줌
        steps = [len(matrix[0]), len(matrix) - 1]

        r, c, d = 0, -1, 0   # 시작점은 (0, -1)에서 오른쪽으로 이동 시작
        while steps[d & 1]:
            # 현재 방향으로 steps[d&1] 만큼 이동
            for i in range(steps[d & 1]):
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            # 해당 방향의 길이 1 줄이기
            steps[d & 1] -= 1
            # 방향을 시계방향으로 변경
            d = (d + 1) % 4
        return res
    
    # 2. Iteration (경계값 네 개를 두고 좁혀가기)
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []

        # 경계값 초기화
        left, right = 0, len(matrix[0])   # 열의 좌우 경계
        top, bottom = 0, len(matrix)      # 행의 상하 경계

        while left < right and top < bottom:
            # 1) 위쪽 행(left → right-1)
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1  # 위쪽 행은 다 썼으니 한 칸 내려옴

            # 2) 오른쪽 열(top → bottom-1)
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1  # 오른쪽 열은 다 썼으니 왼쪽으로 이동

            # 더 이상 남은 영역이 없으면 종료
            if not (left < right and top < bottom):
                break

            # 3) 아래쪽 행(right-1 → left)
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1  # 아래쪽 행은 다 썼으니 위로 이동

            # 4) 왼쪽 열(bottom-1 → top)
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1  # 왼쪽 열은 다 썼으니 오른쪽으로 이동

        return res


# 실행 예시
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(sol.spiralOrder(matrix))  # [1,2,3,4,8,12,11,10,9,5,6,7]