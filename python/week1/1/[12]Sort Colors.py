# Sort Colors
# 문제 설때: 배열 nums가 주어지면, 배열을 정렬하는 함수를 작성하세요.
# 입력: [2,0,2,1,1,0]
# 출력: [0,0,1,1,2,2]
# 설명: 배열을 정렬하면 [0,0,1,1,2,2]가 됩니다.

from typing import List

def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            
# test case
nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums) # [0,0,1,1,2,2]