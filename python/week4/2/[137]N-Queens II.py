'''
N-Queens II
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

You are given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:



Input: n = 4

Output: 2
Explanation: There are two different solutions to the 4-queens puzzle.

Example 2:

Input: n = 1

Output: 1
'''

'''
N-Queens II
문제 설명:
- n x n 체스판에 n개의 퀸을 배치해야 한다.
- 모든 퀸은 서로 공격할 수 없어야 한다. (같은 행, 같은 열, 대각선 X)
- 가능한 배치의 경우의 수를 반환한다.
'''

class Solution:
    # Backtracking
    def totalNQueens(self, n: int) -> int:
        res = 0  # 가능한 배치 경우의 수 저장
        board = [["."] * n for i in range(n)]  # n x n 체스판 초기화, '.'는 빈칸
        
        # 백트래킹 함수: r번째 행에 퀸을 배치
        def backtrack(r):
            nonlocal res
            # 모든 행에 퀸을 배치했다면 경우의 수 +1
            if r == n:
                res += 1
                return
            
            # r번째 행의 모든 열에 퀸을 놓아본다
            for c in range(n):
                # (r, c)에 퀸을 놓을 수 있는지 확인
                if self.isSafe(r, c, board):
                    board[r][c] = "Q"    # 퀸 배치
                    backtrack(r + 1)     # 다음 행으로 이동
                    board[r][c] = "."    # 원상 복구 (백트래킹)
        
        backtrack(0)
        return res

    # 현재 위치 (r, c)에 퀸을 놓을 수 있는지 확인
    def isSafe(self, r: int, c: int, board):
        # 1) 같은 열 확인 (위쪽만 보면 됨)
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1
        
        # 2) 왼쪽 대각선 확인 (↖ 방향)
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        
        # 3) 오른쪽 대각선 확인 (↗ 방향)
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        
        return True  # 모든 방향 안전하면 True 반환
        
if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(sol.totalNQueens(n))  # 출력: 2
    