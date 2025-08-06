'''
Redundant Connection

You are given a connected undirected graph with n nodes labeled from 1 to n. Initially, it contained no cycles and consisted of n-1 edges.

We have now added one additional edge to the graph. The edge has two different vertices chosen from 1 to n, and was not an edge that previously existed in the graph.

The graph is represented as an array edges of length n where edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple answers, return the edge that appears last in the input edges.

Example 1:

Input: edges = [[1,2],[1,3],[3,4],[2,4]]

Output: [2,4]

Example 2:

Input: edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]

Output: [3,4]
'''
from typing import List

# Cycle Detection (DFS)
def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    adj = [[] for _ in range(n+1)]

    def cycle(cur, prev):
        if(visit[cur]):
            return True
        
        visit[cur] = True

        for nei in adj[cur]:
            if(nei == prev):
                continue

            if(cycle(nei, cur)):
                return True
        return False
    

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        visit = [False] * (n+1)

        if cycle(u, -1):
            return [u,v]

    return []

# Disjoint Set Union
def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    par = [i for i in range(len(edges) + 1)]
    rank = [1] * (len(edges) + 1)

    def find(n):
        p = par[n]
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False
        if rank[p1] > rank[p2]:
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            rank[p2] += rank[p1]
        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]

# ============================
# Test Case [[1,2],[1,3],[3,4],[2,4]] -> [2,4]
# ============================
if __name__ == "__main__":
    res = findRedundantConnection([[1,2],[1,3],[3,4],[2,4]])
    
    print(res)