'''
Find Critical and Pseudo Critical Edges in Minimum Spanning Tree

You are given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [a[i], b[i], weight[i]] represents a bidirectional and weighted edge between nodes a[i] and b[i]. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

Example 1:

Input: n = 4, edges = [[0,3,2],[0,2,5],[1,2,4]]

Output: [[0,2,1],[]]

Example 2:

Input: n = 5, edges = [[0,3,2],[0,4,2],[1,3,2],[3,4,2],[2,3,1],[1,2,3],[0,1,1]]

Output: [[4,6],[0,1,2,3]]
'''
from typing import List

# Kruskal's algorithm
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v1):
        while v1 != self.par[v1]:
            self.par[v1] = self.par[self.par[v1]]
            v1 = self.par[v1]
        return v1

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
    
def findCriticalAndPseudoCriticalEdges(n: int, edges: List[List[int]]) -> List[List[int]]:
    for i, e in enumerate(edges):
        e.append(i)  # [v1, v2, weight, original_index]

    edges.sort(key=lambda e: e[2])

    mst_weight = 0
    uf = UnionFind(n)
    for v1, v2, w, i in edges:
        if uf.union(v1, v2):
            mst_weight += w

    critical, pseudo = [], []
    for n1, n2, e_weight, i in edges:
        # Try without curr edge
        weight = 0
        uf = UnionFind(n)
        for v1, v2, w, j in edges:
            if i != j and uf.union(v1, v2):
                weight += w
        if max(uf.rank) != n or weight > mst_weight:
            critical.append(i)
            continue

        # Try with curr edge
        uf = UnionFind(n)
        uf.union(n1, n2)
        weight = e_weight
        for v1, v2, w, j in edges:
            if uf.union(v1, v2):
                weight += w
        if weight == mst_weight:
            pseudo.append(i)
    return [critical, pseudo]

# ============================
# Test Case 5, [[0,3,2],[0,4,2],[1,3,2],[3,4,2],[2,3,1],[1,2,3],[0,1,1]] -> [[4,6],[0,1,2,3]]
# ============================
if __name__ == "__main__":
    res = findCriticalAndPseudoCriticalEdges(5, [[0,3,2],[0,4,2],[1,3,2],[3,4,2],[2,3,1],[1,2,3],[0,1,1]])
    
    print(res)