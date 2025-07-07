# Contains duplicate
# 문제 설명: 배열 nums가 주어지면, 배열 nums에 중복된 값이 있는지 확인하는 함수를 작성하세요.

from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))

# test case
print(hasDuplicate([1,2,3,1])) # True
print(hasDuplicate([1,2,3,4])) # False