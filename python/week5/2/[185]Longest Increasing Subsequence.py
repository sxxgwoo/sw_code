'''
Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
Example 1:

Input: nums = [9,1,4,2,3,3,7]

Output: 4
Explanation: The longest increasing subsequence is [1,2,3,7], which has a length of 4.

Example 2:

Input: nums = [0,3,1,3,2,3]

Output: 4
'''
class Solution:
    # Dynamic Programming (Bottom-Up) - I
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -2, -1):
                LIS = dp[i + 1][j + 1]  # Not including nums[i]

                if j == -1 or nums[j] < nums[i]:
                    LIS = max(LIS, 1 + dp[i + 1][i + 1])  # Including nums[i]

                dp[i][j + 1] = LIS

        return dp[0][0]
    
if __name__ == "__main__":
    sol = Solution()
    nums = [0,3,1,3,2,3]
    print(sol.lengthOfLIS(nums))