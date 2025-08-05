'''
IPO
A company has limited resources, it can only finish at most k distinct projects before the IPO. Help the company to design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it. Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

Example 1:

Input: k = 3, w = 0, profits = [1,4,2,3], capital = [0,3,1,1]

Output: 8
Explanation : The order of indices to pick are [0,3,1] and final capital is (1 + 3 + 4) = 8.

Example 2:

Input: k = 4, w = 2, profit = [2,3,1,5,3], capital = [4,4,2,3,3]

Output: 14
Explanation: The order of indices to pick are [2,3,4,1] and final capital is (2 + (1 + 5 + 3 + 3)) = 14.
'''
#minheap
class Heap:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)
        self._sift_up(len(self.data) - 1)

    def pop(self):
        if not self.data:
            return None
        self._swap(0, len(self.data) - 1)
        val = self.data.pop()
        self._sift_down(0)
        return val

    def peek(self):
        return self.data[0] if self.data else None

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.data[idx] < self.data[parent]:
            self._swap(idx, parent)
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        n = len(self.data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest == idx:
                break

            self._swap(idx, smallest)
            idx = smallest

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def __bool__(self):
        return bool(self.data)


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        n = len(profits)
        minCapital = Heap()  # 필요자본 기준 오름차순
        maxProfit = Heap()   # 음수로 저장해서 최대 힙처럼 사용

        for i in range(n):
            minCapital.push((capital[i], i))

        for _ in range(k):
            while minCapital and minCapital.peek()[0] <= w:
                _, idx = minCapital.pop()
                maxProfit.push((-profits[idx], idx))  # 음수 저장

            if not maxProfit:
                break

            profit, idx = maxProfit.pop()
            w += -profit  # 꺼낼 때 부호 복원

        return w


if __name__ == "__main__":
    sol = Solution()
    # example 1
    k = 3
    w = 0
    profits = [1,4,2,3]
    capital = [0,3,1,1]

    print(sol.findMaximizedCapital(k, w, profits, capital))  # 8

    # example 2
    k = 4
    w = 2
    profits = [2,3,1,5,3]
    capital = [4,4,2,3,3]

    print(sol.findMaximizedCapital(k, w, profits, capital))  # 14