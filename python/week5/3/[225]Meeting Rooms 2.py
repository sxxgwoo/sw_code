'''
Meeting Rooms II

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2

Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
'''
from typing import List
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

# Two Pointers
def mergeSort(lst):
    if(len(lst) < 2):
        return lst
    
    mid = len(lst) // 2

    lst1 = mergeSort(lst[:mid])
    lst2 = mergeSort(lst[mid:])

    return mergeLst(lst1, lst2)

def mergeLst(lst1, lst2):
    i = j = 0
    res = []

    while i < len(lst1) and j < len(lst2):
        if(lst1[i]> lst2[j]):
            res.append(lst2[j])
            j += 1
        
        else:
            res.append(lst1[i])
            i += 1
    
    if(i == len(lst1)):
        res.extend(lst2[j:])
    if(j == len(lst2)):
        res.extend(lst1[i:])
    
    return res

def minMeetingRooms(intervals: List[Interval]) -> int:
    start = mergeSort([i.start for i in intervals])
    end = mergeSort([i.end for i in intervals])

    res = count = 0
    s = e = 0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    return res

# ============================
# Test Case [(0,40),(5,10),(15,20)] -> 2
# ============================
if __name__ == "__main__":
    int1 = Interval(0,40)
    int2 = Interval(5,10)
    int3 = Interval(15,20)
    res = minMeetingRooms([int1, int2, int3])
    
    print(res)
