# 460. LFU Cache
# https://leetcode.com/problems/lfu-cache/
# Problem description
# Design a data structure that follows the Least Frequently Used (LFU) cache eviction policy.
# Implement the LFUCache class:
# LFUCache(int capacity) Initializes the object with the capacity of the data structure.
# int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
# void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key first, or if there is a tie, the least recently used key.

# Solution 1: Hash Map + Ordered Dict
# Time Complexity: O(1) for get and put operations
# Space Complexity: O(n)

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        """
        capacity: 캐시 최대 용량
        key2val: key → value 저장
        key2freq: key → 사용 빈도 저장
        freq2keys: freq → 해당 빈도의 키들을 사용한 순서를 보장하는 OrderedDict로 저장
        minfreq: 현재 캐시에서 최소 사용 빈도
        """
        self.capacity = capacity
        self.key2val = {}
        self.key2freq = {}
        self.freq2keys = defaultdict(OrderedDict)
        self.minfreq = 0

    def _update_freq(self, key: int):
        """
        key의 사용 빈도를 1 증가시키고,
        freq2keys 구조를 갱신하며 minfreq를 조정
        """
        freq = self.key2freq[key]
        # 1) 기존 freq 그룹에서 key 제거
        del self.freq2keys[freq][key]
        if not self.freq2keys[freq]:
            # 그룹이 비면 삭제
            del self.freq2keys[freq]
            # 만약 이 freq가 현재 최소 빈도면 다음 빈도로 증가
            if freq == self.minfreq:
                self.minfreq += 1

        # 2) 빈도를 1 증가시키고, 새 그룹에 key 추가
        new_freq = freq + 1
        self.key2freq[key] = new_freq
        self.freq2keys[new_freq][key] = None  # 값은 필요 없으므로 None

    def get(self, key: int) -> int:
        """
        key가 캐시에 있으면 값을 반환하고 사용 빈도 업데이트.
        없으면 -1 반환.
        """
        if key not in self.key2val:
            return -1
        # 사용 빈도 갱신
        self._update_freq(key)
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        """
        key가 이미 있으면 값을 갱신하고 빈도 업데이트.
        없으면, 용량 초과 시 LFU(최소 빈도 & LRU) 키를 제거하고
        새 key를 빈도=1로 삽입.
        """
        if self.capacity <= 0:
            return

        if key in self.key2val:
            # 기존 키: 값만 업데이트, 빈도 증가
            self.key2val[key] = value
            self._update_freq(key)
            return

        # 새 키: 용량 초과 시 제거
        if len(self.key2val) >= self.capacity:
            # minfreq 그룹에서 가장 오래된 키를 꺼냄 (LRU)
            evict_key, _ = self.freq2keys[self.minfreq].popitem(last=False)
            # 관련 정보 제거
            del self.key2val[evict_key]
            del self.key2freq[evict_key]
            if not self.freq2keys[self.minfreq]:
                del self.freq2keys[self.minfreq]

        # 새 키를 빈도=1로 삽입
        self.key2val[key] = value
        self.key2freq[key] = 1
        self.freq2keys[1][key] = None
        # 최소 빈도는 새로 삽입된 1
        self.minfreq = 1
        
# Test cases
cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 1
cache.put(3, 3)
print(cache.get(2))  # -1
print(cache.get(3))  # 3
cache.put(4, 4)
print(cache.get(1))  # -1
print(cache.get(3))  # 3
print(cache.get(4))  # 4