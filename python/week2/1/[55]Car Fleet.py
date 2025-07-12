# 853. Car Fleet
# https://leetcode.com/problems/car-fleet/
# Problem description
# There are n cars going to the same destination along a one-lane road.
# The destination is target miles away.
# You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).
# A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed.
# The distance between these two cars is ignored (i.e., they are assumed to have the same position).
# A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

# Solution 1: Time Calculation + Stack Simulation
# Time Complexity: O(n log n)
# Space Complexity: O(n)

from typing import List

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    """
    주행 도착 시간 계산 후, 뒤에서부터 보면서
    도착 시간이 더 크면 새로운 플릿으로 카운트하는 방식
    시간 복잡도: O(n log n), 공간 복잡도: O(n)
    """
    # (position, speed) 쌍을 위치 기준 내림차순으로 정렬
    cars = sorted(zip(position, speed), key=lambda x: -x[0])
    
    fleets = 0         # 최종 플릿 개수
    max_time = 0.0     # 지금까지 본 차들 중 가장 늦게 도착하는 시간
    
    for pos, spd in cars:
        # 각 차가 목표 지점까지 가는 시간
        time = (target - pos) / spd
        
        # 이전에 본 차들보다 더 늦게 도착하면 새로운 플릿
        if time > max_time:
            fleets += 1
            max_time = time   # 기준 시간을 갱신
    
    return fleets

# Test cases
print(carFleet(10, [1,4], [3,2])) # 1
print(carFleet(10, [4,1,0,7], [2,2,1,1])) # 3
print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3])) # 3