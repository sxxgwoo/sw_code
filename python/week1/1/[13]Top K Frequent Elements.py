# Top K Frequent Elements
# 문제 설명: 배열 nums와 정수 k가 주어지면, 배열에서 가장 많이 등장하는 k개의 수를 반환하는 함수를 작성하세요.
# 입력: nums = [1,1,1,2,2,3], k = 2
# 출력: [1,2]
# 설명: 배열에서 1이 3번, 2가 2번 등장하므로, [1,2]를 반환합니다.

from typing import List
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)

    n = len(nums)
    buckets = [[] for _ in range(n+1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    
    res = []

    for freq in range(n, 0, -1):
        if not buckets[freq]:
            continue
        for num in buckets[freq]:
            res.append(num)
            if len(res) == k:
                return res
    
    return res

# test case
print(topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
print(topKFrequent([1], 1)) # [1]