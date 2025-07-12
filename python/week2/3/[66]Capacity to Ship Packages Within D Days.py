'''
Capacity to Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). It is not allowed to load weight more than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:

Input: weights = [2,4,6,1,3,10], days = 4

Output: 10

Explanation:
1st day: [2]
2nd day: [4,6]
3rd day: [1,3]
4th day: [10]

Example 2:

Input: weights = [1,2,3,4,5], days = 5

Output: 5

Explanation:
1st day: [1]
2nd day: [2]
3rd day: [3]
4th day: [4]
5th day: [5]

Example 3:

Input: weights = [1,5,4,4,2,3], days = 3

Output: 8

Explanation:
1st day = [1,5]
2nd day = [4,4]
3rd day = [2,3]
'''
from typing import List

# Linear Search
def shipWithinDays(weights: List[int], days: int) -> int:
    res = max(weights)
    while True:
        ships = 1
        cap = res
        for w in weights:
            if cap - w < 0:
                ships += 1
                cap = res
            cap -= w

        if ships <= days:
            return res

        res += 1

# Binary Search
def shipWithinDays(weights: List[int], days: int) -> int:
    l, r = max(weights), sum(weights)
    res = r

    def canShip(cap):
        ships, currCap = 1, cap
        for w in weights:
            if currCap - w < 0:
                ships += 1
                if ships > days:
                    return False
                currCap = cap

            currCap -= w
        return True

    while l <= r:
        cap = (l + r) // 2
        if canShip(cap):
            res = min(res, cap)
            r = cap - 1
        else:
            l = cap + 1
    
    return res

# ============================
# Test Case [2,4,6,1,3,10], 4 -> 10
# ============================
if __name__ == "__main__":
    res = shipWithinDays([2,4,6,1,3,10], 4)

    print(res)