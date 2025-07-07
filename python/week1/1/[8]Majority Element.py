# Majority Element
# 문제 설명: 배열 nums가 주어지면, 배열에서 가장 많이 등장하는 수를 반환하는 함수를 작성하세요.
# 배열에서 가장 많이 등장하는 수를 반환합니다.
# 입력: nums = [3,2,3]
# 출력: 3
# 설명: 배열에서 3이 2번 등장하므로, 3을 반환합니다.

from typing import List

def majorityElement(nums: List[int]) -> int:
    # Boyer-Moore Voting
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate

# test case
print(majorityElement([3,2,3])) # 3
print(majorityElement([2,2,1,1,1,2,2])) # 2