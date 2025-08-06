'''
Rotting Fruit

You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit

Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

Example 1:

Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

Output: 4

Example 2:

Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

Output: -1
'''
from typing import List
from collections import deque

# SH proof (Breadth First Search)
def orangesRotting(grid: List[List[int]]) -> int:
    rownum = len(grid)
    colnum = len(grid[0])
    t = 0
    q = deque()

    for i in range(rownum):
        for j in range(colnum):
            if(grid[i][j] == 2):
                q.append((i,j,t))
    
    while q:
        i,j,t = q.popleft()

        if(i < rownum - 1 and grid[i+1][j] == 1):
            grid[i+1][j] = 2
            q.append((i+1,j,t+1))

        if(i > 0 and grid[i-1][j] == 1):
            grid[i-1][j] = 2
            q.append((i-1,j,t+1))

        if(j > 0 and grid[i][j-1] == 1):
            grid[i][j-1] = 2
            q.append((i,j-1,t+1))

        if(j < colnum - 1 and grid[i][j+1] == 1):
            grid[i][j+1] = 2
            q.append((i,j+1,t+1))

    for i in range(rownum):
        if(1 in grid[i]):
            return -1
    
    return t

# Breadth First Search (No Queue)
def orangesRotting(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    fresh = 0
    time = 0

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while fresh > 0:
        flag = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        if (row in range(ROWS) and col in range(COLS) and grid[row][col] == 1):
                            grid[row][col] = 3  
                            fresh -= 1
                            flag = True

        if not flag:
            return -1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 3:
                    grid[r][c] = 2  

        time += 1

    return time

# ============================
# Test Case [[1,1,0],[0,1,1],[0,1,2]] -> 4
# ============================
if __name__ == "__main__":
    res = orangesRotting([[1,1,0],[0,1,1],[0,1,2]])
    
    print(res)