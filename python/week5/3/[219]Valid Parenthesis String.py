'''
Valid Parenthesis String

You are given a string s which contains only three types of characters: '(', ')' and '*'.

Return true if s is valid, otherwise return false.

A string is valid if it follows all of the following rules:

Every left parenthesis '(' must have a corresponding right parenthesis ')'.
Every right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".

Example 1:

Input: s = "((**)"

Output: true

Explanation: One of the '*' could be a ')' and the other could be an empty string.

Example 2:

Input: s = "(((*)"

Output: false

Explanation: The string is not valid because there is an extra '(' at the beginning, regardless of the extra '*'.
'''

# Recursion
def checkValidString(s: str) -> bool:

    def dfs(i, open):
        if open < 0:
            return False
        if i == len(s):
            return open == 0

        if s[i] == '(':
            return dfs(i + 1, open + 1)
        elif s[i] == ')':
            return dfs(i + 1, open - 1)
        else:
            return (dfs(i + 1, open) or
                    dfs(i + 1, open + 1) or
                    dfs(i + 1, open - 1))
    return dfs(0, 0)

# Greedy
def checkValidString(s: str) -> bool:
    leftMin, leftMax = 0, 0

    for c in s:
        if c == "(":
            leftMin, leftMax = leftMin + 1, leftMax + 1
        elif c == ")":
            leftMin, leftMax = leftMin - 1, leftMax - 1
        else:
            leftMin, leftMax = leftMin - 1, leftMax + 1
        if leftMax < 0:
            return False
        if leftMin < 0:
            leftMin = 0
    return leftMin == 0

# ============================
# Test Case "((**)" -> True
# ============================
if __name__ == "__main__":
    res = checkValidString("((**)")
    
    print(res)