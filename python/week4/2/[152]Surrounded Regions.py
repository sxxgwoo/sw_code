'''
Surrounded Regions
You are given a 2-D matrix board containing 'X' and 'O' characters.

If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.

Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.

Example 1:



Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]

Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","O"]
]
Explanation: Note that regions that are on the border are not considered surrounded regions.
'''
# 간단한 Queue 클래스 구현 (FIFO)
class Queue:
    def __init__(self):
        self.data = []

    def append(self, val):
        self.data.append(val)  # 큐의 맨 뒤에 데이터 삽입

    def popleft(self):
        if self.data:
            return self.data.pop(0)  # 큐의 맨 앞 데이터 꺼내기 (O(n))
        raise IndexError("pop from empty queue")

    def __len__(self):
        return len(self.data)       # 현재 큐의 길이 반환

    def __bool__(self):
        return bool(self.data)      # 큐가 비었는지 여부 반환
    
    
class Solution:
    # 1) BFS
    def solve(self, board: list[list[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상하좌우

        def BFS():
            q = Queue()
            # 1️⃣ 우선 테두리(가장자리)에 있는 'O'를 모두 큐에 추가
            for r in range(ROWS):
                for c in range(COLS):
                    # 테두리 위치 확인
                    if (r == 0 or r == ROWS - 1 or
                        c == 0 or c == COLS - 1) and board[r][c] == "O":
                        q.append((r, c))
            
            # 2️⃣ 테두리에서 시작해서 연결된 모든 'O'를 'T'로 바꾼다
            while q:
                r, c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"  # 임시로 표시해서 살아남을 'O'
                    # 상하좌우 탐색
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        # 범위 안이면 큐에 추가
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            q.append((nr, nc))

        BFS()

        # 3️⃣ 남은 'O'는 모두 X로 바꾸고, 'T'는 다시 O로 복원
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"  # 완전히 둘러싸인 영역
                elif board[r][c] == "T":
                    board[r][c] = "O"  # 테두리와 연결된 영역 복원

    # 2) DFS
    def solve(self, board: list[list[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        # DFS로 테두리와 연결된 O를 T로 바꿔서 표시
        def DFS(r, c):
            # 범위를 벗어나거나 O가 아니면 종료
            if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != "O"
            ):
                return
            
            board[r][c] = "T"  # 안전한 영역을 임시로 표시

            # 상하좌우로 계속 DFS 확장
            DFS(r + 1, c)  # 아래
            DFS(r - 1, c)  # 위
            DFS(r, c + 1)  # 오른쪽
            DFS(r, c - 1)  # 왼쪽

        # 1️⃣ 왼쪽·오른쪽 테두리 탐색
        for r in range(ROWS):
            if board[r][0] == "O":          # 왼쪽 테두리
                DFS(r, 0)
            if board[r][COLS - 1] == "O":   # 오른쪽 테두리
                DFS(r, COLS - 1)

        # 2️⃣ 위·아래 테두리 탐색
        for c in range(COLS):
            if board[0][c] == "O":          # 위쪽 테두리
                DFS(0, c)
            if board[ROWS - 1][c] == "O":   # 아래쪽 테두리
                DFS(ROWS - 1, c)

        # 3️⃣ 최종 변환
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"  # 테두리와 연결되지 않은 O → X로 변환
                elif board[r][c] == "T":
                    board[r][c] = "O"  # 테두리와 연결된 O → 원래 상태로 복원

if __name__=="__main__":
    sol = Solution()
    board = [
      ["X","X","X","X"],
      ["X","O","O","X"],
      ["X","O","O","X"],
      ["X","X","X","O"]
    ] 
    sol.solve(board)
    print(board)