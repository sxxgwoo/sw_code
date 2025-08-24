'''
Bitwise AND of Numbers Range

You are given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: left = 1, right = 5

Output: 0

Example 2:

Input: left = 10, right = 12

Output: 8
'''

# Brute Force
def rangeBitwiseAnd(left: int, right: int) -> int:
    res = left
    for i in range(left + 1, right + 1):
        res &= i
    return res

# Bit Manipulation
def rangeBitwiseAnd(left: int, right: int) -> int:
    res = 0
    for i in range(32):
        bit = (left >> i) & 1
        if not bit:
            continue

        remain = left % (1 << (i + 1))
        diff = (1 << (i + 1)) - remain # 특정 자리에서 1이 처음으로 0이 되기 위한 최소한의 차이 
        if right - left < diff:
            res |= (1 << i) # Bitwise OR 연산자

    return res

# ============================
# Test Case 10, 12 -> 8
# ============================
if __name__ == "__main__":
    res = rangeBitwiseAnd(10,12)
    
    print(res)