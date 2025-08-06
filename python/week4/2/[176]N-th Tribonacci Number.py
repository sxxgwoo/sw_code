'''
N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

Input: n = 3

Output: 2
Explanation:
T_3 = 0 + 1 + 1 = 2

Example 2:

Input: n = 21

Output: 121415
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        