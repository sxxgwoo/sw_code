'''
Counting Bits

Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 4

Output: [0,1,1,2,1]

Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
'''
from typing import List

# Brute Force
def countBits(n: int) -> List[int]:
    res = [0]

    for i in range(1, n+1):
        cnt = 0
        while i > 0:
            if(i % 2 == 1):
                cnt += 1
            i = i // 2
        res.append(cnt)
    
    return res

# Bit Manipulation (DP)
def countBits(n: int) -> List[int]:
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp

# ============================
# Test Case 4 -> [0,1,1,2,1]
# ============================
if __name__ == "__main__":
    res = countBits(4)
    
    print(res)
