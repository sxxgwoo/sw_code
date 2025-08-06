'''
Path with Minimum Effort
You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:

Input: heights = [
    [1,1,1],
    [3,2,4],
    [2,5,4]
]

Output: 2
Explanation: The route of [1,1,2,4,4] has a maximum absolute difference of 2 in consecutive cells.

Example 2:

Input: heights = [
    [1,1,1],
    [1,1,2],
    [6,5,2]
]

Output: 1
Explanation: The route of [1,1,1,1,1,2,2] has a maximum absolute difference of 1 in consecutive cells.
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        