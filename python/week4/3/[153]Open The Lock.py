'''
Open The Lock

You have a lock with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:

Input: deadends = ["1111","0120","2020","3333"], target = "5555"

Output: 20

Example 2:

Input: deadends = ["4443","4445","4434","4454","4344","4544","3444","5444"], target = "4444"

Output: -1
'''
from typing import List
from collections import deque

# Breadth First Search 1
def openLock(deadends: List[str], target: str) -> int:
    if "0000" in deadends:
        return -1

    def children(lock):
        res = []
        for i in range(4):
            digit = str((int(lock[i]) + 1) % 10)
            res.append(lock[:i] + digit + lock[i+1:])
            digit = str((int(lock[i]) - 1 + 10) % 10)
            res.append(lock[:i] + digit + lock[i+1:])
        return res

    q = deque([("0000", 0)])
    visit = set(deadends)

    while q:
        lock, turns = q.popleft()
        if lock == target:
            return turns
        for child in children(lock):
            if child not in visit:
                visit.add(child)
                q.append((child, turns + 1))
    return -1

# Breadth First Search 2
def openLock(deadends: List[str], target: str) -> int:
    if target == "0000":
        return 0

    visit = set(deadends)
    if "0000" in visit:
        return -1
    
    q = deque(["0000"])
    visit.add("0000")
    steps = 0
    
    while q:
        steps += 1
        for _ in range(len(q)):
            lock = q.popleft()
            for i in range(4):
                for j in [1, -1]:
                    digit = str((int(lock[i]) + j + 10) % 10)
                    nextLock = lock[:i] + digit + lock[i+1:]
                    if nextLock in visit:
                        continue
                    if nextLock == target:
                        return steps
                    q.append(nextLock)
                    visit.add(nextLock)
    return -1

# ============================
# Test Case ["1111","0120","2020","3333"], "5555" -> 20
# ============================
if __name__ == "__main__":
    res = openLock(["1111","0120","2020","3333"], "5555")
    
    print(res)