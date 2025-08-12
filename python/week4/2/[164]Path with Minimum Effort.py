'''
Path with Minimum Effort
You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:

Input: heights = [
    [1,1,1],
    [3,2,4],
    [2,5,4]
]

Output: 2
Explanation: The route of [1,1,2,4,4] has a maximum absolute difference of 2 in consecutive cells.

Example 2:

Input: heights = [
    [1,1,1],
    [1,1,2],
    [6,5,2]
]

Output: 1
Explanation: The route of [1,1,1,1,1,2,2] has a maximum absolute difference of 1 in consecutive cells.
'''
# class heapq
class MaxHeap:
    def __init__(self):
        self.data = []  # 내부 배열에 힙 저장

    def heappush(self, val):
        """힙에 값 추가 (최대 힙 유지)"""
        self.data.append(val)
        self._sift_up(len(self.data) - 1)

    def heappop(self):
        """최대값 꺼내기"""
        if not self.data:
            return None
        self._swap(0, len(self.data) - 1)
        val = self.data.pop()
        self._sift_down(0)
        return val

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.data[idx][0] > self.data[parent][0]:
            self._swap(idx, parent)
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        n = len(self.data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            if left < n and self.data[left][0] > self.data[largest][0]:
                largest = left
            if right < n and self.data[right][0] > self.data[largest][0]:
                largest = right
            if largest == idx:
                break
            self._swap(idx, largest)
            idx = largest

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def __bool__(self):
        return bool(self.data)

    def __len__(self):
        return len(self.data)


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
    # 1. Dijkstra's Algorithm: 최소 effort 경로 탐색 **
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        
        # 최소 힙 사용: (현재까지의 최대 높이차, r, c)
        heapq = MinHeap()
        heapq.heappush([0, 0, 0])  # 시작점에서의 effort = 0

        visit = set()  # 방문한 노드 저장
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 상하좌우 이동 방향

        while heapq:
            # 가장 작은 effort부터 꺼냄 (Dijkstra 핵심)
            diff, r, c = heapq.heappop()

            # 이미 방문한 노드면 무시
            if (r, c) in visit:
                continue

            # 현재 노드를 방문 처리
            visit.add((r, c))

            # 도착지에 도달하면 해당 effort가 정답
            if (r, c) == (ROWS - 1, COLS - 1):
                return diff

            # 상하좌우 이웃 노드로 이동
            for dr, dc in directions:
                newR, newC = r + dr, c + dc

                # 격자 밖이거나 이미 방문한 곳은 무시
                if (
                    newR < 0 or newC < 0 or
                    newR >= ROWS or newC >= COLS or
                    (newR, newC) in visit
                ):
                    continue

                # 이동 시 발생하는 높이 차를 고려한 새로운 경로 effort
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))

                # 새 경로 후보를 힙에 추가
                heapq.heappush([newDiff, newR, newC])

        return 0  # 도달 불가능한 경우 (문제 조건상 없음)
    

    # 2. Binary Search + DFS
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 상하좌우 방향

        # DFS: 현재 (r, c)에서 도착지까지 limit 이하로 도달 가능한지 확인
        def dfs(r, c, limit, visited):
            if r == ROWS - 1 and c == COLS - 1:
                return True  # 도착 지점에 도달

            visited.add((r, c))  # 현재 위치 방문 처리

            for dr, dc in directions:
                newR, newC = r + dr, c + dc

                # 범위를 벗어나거나, 이미 방문했거나, 높이 차이가 limit 초과면 skip
                if (newR < 0 or newC < 0 or
                    newR >= ROWS or newC >= COLS or
                    (newR, newC) in visited or
                    abs(heights[newR][newC] - heights[r][c]) > limit):
                    continue

                # 다음 칸으로 이동해서 도달 가능하면 True 반환
                if dfs(newR, newC, limit, visited):
                    return True

            return False  # 어떤 방향으로도 도달 불가능

        # 이분 탐색 범위: 최소 0 ~ 최대 10^6 (문제 조건 상 최대 높이 차이)
        l, r = 0, 10**6
        res = r  # 정답 저장용 변수

        # 이분 탐색
        while l <= r:
            mid = (l + r) // 2  # 현재 시도하는 최대 허용 높이차
            if dfs(0, 0, mid, set()):
                # 시작점에서 도착점까지 mid 이하 effort로 도달 가능하면
                res = mid       # 정답 후보 갱신
                r = mid - 1     # 더 작은 effort 시도
            else:
                l = mid + 1     # 더 큰 effort 필요

        return res

        
if __name__=="__main__":
    sol = Solution()
    heights = [
        [1,1,1],
        [1,1,2],
        [6,5,2]
    ]
    # heights = [
    #     [1,1,1],
    #     [3,2,4],
    #     [2,5,4]
    # ]
    print(sol.minimumEffortPath(heights))