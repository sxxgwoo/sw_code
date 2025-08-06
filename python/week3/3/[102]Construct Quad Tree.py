'''
Construct Quad Tree

You are given a n * n binary matrix grid. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
val: True if the node represents a grid cell of 1's or False if the node represents a grid cell of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional grid using the following steps:

If the current grid has the same value (i.e all 1's or all 0's), set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids representing the four childrens of the current node.
Recurse the steps for every children of the current node.

Example 1:

Input: grid = [[1,1],[1,1]]

Output: [[1,1]]

Example 2:

Input: grid = [
    [1,1,1,1],
    [0,0,0,0],
    [1,1,1,1],
    [1,1,1,1]
]

Output: [[0,0],[0,0],[0,0],[1,1],[1,1],[1,1],[1,1],[1,0],[1,0],[1,1],[1,1],[1,0],[1,0]]
'''
from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

# Recursion
def construct(grid: List[List[int]]) -> 'Node':
    def dfs(n, r, c):
        allSame = True
        for i in range(n):
            for j in range(n):
                if grid[r][c] != grid[r + i][c + j]:
                    allSame = False
                    break
        if allSame:
            return Node(grid[r][c], True, None, None, None, None)
        
        n = n // 2
        topleft = dfs(n, r, c)
        topright = dfs(n, r, c + n)
        bottomleft = dfs(n, r + n, c)
        bottomright = dfs(n, r + n, c + n)
        
        return Node(0, False, topleft, topright, bottomleft, bottomright)
    
    return dfs(len(grid), 0, 0)

# Recursion (optimal)
def construct(grid: List[List[int]]) -> 'Node':
    def dfs(n, r, c):
        if n == 1:
            return Node(grid[r][c] == 1, True, None, None, None, None)

        mid = n // 2
        topLeft = dfs(mid, r, c)
        topRight = dfs(mid, r, c + mid)
        bottomLeft = dfs(mid, r + mid, c)
        bottomRight = dfs(mid, r + mid, c + mid)

        if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and
            topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            return Node(topLeft.val, True, None, None, None, None)

        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

    return dfs(len(grid), 0, 0)

# ============================
# Test Case 
#   [[1,1,1,1],
#    [0,0,0,0],
#    [1,1,1,1],
#    [1,1,1,1]]
# -> [[0,0],[0,0],[0,0],[1,1],[1,1],[1,1],[1,1],[1,0],[1,0],[1,1],[1,1],[1,0],[1,0]]
# ============================
if __name__ == "__main__":
    grid = [
    [1,1,1,1],
    [0,0,0,0],
    [1,1,1,1],
    [1,1,1,1]
    ]
    
    res = construct(grid)

    print(res)