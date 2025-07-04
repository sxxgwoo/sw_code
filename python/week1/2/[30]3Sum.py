'''
#two pointers
3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''
class Solution:
    # 1) Brute Force - 모든 세 수 조합을 다 탐색하는 방식
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()          # 중복 방지를 위해 set 사용
        nums.sort()          # 정렬하면 중복 제거 및 조합 비교가 쉬워짐

        # 세 수의 조합을 모두 시도 (i < j < k)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    # 합이 0이면 정답 후보
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]   # 정렬된 상태라 순서 고정됨
                        res.add(tuple(tmp))                 # set은 리스트 대신 튜플 저장

        # 최종적으로 리스트로 변환해서 반환
        return [list(i) for i in res]

    
    # 2) **Two Pointers - 세 수의 합이 0이 되는 모든 고유한 조합을 찾는 함수
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []             # 결과 리스트
        nums.sort()          # 먼저 정렬 (정렬이 핵심 전제 조건)

        for i, a in enumerate(nums):  # 첫 번째 수 a를 기준으로 고정
            if a > 0:
                break  # 정렬된 상태에서 a > 0이면 이후도 모두 양수 → 합이 0이 될 수 없음

            if i > 0 and a == nums[i - 1]:
                continue  # 중복된 a는 건너뛰기 (중복된 조합 방지)

            l, r = i + 1, len(nums) - 1  # a 다음부터 끝까지 투 포인터 설정
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1  # 합이 너무 크면 오른쪽 포인터 왼쪽으로 이동
                elif threeSum < 0:
                    l += 1  # 합이 너무 작으면 왼쪽 포인터 오른쪽으로 이동
                else:
                    # 합이 0이면 정답 조합 발견
                    res.append([a, nums[l], nums[r]])

                    # 다음 유효한 값으로 포인터 이동 (중복 제거)
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res  # 모든 고유한 3합 조합을 반환

        
        
if __name__ == "__main__":
    sol = Solution()
    numbers=[-5,-3,0,2,4,6,8]
    print(sol.threeSum(numbers))