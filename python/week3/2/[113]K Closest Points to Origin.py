'''
K Closest Points to Origin
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.

Example 1:



Input: points = [[0,2],[2,2]], k = 1

Output: [[0,2]]
Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

Example 2:

Input: points = [[0,2],[2,0],[2,2]], k = 2

Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted.
'''
class MinHeap:
    def __init__(self):
        self.heap = []

    def heappush(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def heappop(self):
        if len(self.heap) == 0:
            raise IndexError("heap is empty")

        # 최소값 추출: 맨 앞 값
        self._swap(0, len(self.heap) - 1)
        val = self.heap.pop()
        self._sift_down(0)
        return val

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx][0] < self.heap[parent][0]:
            self._swap(idx, parent)
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        size = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == idx:
                break
            self._swap(idx, smallest)
            idx = smallest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

class Solution:
    # 1) sorting
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]
    # 2) Minheap
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minHeap = MinHeap()

        for x, y in points:
            dist = x ** 2 + y ** 2
            minHeap.heappush([dist, x, y])

        res = []
        for _ in range(k):
            dist, x, y = minHeap.heappop()
            res.append([x, y])
        return res

if __name__ == "__main__":
    sol = Solution()
    points = [[0, 2], [2, 0], [2, 2]]
    k = 2
    print(sol.kClosest(points, k))  # 출력 예: [[0, 2], [2, 0]]
    