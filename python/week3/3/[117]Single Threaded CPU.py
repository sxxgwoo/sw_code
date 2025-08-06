'''
Single Threaded CPU

You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the ith task will be available to process at enqueueTime[i] and will take processingTime[i] to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started to process, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.

Example 1:

Input: tasks = [[1,4],[3,3],[2,1]]

Output: [0,2,1]

Example 2:

Input: tasks = [[5,2],[4,4],[4,1],[2,1],[3,3]]

Output: [3,4,2,0,1]
'''
from typing import List
import math

# Brute Force
def getOrder(tasks: List[List[int]]) -> List[int]:
    res = []
    l = len(tasks)
    threshold = float('inf')

    for i in range(l):
        if(threshold > tasks[i][0]):
            threshold = tasks[i][0]

    for _ in range(l):
        m = float('inf')
        n = float('inf')
        idx = 0
        for i in range(l):
            if i not in res and tasks[i][0] <= threshold and n > tasks[i][1]:
                m = min(m, tasks[i][0])
                n = tasks[i][1]
                idx = i
        
        res.append(idx)
        threshold = max(m, threshold)
        threshold += tasks[idx][1]
    
    return res

# ============================
# Test Case [[5,2],[4,4],[4,1],[2,1],[3,3]] -> [3,4,2,0,1]
# ============================
if __name__ == "__main__":
    res = getOrder([[5,2],[4,4],[4,1],[2,1],[3,3]])
    
    print(res)