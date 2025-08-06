'''
Island Perimeter
#matrix DFS #matrix BFS
You are given a row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1.

Return the perimeter of the island.

Example 1:



Input: grid = [
    [1,1,0,0],
    [1,0,0,0],
    [1,1,1,0],
    [0,0,1,1]
]

Output: 18
Explanation: The perimeter is the 18 red stripes shown in the image above.

Example 2:

Input: grid = [[1,0]]

Output: 4
'''
# 간단한 Queue 클래스 구현 (FIFO)
class Queue:
    def __init__(self):
        self.data = []

    def append(self, val):
        self.data.append(val)

    def popleft(self):
        if self.data:
            return self.data.pop(0)  # O(n) 시간복잡도
        raise IndexError("pop from empty queue")

    def __len__(self):
        return len(self.data)

    def __bool__(self):
        return bool(self.data)
class Solution:
    # 1) DFS
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0

            visit.add((i, j))
            perim = dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i - 1, j)
            return perim

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i, j)
        return 0
    
    # 2) BFS (직접 구현한 Queue 사용)
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()  # 방문한 육지 좌표 저장
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북

        def bfs(r, c):
            queue = Queue()
            queue.append((r, c))
            visited.add((r, c))
            perimeter = 0

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    # 1) 범위 밖이거나 물(0)이면 둘레 +1
                    if (nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] == 0):
                        perimeter += 1
                    # 2) 육지이고 아직 방문 안했으면 큐에 추가
                    elif (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))

            return perimeter

        # 육지(1) 찾으면 BFS 시작
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return bfs(i, j)
        return 0
    
    # 3) Iteration
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += (i + 1 >= m or grid[i + 1][j] == 0)
                    res += (j + 1 >= n or grid[i][j + 1] == 0)
                    res += (i - 1 < 0 or grid[i - 1][j] == 0)
                    res += (j - 1 < 0 or grid[i][j - 1] == 0)
        return res
    
if __name__=="__main__":
    sol = Solution()
    grid = [
        [1,1,0,0],
        [1,0,0,0],
        [1,1,1,0],
        [0,0,1,1]
    ]
    print(sol.islandPerimeter(grid))