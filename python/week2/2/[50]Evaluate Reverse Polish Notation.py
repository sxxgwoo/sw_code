'''
Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
'''
class Solution:
    #Brute Force
    # def evalRPN(self, tokens: list[str]) -> int:
    #     while len(tokens) > 1:
    #         for i in range(len(tokens)):
    #             if tokens[i] in "+-*/":
    #                 a = int(tokens[i-2])
    #                 b = int(tokens[i-1])
    #                 if tokens[i] == '+':
    #                     result = a + b
    #                 elif tokens[i] == '-':
    #                     result = a - b
    #                 elif tokens[i] == '*':
    #                     result = a * b
    #                 elif tokens[i] == '/':
    #                     result = int(a / b)
    #                 tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
    #                 break
    #     return int(tokens[0])
    
    # Stack
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop() # 굳이 이렇게하는 이유-> 순서가 다르기 때문
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]

if __name__=="__main__":
    sol = Solution()
    tokens = ["1","2","+","3","*","4","-"]
    print(sol.evalRPN(tokens))