'''
Partition to K Equal Sum Subsets

You are given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [2,4,1,3,5], k = 3

Output: true

Explanation: Given array can be divided into three subsets [5], [2,3], [4,1].

Example 2:

Input: nums = [1,2,3,4], k = 3

Output: false
'''
from typing import List

# Backtracking
def canPartitionKSubsets(nums: List[int], k: int) -> bool:
    if sum(nums) % k != 0:
        return False

    nums.sort(reverse=True)
    target = sum(nums) // k
    used = [False] * len(nums)

    # i: 현재 숫자를 탐색할 시작 인덱스, k: 남은 부분집합의 개수, subsetSum: 현재 구성 중인 부분집합의 누적 합
    def backtrack(i, k, subsetSum):
        if k == 0:
            return True
        if subsetSum == target:
            return backtrack(0, k - 1, 0)
        for j in range(i, len(nums)):
            if used[j] or subsetSum + nums[j] > target:
                continue
            used[j] = True
            if backtrack(j + 1, k, subsetSum + nums[j]):
                return True
            used[j] = False
        return False

    return backtrack(0, k, 0)

# Dynamic Programming
def canPartitionKSubsets(nums: List[int], k: int) -> bool:
    total = sum(nums)
    if total % k != 0:
        return False

    target = total // k
    n = len(nums)
    N = 1 << n
    dp = [0] + [-1] * (N - 1) # mask에 해당하는 숫자들을 사용해서 이미 여러 개의 부분집합을 만들었고, 지금 새로 만들고 있는 부분집합의 누적 합을 target으로 나눈 나머지를 의미

    for mask in range(N):
        if dp[mask] == -1:
            continue
        for i in range(n):
            if (mask & (1 << i)) == 0 and dp[mask] + nums[i] <= target: # 현재 mask에 i번째 숫자가 포함되지 않고, 현재 부분집합의 합에 nums[i]를 더해도 target을 넘지 않는 경우
                dp[mask | (1 << i)] = (dp[mask] + nums[i]) % target # nums[i]를 추가한 새로운 mask에 대해, 하나의 부분집합이 정확히 완성된 상태면 0을 대입

    return dp[N - 1] == 0

# ============================
# Test Case [2,4,1,3,5], 3 -> True
# ============================
if __name__ == "__main__":
    res = canPartitionKSubsets([2,4,1,3,5], 3)
    
    print(res)