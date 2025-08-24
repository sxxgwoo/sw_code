'''
Excel Sheet Column Title

You are given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:

Input: columnNumber = 32

Output: "AF"

Example 2:

Input: columnNumber = 53

Output: "BA"
'''

# Iteration
def convertToTitle(columnNumber: int) -> str:
    res = []
    while columnNumber > 0:
        columnNumber -= 1
        offset = columnNumber % 26
        res += chr(ord('A') + offset) # ord 함수는 문자의 ASCII code 값 반환
        columnNumber //= 26

    return ''.join(reversed(res))

# Recursion 
def convertToTitle(columnNumber: int) -> str:
    if columnNumber == 0:
        return ""

    n = columnNumber - 1
    return convertToTitle(n // 26) + chr(n % 26 + ord('A'))

# ============================
# Test Case 53 -> "BA"
# ============================
if __name__ == "__main__":
    res = convertToTitle(53)
    
    print(res)