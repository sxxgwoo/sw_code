'''
Min Cost to Connect Points
You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.

Example 1:



Input: points = [[0,0],[2,2],[3,3],[2,4],[4,2]]

Output: 10
'''

class MinHeap:
    def __init__(self):
        self.data = []  # 내부 배열에 힙 저장

    def heappush(self, val):
        """힙에 값 추가 (최소 힙 유지)"""
        self.data.append(val)
        self._sift_up(len(self.data) - 1)

    def heappop(self):
        """최소값 꺼내기"""
        if not self.data:
            return None
        self._swap(0, len(self.data) - 1)
        val = self.data.pop()
        self._sift_down(0)
        return val

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.data[idx][0] < self.data[parent][0]:
            self._swap(idx, parent)
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        n = len(self.data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < n and self.data[left][0] < self.data[smallest][0]:
                smallest = left
            if right < n and self.data[right][0] < self.data[smallest][0]:
                smallest = right
            if smallest == idx:
                break
            self._swap(idx, smallest)
            idx = smallest

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def __bool__(self):
        return bool(self.data)

    def __len__(self):
        return len(self.data)
    
class Solution:
    # 1. Prim's Algorithm - Minimum Spanning Tree (MST)
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)  # 총 정점 수

        # 인접 리스트 생성: 각 점에서 다른 모든 점까지의 거리 저장
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)  # 맨해튼 거리
                adj[i].append([dist, j])  # i → j 간선
                adj[j].append([dist, i])  # j → i 간선 (무방향)

        res = 0               # 전체 비용 누적
        visit = set()         # MST에 포함된 정점 저장
        heapq = MinHeap()     # 최소 힙 사용: (비용, 정점 번호)
        heapq.heappush([0, 0])  # 시작점: 비용 0, 정점 0

        # Prim's Algorithm: 모든 정점을 방문할 때까지 반복
        while len(visit) < N:
            cost, i = heapq.heappop()

            # 이미 방문한 정점이면 무시
            if i in visit:
                continue

            res += cost        # 해당 정점 연결 비용 누적
            visit.add(i)       # 정점 i 방문 처리

            # 현재 정점 i에서 갈 수 있는 모든 이웃 확인
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush([neiCost, nei])  # 이웃 정점 후보로 삽입

        return res  # 모든 점을 연결하는 최소 비용

if __name__=="__main__":
    sol = Solution()
    points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
    print(sol.minCostConnectPoints(points))