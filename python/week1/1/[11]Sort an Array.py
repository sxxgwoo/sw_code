# Sort an Array
# 문제 설명: 배열 nums를 정렬하는 함수를 작성하세요.
# 입력: [5,2,3,1]
# 출력: [1,2,3,5]
# 설명: 배열을 정렬하면 [1,2,3,5]가 됩니다.

import random
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(l: int, r: int) -> None:
            if l >= r:
                return
            p = random.randint(l, r)
            pivot = nums[p]
            nums[p], nums[r] = nums[r], nums[p]

            i = l
            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]

            quicksort(l, i-1)
            quicksort(i+1, r)
        
        quicksort(0, len(nums) - 1)
        return nums

# test case
solution = Solution()
print(solution.sortArray([5,2,3,1])) # [1,2,3,5]
print(solution.sortArray([5,1,1,2,0,0])) # [0,0,1,1,2,5]