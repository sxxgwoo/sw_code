# 895. Maximum Frequency Stack
# https://leetcode.com/problems/maximum-frequency-stack/
# Problem description
# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.
# Implement the FreqStack class:
# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

# Solution 1: Hash Map + Stack
# Time Complexity: O(1) for push and pop operations
# Space Complexity: O(n)

class FreqStack:
    def __init__(self):
        # val → 현재 빈도
        self.freq = {}
        # 빈도 f → 빈도 f를 가진 값들의 스택(리스트)
        self.group = {}
        # 현재까지 가장 높은 빈도
        self.maxfreq = 0

    def push(self, val: int) -> None:
        # val의 빈도 갱신
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        
        # 해당 빈도의 그룹이 없으면 새로 만들기
        if f not in self.group:
            self.group[f] = []
        # 빈도 f 스택에 val 추가 (가장 최근 순서대로)
        self.group[f].append(val)
        
        # 최대 빈도 갱신
        if f > self.maxfreq:
            self.maxfreq = f

    def pop(self) -> int:
        # 가장 높은 빈도의 스택에서 꺼냄 (가장 최근에 푸시된 것)
        val = self.group[self.maxfreq].pop()
        
        # 해당 빈도 스택이 비었으면 빈도 레벨 하나 낮추기
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        
        # val의 빈도도 하나 줄임
        self.freq[val] -= 1
        return val

# Test cases
freqStack = FreqStack()
# 주어진 예시 시퀀스 실행
freqStack.push(5)  # 스택: [5]
freqStack.push(7)  # 스택: [5,7]
freqStack.push(5)  # 스택: [5,7,5]
freqStack.push(7)  # 스택: [5,7,5,7]
freqStack.push(4)  # 스택: [5,7,5,7,4]
freqStack.push(5)  # 스택: [5,7,5,7,4,5]

# pop() 호출 결과를 리스트에 모아서 확인
results = [
    freqStack.pop(),  # 기대: 5
    freqStack.pop(),  # 기대: 7
    freqStack.pop(),  # 기대: 5
    freqStack.pop(),  # 기대: 4
]

expected = [5, 7, 5, 4]
assert results == expected, f"테스트 실패: 얻은 결과 {results}, 기대값 {expected}"
print("모든 테스트 통과!")  # 테스트 성공 시 출력