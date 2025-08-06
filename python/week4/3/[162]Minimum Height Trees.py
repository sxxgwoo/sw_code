'''
Minimum Height Trees

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

You are given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [a[i], b[i]] indicates that there is an undirected edge between the two nodes a[i] and b[i] in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h)) are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example 1:

Input: n = 5, edges = [[0,1],[3,1],[2,3],[4,1]]

Output: [3,1]

Explanation: As shown, the trees with root labels [3,1] are MHT's with height of 2.

Example 2:

Input: n = 4, edges = [[1,0],[2,0],[3,0]]

Output: [0]

Explanation: As shown, the tree with root label [0] is MHT with height of 1.
'''
from typing import List

# SH proof
class Queue: # Queue 직접 구현
    def __init__(self):
        self.in_stack = []   # enqueue 되는 쪽
        self.out_stack = []  # dequeue 되는 쪽

    def enqueue(self, value):
        self.in_stack.append(value)

    def dequeue(self):
        if not self.out_stack:
            # in_stack에서 out_stack으로 요소를 옮김
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("dequeue from empty queue")
        return self.out_stack.pop()

    def is_empty(self):
        return not self.in_stack and not self.out_stack

def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    adj = [[] for _ in range(n)]

    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    def bfs(node):
        q = Queue()
        visit = set()
        time = 0
        q.enqueue((node, 0))
        visit.add(node)
        while not q.is_empty():
            cur, t = q.dequeue()
            for v in adj[cur]:
                if(v not in visit):
                    q.enqueue((v, t+1))
                    visit.add(v)
                    time = max(time, t+1)
        
        return time
        
    h = [-1] * n
    for i in range(n):
        h[i] = bfs(i)
    
    m = min(h)

    res = []
    for i in range(n):
        if(m == h[i]):
            res.append(i)
    
    return res
        

# Brute Force (DFS)
def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    def dfs(node, parent):
        hgt = 0
        for nei in adj[node]:
            if nei == parent:
                continue
            hgt = max(hgt, 1 + dfs(nei, node))
        return hgt
    
    minHgt = n
    res = []
    for i in range(n):
        curHgt = dfs(i, -1)
        if curHgt == minHgt:
            res.append(i)
        elif curHgt < minHgt:
            res = [i]
            minHgt = curHgt
    
    return res

# ============================
# Test Case 5, [[0,1],[3,1],[2,3],[4,1]] -> [3,1]
# ============================
if __name__ == "__main__":
    res = findMinHeightTrees(5, [[0,1],[3,1],[2,3],[4,1]])
    
    print(res)