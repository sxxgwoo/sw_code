'''
Implement Stack Using Queues
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

Example 1:

Input: ["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]

Output: [null, null, null, 2, 2, false]
Explanation:
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

=============deque함수==============
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)       # dq: [1, 2, 3, 4]
dq.appendleft(0)   # dq: [0, 1, 2, 3, 4]
dq.pop()           # 4 제거 [0, 1, 2, 3]
dq.popleft()       # 0 제거 [1, 2, 3]
dq.rotate(1)       # dq: [3, 1, 2] (오른쪽 회전/밀어내기
dq.rotate(-1)      # dq: [1, 2, 3] (왼쪽 회전/밀어내기)

print(dq)          # deque([1, 2, 3])
dq[0]              # 1
'''
from collections import deque

class MyStack:
    # 1) deque 버전
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0

    # 2)list 버전
    # def __init__(self):
    #     self.q1 = []
    #     self.q2 = []

    # def push(self, x: int) -> None:
    #     self.q2.append(x)
    #     while self.q1:
    #         self.q2.append(self.q1.pop(0))  # ⚠️ O(n)
    #     self.q1, self.q2 = self.q2, []

    # def pop(self) -> int:
    #     return self.q1.pop(0)  # ⚠️ O(n)

    # def top(self) -> int:
    #     return self.q1[0]

    # def empty(self) -> bool:
    #     return len(self.q1) == 0



if __name__ == "__main__":
    # 시뮬레이션할 명령어들과 그에 해당하는 인자들
    commands = ["MyStack", "push", "push", "top", "pop", "empty"]
    arguments = [[], [1], [2], [], [], []]

    # 결과를 저장할 리스트
    results = []

    # 객체 저장용 변수
    obj = None

    # 명령어 처리
    for cmd, arg in zip(commands, arguments):
        if cmd == "MyStack":
            obj = MyStack()
            results.append(None)
        elif cmd == "push":
            obj.push(arg[0])
            results.append(None)
        elif cmd == "pop":
            results.append(obj.pop())
        elif cmd == "top":
            results.append(obj.top())
        elif cmd == "empty":
            results.append(obj.empty())

    print(results)