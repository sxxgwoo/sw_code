'''
Network Delay Time

You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

ui is the source node (an integer from 1 to n)
vi is the target node (an integer from 1 to n)
ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
You are also given an integer k, representing the node that we will send a signal from.

Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.

Example 1:

Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

Output: 3

Example 2:

Input: times = [[1,2,1],[2,3,1]], n = 3, k = 2

Output: -1
'''
from typing import List
import heapq

# Dijkstra's algorithm
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    edges = {}
    for i in range(1,n+1):
        edges[i] = []
    for u, v, w in times:
        edges[u].append((v, w))

    minHeap = [(0, k)]
    visit = set()
    t = 0
    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in visit:
            continue
        visit.add(n1)
        t = w1

        for n2, w2 in edges[n1]:
            if n2 not in visit:
                heapq.heappush(minHeap, (w1 + w2, n2))
    return t if len(visit) == n else -1

# Floyd Warshall algorithm
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    inf = float('inf')
    dist = [[inf] * n for _ in range(n)]
    
    for u, v, w in times:
        dist[u-1][v-1] = w
    for i in range(n):
        dist[i][i] = 0
    
    for mid in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][mid] + dist[mid][j])
    
    res = max(dist[k-1])
    return res if res < inf else -1

# Bellman Ford algorithm
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    dist = [float('inf')] * n
    dist[k - 1] = 0
    for _ in range(n - 1):
        for u, v, w in times:
            if dist[u - 1] + w < dist[v - 1]:
                dist[v - 1] = dist[u - 1] + w
    max_dist = max(dist)
    return max_dist if max_dist < float('inf') else -1

# ============================
# Test Case [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], 4, 1 -> 3
# ============================
if __name__ == "__main__":
    res = networkDelayTime([[1,2,1],[2,3,1],[1,4,4],[3,4,1]], 4, 1)
    
    print(res)