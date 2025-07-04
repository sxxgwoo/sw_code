'''
Subarray Sum Equals K
#Hash Usage #Hash Implementation #Prefix Sums
You are given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
연속되어야함 / 조합이 아님.

Example 1:

Input: nums = [2,-1,1,2], k = 2

Output: 4
Explanation: [2], [2,-1,1], [-1,1,2], [2] are the subarrays whose sum is equals to k.

Example 2:

Input: nums = [4,4,4,4,4,4], k = 4

Output: 6
'''

class Solution:

    # 1) Brute Force    
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    res += 1
        return res
    
    # 2) Hash Map
    # Hash Map을 이용한 Subarray Sum Equals K 풀이
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0              # 조건을 만족하는 subarray 개수 누적
        curSum = 0           # 현재까지의 누적합
        prefixSums = {0: 1}  # 누적합의 등장 횟수를 저장하는 딕셔너리
                            # 0:1 은 초기값. 누적합이 정확히 k일 때를 커버하기 위함.

        for num in nums:
            curSum += num                    # 현재까지의 누적합 갱신
            diff = curSum - k                # 과거에 누적합이 diff인 지점이 있다면,
                                            # 그 지점 이후 현재까지의 부분합이 k라는 뜻

            res += prefixSums.get(diff, 0)   # 그런 diff가 prefixSums에 몇 번 등장했는지 더함, 해당 subarray의 개수만큼 결과에 추가
                                            #만약 prefixSums 딕셔너리에 diff라는 key가 있으면 그 값을 반환하고, 없다면 기본값 0을 반환하라.

            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
            # 현재 누적합을 prefixSums에 기록 (등장 횟수 증가)
        
        return res                            # k를 만족하는 모든 subarray의 개수를 반환


if __name__ == "__main__":
    sol=Solution()
    # nums = [4,4,4,4,4,4]
    # k = 4
    nums = [-1,2,1,2]
    k = 2
    print(sol.subarraySum(nums,k))