'''
Swim in Rising Water

You are given a square 2-D matrix of distinct integers grid where each integer grid[i][j] represents the elevation at position (i, j).

Rain starts to fall at time = 0, which causes the water level to rise. At time t, the water level across the entire grid is t.

You may swim either horizontally or vertically in the grid between two adjacent squares if the original elevation of both squares is less than or equal to the water level at time t.

Starting from the top left square (0, 0), return the minimum amount of time it will take until it is possible to reach the bottom right square (n - 1, n - 1).

Example 1:

Input: grid = [[0,1],[2,3]]

Output: 3

Explanation: For a path to exist to the bottom right square grid[1][1] the water elevation must be at least 3. At time t = 3, the water level is 3.

Example 2:

Input: grid = [
    [0,1,2,10],
    [9,14,4,13],
    [12,3,8,15],
    [11,5,7,6]]
    ]

Output: 8

Explanation: The water level must be at least 8 to reach the bottom right square. The path is [0, 1, 2, 4, 8, 7, 6].
'''
from typing import List
import heapq

# Dijkstra's algorithm
def swimInWater(grid: List[List[int]]) -> int:
    N = len(grid)
    visit = set()
    minH = [[grid[0][0], 0, 0]]  # (time(or max-height), r, c)
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    visit.add((0, 0))
    while minH:
        t, r, c = heapq.heappop(minH)
        if r == N - 1 and c == N - 1:
            return t
        for dr, dc in directions:
            neiR, neiC = r + dr, c + dc
            if (neiR < 0 or neiC < 0 or 
                neiR == N or neiC == N or
                (neiR, neiC) in visit
            ):
                continue
            visit.add((neiR, neiC))
            heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])

# ============================
# Test Case [[0,1,2,10], [9,14,4,13], [12,3,8,15], [11,5,7,6]]] -> 8
# ============================
if __name__ == "__main__":
    res = swimInWater([[0,1,2,10], [9,14,4,13], [12,3,8,15], [11,5,7,6]])
    
    print(res)