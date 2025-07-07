# Remove Element
# 문제 설명: 배열 nums와 정수 val이 주어지면, 배열에서 val을 제거하고 배열의 길이를 반환하는 함수를 작성하세요.
# 배열에서 val을 제거한 후, 배열의 길이를 반환합니다.
# 입력: nums = [3,2,2,3], val = 3
# 출력: 2
# 설명: 배열에서 3을 제거한 후, 배열의 길이는 2가 됩니다.

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1
    return write

# test case
print(removeElement([3,2,2,3], 3)) # 2
print(removeElement([0,1,2,2,3,0,4,2], 2)) # 5