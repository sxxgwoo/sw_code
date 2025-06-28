'''
Majority Element II
You are given an integer array nums of size n, 
find all elements that appear more than ⌊ n/3 ⌋ times. 
You can return the result in any order.

Example 1:

Input: nums = [5,2,3,2,2,2,2,5,5,5]

Output: [2,5]

Example 2:

Input: nums = [4,4,4,4,4]

Output: [4]

Example 3:

Input: nums = [1,2,3]

Output: []
'''

class Solution:
    # Brute Force
    def majorityElement(self, nums: list[int]) -> list[int]:
        cnt=0
        res=[]
        n = set(nums)

        for i in n:
            for j in range(len(nums)):
                if i == nums[j]:
                    cnt+=1
            if cnt > len(nums)//3:
                res.append(i)
            cnt=0

        return res
    
    # Boyer-Moore Voting Algorithm 확장 버전 (n/3 초과 다수 원소 찾기)
    # def majorityElement(self, nums: list[int]) -> list[int]:
    #     n = len(nums)
        
    #     # 후보값 2개와 그에 대한 카운트
    #     num1 = num2 = -1       # 초기 후보값 (-1로 설정, 어떤 숫자든 상관없음)
    #     cnt1 = cnt2 = 0        # 후보에 대한 득표 수

    #     # 1단계: 후보 선출 과정
    #     for num in nums:
    #         if num == num1:
    #             cnt1 += 1
    #         elif num == num2:
    #             cnt2 += 1
    #         elif cnt1 == 0:
    #             num1 = num
    #             cnt1 = 1
    #         elif cnt2 == 0:
    #             num2 = num
    #             cnt2 = 1
    #         else:
    #             # 두 후보와도 다른 숫자이면서 카운트도 남아있지 않으면
    #             cnt1 -= 1
    #             cnt2 -= 1

    #     # 2단계: 후보가 실제로 n/3 초과로 등장하는지 검증
    #     cnt1 = cnt2 = 0
    #     for num in nums:
    #         if num == num1:
    #             cnt1 += 1
    #         elif num == num2:
    #             cnt2 += 1

    #     # 3단계: 조건을 만족하는 후보만 결과에 포함
    #     res = []
    #     if cnt1 > n // 3:
    #         res.append(num1)
    #     if cnt2 > n // 3:
    #         res.append(num2)
        
    #     return res

    
if __name__ == "__main__":
    sol = Solution()
    nums1 = [5,2,3,2,2,2,2,5,5,5]
    nums2 = [4,4,4,4,4]
    nums3 = [1,2,3]
    
    print(sol.majorityElement(nums1))
    print(sol.majorityElement(nums2))
    print(sol.majorityElement(nums3))
    