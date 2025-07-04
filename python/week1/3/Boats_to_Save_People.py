# Boats to Save People
# each boat carries at most two people
# minimum number of boats to carry every person
# Two Pointers, Counting Sort
from typing import List

def merge(left, right):
    result = []
    i = j = 0

    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    if(len(arr) <= 1):
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# Solution 1
def numRescueBoats(people: List[int], limit: int) -> int:
    people[:] = merge_sort(people)
    res, l, r = 0, 0, len(people) - 1
    while l <= r:
        remain = limit - people[r]
        r -= 1
        res += 1
        if l <= r and remain >= people[l]:
            l += 1
    return res

# Solution 2
def numRescueBoats(people: List[int], limit: int) -> int:
    m = max(people)
    count = [0] * (m + 1)
    for p in people:
        count[p] += 1

    idx, i = 0, 1
    while idx < len(people):
        while count[i] == 0:
            i += 1
        people[idx] = i
        count[i] -= 1
        idx += 1

    res, l, r = 0, 0, len(people) - 1
    while l <= r:
        remain = limit - people[r]
        r -= 1
        res += 1
        if l <= r and remain >= people[l]:
            l += 1
    return res

# ============================
# Test Case [1,3,2,3,2], 3 -> 4
# ============================
if __name__ == "__main__":
    people = [1,3,2,3,2]
    limit = 3

    print(numRescueBoats(people, limit))