'''
Car Pooling

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and a integer array trips where trips[i] = [numPassengers[i], from[i], to[i]] indicates that the ith trip has numPassengers[i] passengers and the locations to pick them up and drop them off are from[i] and to[i] respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Example 1:

Input: trips = [[4,1,2],[3,2,4]], capacity = 4

Output: true

Example 2:

Input: trips = [[2,1,3],[3,2,4]], capacity = 4

Output: false
'''
from typing import List

# Brute Force
def carPooling(trips: List[List[int]], capacity: int) -> bool:
    max = -1

    for i in range(len(trips)):
        if(max < trips[i][2]):
            max = trips[i][2]
    
    res = [0] * (max + 1)

    for i in range(len(trips)):
        for j in range(trips[i][1], trips[i][2]):
            res[j] += trips[i][0]
    
    for i in range(len(res)):
        if(res[i] > capacity):
            return False
    
    return True

# Line Sweep
def carPooling(trips: List[List[int]], capacity: int) -> bool:
    points = []
    for passengers, start, end in trips:
        points.append([start, passengers])
        points.append([end, -passengers])
    
    points.sort()
    curPass = 0
    for point, passengers in points:
        curPass += passengers
        if curPass > capacity:
            return False
    
    return True

# ============================
# Test Case [[2,1,3],[3,2,4]], 4 -> false
# ============================
if __name__ == "__main__":
    res = carPooling([[2,1,3],[3,2,4]], 4)
    
    print(res)