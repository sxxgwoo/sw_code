'''
Products of Array Except Self
Solved 
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]

Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]

###
range(start, stop, step):

start: 시작값 → len(nums) - 1 (즉, 마지막 인덱스)
stop: 멈출 직전 값 → -1 (즉, 0까지 포함하려면 -1까지 가야 함)
step: 증가량 → -1 (즉, 하나씩 감소)

List -> list 소문자로 변경해야 오류 안뜸

'''
class Solution:

    #1) Brutal Force
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = []
        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]
            res.append(prod)
        return res
    
    #2) prefix & suffix
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res



if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 3, 4]
    nums2 = [3, 4, 2, 8]
    nums3 = [10, 0, -3, 4]
    
    print(sol.productExceptSelf(nums1))
    print(sol.productExceptSelf(nums2))
    print(sol.productExceptSelf(nums3))
    

