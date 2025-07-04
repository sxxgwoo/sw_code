# Baseball Game
# sum of all the scores on the record after applying all the operations
# Stacks
from typing import List

# Solution 1
def calPoints(operations: List[str]) -> int:
    stack = []
    for op in operations:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)

# Solution 2
def calPoints(operations: List[str]) -> int:
    stack, res = [], 0
    for op in operations:
        if op == "+":
            res += stack[-1] + stack[-2]
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            res += (2 * stack[-1])
            stack.append(2 * stack[-1])
        elif op == "C":
            res -= stack.pop()
        else:
            res += int(op)
            stack.append(int(op))
    return res

# ============================
# Test Case ["1","2","+","C","5","D"] -> 18
# ============================
if __name__ == "__main__":
    nums = ["1","2","+","C","5","D"]
    res = calPoints(nums)

    print(res)