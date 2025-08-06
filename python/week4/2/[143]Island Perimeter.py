'''
Island Perimeter
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
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        