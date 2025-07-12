# 155. Min Stack
# https://leetcode.com/problems/min-stack/
# Problem description
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

# Solution 1: Two Stacks
# Time Complexity: O(1) for all operations
# Space Complexity: O(n)

class MinStack:
    def __init__(self):
        # 주 스택과 보조(최소값) 스택 초기화
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 보조 스택이 비어있거나 새 값이 현재 최소값 이하일 때만 push
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # 주 스택에서 꺼낸 값이 최소값 스택 최상단과 같으면, 둘 다 pop
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # 주 스택 최상단 반환
        return self.stack[-1]

    def getMin(self) -> int:
        # 보조 스택 최상단(현재 최소값) 반환
        return self.min_stack[-1]

# Solution 2: Single Stack with Tuple
# Time Complexity: O(1) for all operations
# Space Complexity: O(n)

# class MinStack:
#     def __init__(self):
#         # (값, 그 시점까지의 최소값) 쌍을 저장
#         self.stack = []

#     def push(self, val: int) -> None:
#         if not self.stack:
#             # 스택이 비어있으면, 최소값 = val
#             self.stack.append((val, val))
#         else:
#             curr_min = self.stack[-1][1]
#             # 새 최소값은 기존 최소값과 val 중 더 작은 쪽
#             self.stack.append((val, min(val, curr_min)))

#     def pop(self) -> None:
#         self.stack.pop()

#     def top(self) -> int:
#         # 값만 반환
#         return self.stack[-1][0]

#     def getMin(self) -> int:
#         # 튜플의 두 번째 원소가 그 시점 최소값
#         return self.stack[-1][1]

# Test cases
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # -3
minStack.pop()
print(minStack.top())     # 0
print(minStack.getMin())  # -2