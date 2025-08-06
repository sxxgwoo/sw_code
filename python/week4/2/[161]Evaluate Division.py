'''
Evaluate Division
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Example 1:

Input: equations = [["a","b"],["b","c"],["ab","bc"]], values = [4.0,1.0,3.25], queries = [["a","c"],["b","a"],["c","c"],["ab","a"],["d","d"]]

Output: [4.00000,0.25000,1.00000,-1.00000,-1.00000]
Example 2:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"]]

Output: [0.50000,2.00000]
'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        