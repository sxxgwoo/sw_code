'''
Minimum Interval to Include Each Query
You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] represents the ith interval starting at left_i and ending at right_i (inclusive).

You are also given an integer array of query points queries. The result of query[j] is the length of the shortest interval i such that left_i <= queries[j] <= right_i. If no such interval exists, the result of this query is -1.

Return an array output where output[j] is the result of query[j].

Note: The length of an interval is calculated as right_i - left_i + 1.

Example 1:

Input: intervals = [[1,3],[2,3],[3,7],[6,6]], queries = [2,3,1,7,6,8]

Output: [2,2,3,5,1,-1]
Explanation:

Query = 2: The interval [2,3] is the smallest one containing 2, it's length is 2.
Query = 3: The interval [2,3] is the smallest one containing 3, it's length is 2.
Query = 1: The interval [1,3] is the smallest one containing 1, it's length is 3.
Query = 7: The interval [3,7] is the smallest one containing 7, it's length is 5.
Query = 6: The interval [6,6] is the smallest one containing 6, it's length is 1.
Query = 8: There is no interval containing 8.
'''
class MinHeap:
    """
    heapq 모듈처럼 리스트를 외부에서 넘겨받아 조작하는 클래스형 래퍼.
    사용 예)
        heapq = MinHeap()
        h = []
        heapq.heappush(h, (priority, data))
        x = heapq.heappop(h)
    """
    # --- public API (heapq 스타일) ---
    def heappush(self, heap: list, val):
        """리스트 heap에 원소 val 삽입 (최소 힙 유지)"""
        heap.append(val)
        self._sift_up(heap, len(heap) - 1)

    def heappop(self, heap: list):
        """리스트 heap에서 최소 원소 제거 후 반환 (빈 경우 None)"""
        if not heap:
            return None
        # 루트를 끝과 교환 후 pop, 남았으면 아래로 내리기
        heap[0], heap[-1] = heap[-1], heap[0]
        val = heap.pop()
        if heap:
            self._sift_down(heap, 0)
        return val

    def heapify(self, heap: list):
        """임의 리스트를 제자리에서 최소 힙으로 변환"""
        n = len(heap)
        for i in reversed(range(n // 2)):
            self._sift_down(heap, i)

    # --- internal helpers ---
    def _sift_up(self, heap: list, idx: int):
        """삽입 시 위로 올리기"""
        item = heap[idx]
        while idx > 0:
            parent = (idx - 1) // 2
            # 파이썬 튜플 비교(사전식)를 그대로 사용해 일반화
            if heap[parent] <= item:
                break
            heap[idx] = heap[parent]
            idx = parent
        heap[idx] = item

    def _sift_down(self, heap: list, idx: int):
        """삭제 시 아래로 내리기"""
        n = len(heap)
        item = heap[idx]
        while True:
            left = 2 * idx + 1
            right = left + 1
            smallest = idx

            if left < n and heap[left] < heap[smallest]:
                smallest = left
            if right < n and heap[right] < heap[smallest]:
                smallest = right
            if smallest == idx:
                break

            heap[idx] = heap[smallest]
            idx = smallest
        heap[idx] = item
# class MaxHeap:
#     """
#     heapq 모듈처럼 리스트를 외부에서 넘겨받아 조작하는 최대 힙 래퍼.
#     사용 예)
#         maxheap = MaxHeap()
#         h = []
#         maxheap.heappush(h, (priority, data))
#         x = maxheap.heappop(h)
#     """
#     # --- public API (heapq 스타일) ---
#     def heappush(self, heap: list, val):
#         """리스트 heap에 원소 val 삽입 (최대 힙 유지)"""
#         heap.append(val)
#         self._sift_up(heap, len(heap) - 1)

#     def heappop(self, heap: list):
#         """리스트 heap에서 최대 원소 제거 후 반환 (빈 경우 None)"""
#         if not heap:
#             return None
#         heap[0], heap[-1] = heap[-1], heap[0]
#         val = heap.pop()
#         if heap:
#             self._sift_down(heap, 0)
#         return val

#     def heapify(self, heap: list):
#         """임의 리스트를 제자리에서 최대 힙으로 변환"""
#         n = len(heap)
#         for i in reversed(range(n // 2)):
#             self._sift_down(heap, i)

#     # --- internal helpers ---
#     def _sift_up(self, heap: list, idx: int):
#         """삽입 시 위로 올리기"""
#         item = heap[idx]
#         while idx > 0:
#             parent = (idx - 1) // 2
#             # 최소 힙과 반대로, 부모가 더 작으면 교환
#             if heap[parent] >= item:
#                 break
#             heap[idx] = heap[parent]
#             idx = parent
#         heap[idx] = item

#     def _sift_down(self, heap: list, idx: int):
#         """삭제 시 아래로 내리기"""
#         n = len(heap)
#         item = heap[idx]
#         while True:
#             left = 2 * idx + 1
#             right = left + 1
#             largest = idx

#             if left < n and heap[left] > heap[largest]:
#                 largest = left
#             if right < n and heap[right] > heap[largest]:
#                 largest = right
#             if largest == idx:
#                 break

#             heap[idx] = heap[largest]
#             idx = largest
#         heap[idx] = item

class Solution:
    # 1. Min Heap 풀이 (효율적인 방법)
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        # intervals: [l, r]로 이루어진 구간들
        # queries: 각각의 질의에 대해 최소 구간 길이를 구해야 함
        intervals.sort()   # 시작점 기준으로 정렬
        heapq = MinHeap()  # 직접 구현한 최소 힙 (heapq 모듈 스타일)
        minHeap = []       # 실제 힙 저장소
        res = {}           # query -> 최소 길이 매핑
        i = 0              # intervals 인덱스

        for q in sorted(queries):  # query를 정렬하여 순서대로 처리
            # 1) 시작점이 q 이하인 interval을 모두 힙에 삽입
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                # (구간 길이, 오른쪽 끝점) 튜플로 저장
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            # 2) q를 포함하지 못하는 interval(끝점 < q)은 제거
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # 3) 현재 query q에 대해 힙의 top이 최소 구간 길이를 가짐
            res[q] = minHeap[0][0] if minHeap else -1

        # 원래 queries 순서대로 결과 반환
        return [res[q] for q in queries]
    
    # 2. Brute Force 풀이 (단순 구현, 비효율적)
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        n = len(intervals)
        res = []

        for q in queries:   # 각 query에 대해
            cur = -1        # 최소 구간 길이 (없으면 -1)
            for l, r in intervals:
                # query가 해당 interval에 포함되면
                if l <= q <= r:
                    # 현재까지의 최소 구간보다 더 짧으면 갱신
                    if cur == -1 or (r - l + 1) < cur:
                        cur = r - l + 1
            res.append(cur)
        return res
    

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[2,3],[3,7],[6,6]]
    queries = [2,3,1,7,6,8]
    print(sol.minInterval(intervals,queries))