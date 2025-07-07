# Two Sum
# 문제 설명: 배열 nums와 정수 target이 주어지면, 두 수의 합이 target이 되는 인덱스를 반환하는 함수를 작성하세요.
# 배열에는 중복된 수가 없다고 가정합니다.
# 입력: nums = [2,7,11,15], target = 9
# 출력: [0,1]
# 설명: nums[0] + nums[1] = 2 + 7 = 9이므로, [0,1]을 반환합니다.

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# test case
print(twoSum([2,7,11,15], 9)) # [0,1]
print(twoSum([3,2,4], 6)) # [1,2]
print(twoSum([3,3], 6)) # [0,1]