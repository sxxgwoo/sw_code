'''
Word Search
Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true
Example 2:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: false
'''
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])  # 보드의 행, 열 크기

        # DFS 함수 정의: (r,c)에서 word[i:]를 찾을 수 있는지 확인
        def dfs(r, c, i):
            # 1) 단어를 전부 찾았으면 True
            if i == len(word):
                return True
            # 2) 범위 벗어나거나, 이미 방문했거나, 글자가 다르면 False
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            # 현재 칸 방문 처리 (재방문 방지)
            temp = board[r][c]
            board[r][c] = '#'

            # 상하좌우 탐색
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            # 탐색 후 복원 (백트래킹)
            board[r][c] = temp
            return res

        # 모든 위치를 시작점으로 시도
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):  # (r,c)에서 시작해 word[0:] 찾기
                    return True
        return False


if __name__=="__main__":
    sol = Solution()
    board = [
        ["A","B","C","D"],
        ["S","A","A","T"],
        ["A","C","A","E"]
    ]
    word = "CAT"
    print(sol.exist(board, word))  # True
    