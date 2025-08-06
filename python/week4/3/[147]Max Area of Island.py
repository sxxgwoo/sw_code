'''
Max Area of Island

You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.

Example 1:

Input: grid = [
[0,1,1,0,1],
[1,0,1,0,1],
[0,1,1,0,1],
[0,1,0,0,1]
]

Output: 6

Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.
'''
from typing import List

# Depth First Search
def maxAreaOfIsland(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()

    def dfs(r, c):
        if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r, c) in visit):
            return 0
        visit.add((r, c))
        return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

    area = 0
    for r in range(ROWS):
        for c in range(COLS):
            area = max(area, dfs(r, c))
    return area

# SH proof
def maxAreaOfIsland(grid: List[List[int]]) -> int:
    used = set()
    area = 0
    rownum = len(grid)
    colnum = len(grid[0])

    def dfs(i,j):
        used.add((i,j))
        a = 1
        if(j < colnum-1 and grid[i][j+1] == 1 and (i,j+1) not in used):
            used.add((i,j+1))
            a += dfs(i,j+1)
        if(j > 0 and grid[i][j-1] == 1 and (i,j-1) not in used):
            used.add((i,j-1))
            a += dfs(i,j-1)
        if(i < rownum-1 and grid[i+1][j] == 1 and (i+1,j) not in used):
            used.add((i+1,j))
            a += dfs(i+1,j)
        if(i > 0 and grid[i-1][j] == 1 and (i-1,j) not in used):
            used.add((i-1,j))
            a += dfs(i-1,j)
        return a

    for i in range(rownum):
        for j in range(colnum):
            if(grid[i][j] == 1 and (i,j) not in used):
                area = max(area, dfs(i,j))
    
    return area

# ============================
# Test Case [[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]] -> 6
# ============================
if __name__ == "__main__":
    res = maxAreaOfIsland([[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]])
    
    print(res)