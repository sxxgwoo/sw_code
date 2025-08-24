'''
Detect Squares

You are given a stream of points consisting of x-y coordinates on a 2-D plane. Points can be added and queried as follows:

Add - new points can be added to the stream into a data structure. Duplicate points are allowed and should be treated as separate points.
Query - Given a single query point, count the number of ways to choose three additional points from the data structure such that the three points and the query point form a square. The square must have all sides parallel to the x-axis and y-axis, i.e. no diagonal squares are allowed. Recall that a square must have four equal sides.
Implement the CountSquares class:

CountSquares() Initializes the object.
void add(int[] point) Adds a new point point = [x, y].
int count(int[] point) Counts the number of ways to form valid squares with point point = [x, y] as described above.

Example 1:

Input: 
["CountSquares", "add", [[1, 1]], "add", [[2, 2]], "add", [[1, 2]], "count", [[2, 1]], "count", [[3, 3]], "add", [[2, 2]], "count", [[2, 1]]]

Output:
[null, null, null, null, 1, 0, null, 2]

Explanation:
CountSquares countSquares = new CountSquares();
countSquares.add([1, 1]);
countSquares.add([2, 2]);
countSquares.add([1, 2]);

countSquares.count([2, 1]);   // return 1.
countSquares.count([3, 3]);   // return 0.
countSquares.add([2, 2]);     // Duplicate points are allowed.
countSquares.count([2, 1]);   // return 2. 
'''
from typing import List
from collections import defaultdict

# SH proof
class CountSquares:
    def __init__(self):
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        x,y = point
        cnt = 0

        row = []
        col = []

        for p in self.pts:
            if(p[1] == y and p[0] != x):
                row.append(p)
            if(p[0] == x and p[1] != y):
                col.append(p)
        
        for p in row:
            for q in col:
                if(abs(p[0]-x) == abs(q[1]-y)):
                    for r in self.pts:
                        if(r == [p[0],q[1]]):
                            cnt += 1
        
        return cnt

# Hash Map
class CountSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res

# ============================
# Test Case ["CountSquares", "add", [[1, 1]], "add", [[2, 2]], "add", [[1, 2]], 
# "count", [[2, 1]], "count", [[3, 3]], "add", [[2, 2]], "count", [[2, 1]]] 
# -> [null, null, null, null, 1, 0, null, 2]
# ============================
if __name__ == "__main__":
    countSquares = CountSquares()
    countSquares.add([1, 1])
    countSquares.add([2, 2])
    countSquares.add([1, 2])

    print(countSquares.count([2, 1]))    # return 1
    print(countSquares.count([3, 3]))    # return 0
    countSquares.add([2, 2])             # Duplicate points are allowed
    print(countSquares.count([2, 1]))    # return 2 