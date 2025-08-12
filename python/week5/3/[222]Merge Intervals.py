'''
Merge Intervals

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.

Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

Example 1:

Input: intervals = [[1,3],[1,5],[6,7]]

Output: [[1,5],[6,7]]

Example 2:

Input: intervals = [[1,2],[2,3]]

Output: [[1,3]]
'''
from typing import List

# Sorting
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
        if(lst1[i][0] > lst2[j][0]):
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

def merge(intervals: List[List[int]]) -> List[List[int]]:
    sort = mergeSort(intervals)
    res = [sort[0]]
    n = len(intervals)

    for i in range(n-1):
        if(res[-1][1] < sort[i+1][0]):
            res.append(sort[i+1])
        else:
            res[-1] = [res[-1][0], max(res[-1][1], sort[i+1][1])]

    return res

# Greedy
def merge(intervals: List[List[int]]) -> List[List[int]]:
    max_val = max(interval[0] for interval in intervals) # 모든 구간의 시작점 중 최댓값을 구함

    mp = [0] * (max_val + 1) # 시작점을 인덱스로 하여, 해당 시작점에서 도달 가능한 '최대 끝점+1'을 저장하는 배열

    for start, end in intervals:
        mp[start] = max(end + 1, mp[start]) # 시작점 i에서 시작하는 구간들이 도달 가능한 최댓값의 '끝+1'

    res = []              # 최종 병합 결과를 저장할 리스트
    have = -1             # 현재 병합 중인 구간의 '끝 인덱스'
    interval_start = -1   # 현재 병합 중인 구간의 '시작 인덱스'

    # mp 배열을 순회하면서 병합
    for i in range(len(mp)):
        if mp[i] != 0:
            # 새로운 구간 시작점 발견 시 기록
            if interval_start == -1:
                interval_start = i
            # 현재 끝점(have)와 새로 발견된 끝점 중 더 큰 값 선택
            have = max(mp[i] - 1, have)

        # 현재 위치가 현재 병합 구간의 끝점에 도달하면 병합된 구간 저장
        if have == i:
            res.append([interval_start, have])
            have = -1
            interval_start = -1

    # mp 배열을 다 순회했는데, 아직 끝나지 않은 구간이 남아있을 경우 처리
    if interval_start != -1:
        res.append([interval_start, have])

    return res

# ============================
# Test Case [[1,3],[1,5],[6,7]] -> [[1,5],[6,7]]
# ============================
if __name__ == "__main__":
    res = merge([[1,3],[1,5],[6,7]])
    
    print(res)