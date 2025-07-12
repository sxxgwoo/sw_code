# 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/
# Problem description
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the TimeMap class:
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

# Solution 1: Binary Search
# Time Complexity: O(log n) for set and get operations
# Space Complexity: O(n)

class TimeMap:
    def __init__(self):
        # key → [(timestamp1, value1), (timestamp2, value2), ...]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        직접 구현한 이진 탐색으로, key의 리스트에서
        timestamp <= 입력값인 가장 큰 타임스탬프의 값을 찾아 반환.
        """
        if key not in self.store:
            return ""
        arr = self.store[key]
        
        left, right = 0, len(arr) - 1
        res = ""  # 찾은 가장 최신 값을 저장할 변수
        
        while left <= right:
            mid = (left + right) // 2
            t, val = arr[mid]
            
            if t == timestamp:
                # 정확히 일치하면 즉시 반환
                return val
            elif t < timestamp:
                # mid의 타임스탬프가 작으면 후보에 저장하고 우측 탐색
                res = val
                left = mid + 1
            else:
                # mid의 타임스탬프가 크면 좌측 탐색
                right = mid - 1
        
        return res
    
# Test cases
timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1)) # "bar"
print(timeMap.get("foo", 3)) # "bar"
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4)) # "bar2"
print(timeMap.get("foo", 5)) # "bar2"