'''
Sqrt(x)

You are given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:

Input: x = 9

Output: 3

Example 2:

Input: x = 13

Output: 3
'''

# Brute Force
def mySqrt(x: int) -> int:
    if x == 0:
        return 0

    res = 1
    for i in range(1, x + 1):
        if i * i > x:
            return res
        res = i

    return res

# Binary Search
def mySqrt(x: int) -> int:
    l, r = 0, x
    res = 0

    while l <= r:
        m = l + (r - l) // 2
        if m * m > x:
            r = m - 1
        elif m * m < x:
            l = m + 1
            res = m
        else:
            return m

    return res

# ============================
# Test Case 13 -> 3
# ============================
if __name__ == "__main__":
    res = mySqrt(13)

    print(res)

