'''
Permutations
#Tree Maze #Combinations
Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [7]

Output: [[7]]

Permutations (순열)
- 주어진 배열 nums의 모든 가능한 순열을 반환하는 문제
- nums의 모든 숫자는 유일(unique)
- 순열의 순서는 상관없고, 결과 순서는 아무거나 가능
==============insert()==============
nums = [10, 20, 30]

nums.insert(1, 99)  
print(nums)  # [10, 99, 20, 30]

nums.insert(0, 5)   
print(nums)  # [5, 10, 99, 20, 30]

nums.insert(len(nums), 100)
print(nums)  # [5, 10, 99, 20, 30, 100]  (append와 동일)
'''

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # 1) 종료 조건: 입력 배열이 비었으면 [[]] 반환
        #    (순열의 구성요소가 없을 때, 빈 순열 하나를 기본으로 반환)
        if len(nums) == 0:
            return [[]]

        # 2) 첫 번째 원소를 제외한 나머지에 대해 재귀 호출
        #    예: nums=[1,2,3]이면, permute([2,3]) 호출
        perms = self.permute(nums[1:])  # 나머지 원소들로 만들 수 있는 모든 순열
        res = []

        # 3) 기존 순열(perms)의 각 자리에 nums[0]을 삽입
        for p in perms:
            for i in range(len(p) + 1):
                # p를 복사하여 i번째 위치에 nums[0] 삽입
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res

# 실행 예시
if __name__=="__main__":
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.permute(nums))  

    