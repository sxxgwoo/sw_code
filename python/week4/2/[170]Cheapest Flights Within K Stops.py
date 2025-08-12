'''
Cheapest Flights Within K Stops
There are n airports, labeled from 0 to n - 1, which are connected by some flights. You are given an array flights where flights[i] = [from_i, to_i, price_i] represents a one-way flight from airport from_i to airport to_i with cost price_i. You may assume there are no duplicate flights and no flights from an airport to itself.

You are also given three integers src, dst, and k where:

src is the starting airport
dst is the destination airport
src != dst
k is the maximum number of stops you can make (not including src and dst)
Return the cheapest price from src to dst with at most k stops, or return -1 if it is impossible.

Example 1:



Input: n = 4, flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]], src = 0, dst = 3, k = 1

Output: 500
Explanation:
The optimal path with at most 1 stop from airport 0 to 3 is shown in red, with total cost 200 + 300 = 500.
Note that the path [0 -> 1 -> 2 -> 3] costs only 400, and thus is cheaper, but it requires 2 stops, which is more than k.

Example 2:



Input: n = 3, flights = [[1,0,100],[1,2,200],[0,2,100]], src = 1, dst = 2, k = 1

Output: 200
Explanation:
The optimal path with at most 1 stop from airport 1 to 2 is shown in red and has cost 200.
'''
# deque 구현 간단한 Queue 클래스 구현 (FIFO)
class Queue:
    def __init__(self):
        self.data = []

    def append(self, val):
        self.data.append(val)

    def popleft(self):
        if self.data:
            return self.data.pop(0)  # O(n) 시간복잡도
        raise IndexError("pop from empty queue")

    def __len__(self):
        return len(self.data)

    def __bool__(self):
        return bool(self.data)
    
class Solution:
    # 2. Bellman-Ford Algorithm
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # 각 노드까지의 최소 비용 저장. 초기값은 ∞, 출발지는 0
        prices = [float("inf")] * n
        prices[src] = 0

        # 최대 k+1번 경유 가능하므로, 간선 완화를 k+1번 반복
        for i in range(k + 1):
            # 이번 라운드에서의 변경 사항을 저장할 임시 배열
            tmpPrices = prices.copy()

            # 모든 간선(비행편)에 대해 완화 시도
            for s, d, p in flights:  # s=출발지, d=도착지, p=비용
                # 출발지에 도달 불가능하면 스킵
                if prices[s] == float("inf"):
                    continue
                # 현재 경로를 거쳐서 도착지로 가는 비용이 더 작으면 갱신
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            # 이번 라운드 결과를 반영
            prices = tmpPrices

        # 목적지에 도달 불가능하면 -1, 가능하면 최소 비용 반환
        return -1 if prices[dst] == float("inf") else prices[dst]
    
    # 3. Shortest Path Faster Algorithm (SPFA)
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # 1) 초기 비용: 출발지는 0, 나머지는 무한대
        prices = [float("inf")] * n
        prices[src] = 0

        # 2) 인접 리스트 생성 (u -> v: 비용 cst)
        adj = [[] for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])

        # 3) 큐 초기화: (현재까지의 비용, 현재 노드, 경유 횟수)
        q = Queue()
        q.append((0, src, 0))

        # 4) 큐가 빌 때까지 반복
        while q:
            cst, node, stops = q.popleft()

            # 경유 횟수 제한 초과 시 skip
            if stops > k:
                continue

            # 현재 노드에서 갈 수 있는 모든 이웃 노드 탐색
            for nei, w in adj[node]:
                nextCost = cst + w  # 새로운 경로 비용
                # 완화(Relaxation): 더 싸게 갈 수 있으면 갱신
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    # 다음 노드로 이동 (경유 횟수 +1)
                    q.append((nextCost, nei, stops + 1))

        # 5) 목적지 가격 반환 (도달 불가 시 -1)
        return prices[dst] if prices[dst] != float("inf") else -1

    
if __name__=="__main__":
    sol = Solution()

    n = 3
    flights = [[1,0,100],[1,2,200],[0,2,100]]
    src = 1
    dst = 2
    k = 1

    print(sol.findCheapestPrice(n,flights,src, dst, k))