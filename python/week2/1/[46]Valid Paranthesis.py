# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Problem description
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Solution 1: Hash Map + Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

def isValid(s: str) -> bool:
    """
    해시맵 + 스택을 이용한 O(n) 풀이
    """
    # 닫는 괄호 → 여는 괄호 매핑
    pairs = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for ch in s:
        if ch in pairs:
            # 스택이 비어있거나 짝이 다르면 False
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()  # 맞다면 한 쌍 제거
        else:
            # 여는 괄호는 스택에 쌓아 두기
            stack.append(ch)
    
    # 모든 짝이 맞아야 스택이 비어있음
    return not stack

# Solution 2: String Replacement
# Time Complexity: O(n^2)
# Space Complexity: O(n)

# def isValid(s: str) -> bool:
#     """
#     문자열 치환을 이용한 이해하기 쉬운 O(n^2) 풀이
#     """
#     prev = None
#     # 더 이상 치환이 일어나지 않을 때까지 반복
#     while prev != s:
#         prev = s
#         s = s.replace("()", "")
#         s = s.replace("[]", "")
#         s = s.replace("{}", "")
#     # 최종적으로 빈 문자열이면 모두 짝이 맞음
#     return s == ""

# Test cases
print(isValid("()"))  # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False
print(isValid("([)]"))  # False
print(isValid("{[]}"))  # True