'''
Valid Sudoku
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: false

for문 안에서 continue는 현재 반복을 건너뛰고 다음 반복으로 넘어가라는 의미
'''

class Solution:

    # 1) Brute Force
    # def isValidSudoku(self, board: list[list[str]]) -> bool:
    #     for row in range(9):
    #         seen = set()
    #         for i in range(9):
    #             if board[row][i] == ".": 
    #                 continue
    #             if board[row][i] in seen:
    #                 return False
    #             seen.add(board[row][i])
        
    #     for col in range(9):
    #         seen = set()
    #         for i in range(9):
    #             if board[i][col] == ".":
    #                 continue
    #             if board[i][col] in seen:
    #                 return False
    #             seen.add(board[i][col])
            
    #     for square in range(9):
    #         seen = set()
    #         for i in range(3):
    #             for j in range(3):
    #                 row = (square//3) * 3 + i
    #                 col = (square % 3) * 3 + j
    #                 if board[row][col] == ".":
    #                     continue
    #                 if board[row][col] in seen:
    #                     return False
    #                 seen.add(board[row][col])
    #     return True
    
    # 2) Bitmask
    # 2) Bitmask 방식으로 중복 검사 (O(1) 공간 활용)
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 각 행, 열, 3x3 박스를 나타내는 비트마스크 배열 (0~8)
        rows = [0] * 9       # 각 행에 어떤 숫자가 나왔는지 비트로 표현
        cols = [0] * 9       # 각 열에 어떤 숫자가 나왔는지 비트로 표현
        squares = [0] * 9    # 각 3x3 사각형에 어떤 숫자가 나왔는지 비트로 표현

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue  # 빈 칸은 건너뜀

                val = int(board[r][c]) - 1  # 1~9 숫자를 0~8로 변환 (비트 연산용)

                # 현재 숫자가 이미 해당 행에 존재하는 경우
                if (1 << val) & rows[r]:
                    return False
                # 현재 숫자가 이미 해당 열에 존재하는 경우
                if (1 << val) & cols[c]:
                    return False
                # 현재 숫자가 이미 해당 3x3 박스에 존재하는 경우
                square_index = (r // 3) * 3 + (c // 3)
                if (1 << val) & squares[square_index]:
                    return False

                # 현재 숫자를 해당 행/열/박스에 기록 (비트 ON)
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[square_index] |= (1 << val)

        # 모든 칸에 대해 중복 없이 검사 완료
        return True



if __name__ == "__main__":
    sol = Solution()

    board1 =[["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","8",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]]
    
    board2 =[["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","1",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]]
    
    print(sol.isValidSudoku(board1))
    print(sol.isValidSudoku(board2))