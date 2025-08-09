'''
Evaluate Division
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Example 1:

Input: equations = [["a","b"],["b","c"],["ab","bc"]], values = [4.0,1.0,3.25], queries = [["a","c"],["b","a"],["c","c"],["ab","a"],["d","d"]]

Output: [4.00000,0.25000,1.00000,-1.00000,-1.00000]
Example 2:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"]]

Output: [0.50000,2.00000]
'''
import collections
# 간단한 Queue 클래스 구현 (FIFO)
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
    # 1. BFS
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # 인접 리스트(adj):
        # 각 노드(문자)에 대해 [(연결 노드, 비율값)]을 저장
        # 예: a/b = 2.0 이면 adj[a] = [(b, 2.0)], adj[b] = [(a, 0.5)]
        import collections
        from collections import deque  # popleft() 쓰려면 deque 필요

        adj = collections.defaultdict(list)  # 기본값이 빈 리스트인 딕셔너리

        # equations와 values를 이용해 양방향 그래프 구성
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))        # a -> b, 값 = a/b
            adj[b].append((a, 1 / values[i]))    # b -> a, 값 = b/a

        # BFS 탐색: src에서 target까지의 경로를 찾아서 비율 계산
        def bfs(src, target):
            # 만약 src나 target이 그래프에 없으면 -1 반환
            if src not in adj or target not in adj:
                return -1

            # BFS 초기화: (현재 노드, 현재까지의 곱셈 결과)
            q = deque([(src, 1)])
            visit = set([src])  # 방문 처리

            while q:
                node, w = q.popleft()

                # 목적지 도착 시 현재까지 계산된 w를 반환
                if node == target:
                    return w

                # 인접 노드 탐색
                for nei, weight in adj[node]:
                    if nei not in visit:
                        # 다음 노드로 이동하면서 w * weight로 값 업데이트
                        q.append((nei, w * weight))
                        visit.add(nei)

            # 경로가 없으면 -1 반환
            return -1

        # 각 query에 대해 BFS 실행 후 결과 리스트로 반환
        return [bfs(q[0], q[1]) for q in queries]

    # 2. DFS
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        import collections

        # 인접 리스트(adj):
        # 각 노드(문자)에 대해 [(연결 노드, 비율값)]을 저장
        # 예: a/b = 2.0 → adj[a] = [(b, 2.0)], adj[b] = [(a, 0.5)]
        adj = collections.defaultdict(list)

        # equations와 values를 이용해 양방향 그래프 구성
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))        # a → b, 값 = a/b
            adj[b].append((a, 1 / values[i]))    # b → a, 값 = b/a

        # DFS 함수: src에서 target까지의 경로를 찾아 비율 계산
        def dfs(src, target, visited):
            # src나 target이 그래프에 없으면 계산 불가
            if src not in adj or target not in adj:
                return -1
            # 자기 자신을 목표로 할 경우 비율은 1
            if src == target:
                return 1

            visited.add(src)  # 방문 처리

            # 인접 노드 순회
            for nei, weight in adj[src]:
                if nei not in visited:
                    # 재귀적으로 다음 노드 탐색
                    result = dfs(nei, target, visited)
                    if result != -1:
                        # 경로가 존재하면 weight * result 반환
                        return weight * result

            # 경로를 찾지 못한 경우
            return -1

        # 각 query에 대해 DFS 실행 후 결과 리스트 반환
        return [dfs(q[0], q[1], set()) for q in queries]


if __name__=="__main__":
    sol = Solution()
    equations = [["a","b"],["b","c"],["ab","bc"]]
    values = [4.0,1.0,3.25]
    queries = [["a","c"],["b","a"],["c","c"],["ab","a"],["d","d"]]

    print(sol.calcEquation(equations,values,queries))