'''
N-Queens II
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

You are given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:



Input: n = 4

Output: 2
Explanation: There are two different solutions to the 4-queens puzzle.

Example 2:

Input: n = 1

Output: 1
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        