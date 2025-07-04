'''
Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
'''

class Solution:

    # 1) Brute Force
    # def longestConsecutive(self, nums: list[int]) -> int:
    #     if len(nums)==0:
    #         return 0
        
    #     sorted_nums = sorted(set(nums))
    #     max_cnt=1
    #     cnt=1
    #     for i in range(len(sorted_nums)-1):
    #         if sorted_nums[i+1] - sorted_nums[i]==1:
    #             cnt+=1
    #         else:
    #             if cnt > max_cnt:
    #                 max_cnt = cnt
    #             cnt = 1
    #         if cnt > max_cnt:
    #             max_cnt = cnt

    #     return max_cnt
    
    #2) Brute Force
    def longestConsecutive(self, nums: list[int]) -> int:
        res = 0  # 최장 연속 수열의 길이를 저장할 변수
        store = set(nums)  # O(1) 조회를 위한 집합으로 변환 (중복 제거 + 빠른 탐색)

        for num in nums:
            streak, curr = 0, num  # 연속 길이 초기화, 현재 수부터 시작

            # 현재 수부터 연속된 수가 존재할 동안 streak 증가
            while curr in store:
                streak += 1      # 연속 길이 1 증가
                curr += 1        # 다음 수로 이동

            # 지금까지의 최대 연속 길이와 비교하여 갱신
            res = max(res, streak)

        return res  # 최장 연속 수열의 길이 반환
    
    # 3) hash set
    # def longestConsecutive(self, nums: list[int]) -> int:
    #     numSet = set(nums)
    #     longest = 0

    #     for num in numSet:
    #         if (num - 1) not in numSet:
    #             length = 1
    #             while (num + length) in numSet:
    #                 length += 1
    #             longest = max(length, longest)
    #     return longest


if __name__ == "__main__":
    sol = Solution()
    nums1 = [0,3,2,5,4,6,1,1]
    nums2=[9,1,4,7,3,-1,0,5,8,-1,6]
    nums3 = [2,20,4,10,3,4,5]
    
    print(sol.longestConsecutive(nums1))
    print(sol.longestConsecutive(nums2))
    print(sol.longestConsecutive(nums3))
    

