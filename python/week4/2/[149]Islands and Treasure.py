'''
Islands and Treasure, Walls and Gates
You are given a mxn 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
'''
'''
Islands and Treasure (Walls and Gates)
문제 요약:
- 주어진 grid에서
  - -1 : 물 (이동 불가)
  - 0  : 보물 상자
  - INF(2147483647) : 육지 (이동 가능)
- 각 육지 칸에 대해 가장 가까운 보물 상자까지의 거리를 채움
- 도달 불가능하면 INF 그대로 유지
- 상하좌우로만 이동 가능
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
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4방향 탐색
        INF = 2147483647

        # 특정 육지 칸 (r, c)에서 BFS로 가장 가까운 보물까지 거리 찾기
        def bfs(r, c):
            q = Queue()
            q.append((r, c))
            visit = [[False] * COLS for _ in range(ROWS)]  # 방문 여부 체크
            visit[r][c] = True
            steps = 0  # 현재 BFS 탐색 거리

            # BFS 시작
            while q:
                # 현재 거리 단계의 모든 노드 탐색
                for _ in range(len(q)):
                    row, col = q.popleft()

                    # 보물(0)을 만나면 현재까지 걸린 steps 반환
                    if grid[row][col] == 0:
                        return steps

                    # 4방향 탐색
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        # 범위 내, 미방문, 물(-1) 아님
                        if (0 <= nr < ROWS and 0 <= nc < COLS and
                            not visit[nr][nc] and grid[nr][nc] != -1
                        ):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                steps += 1  # 한 단계 더 이동

            return INF  # 보물에 도달할 수 없으면 INF 반환

        # 모든 육지(INF)에 대해 BFS 실행
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)


if __name__=="__main__":
    sol = Solution()
    grid = [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
    ]
    sol.islandsAndTreasure(grid)
    print(grid)
    # 출력:
    # [
    #   [3,-1,0,1],
    #   [2,2,1,-1],
    #   [1,-1,2,-1],
    #   [0,-1,3,4]
    # ]