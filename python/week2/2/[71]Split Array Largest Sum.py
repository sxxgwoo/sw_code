'''
Split Array Largest Sum
#search range #tree maze #2-dimension dp # prefix sums
정수 배열 nums와 정수 k가 주어졌을 때, nums를 k개의 연속된 부분 배열로 나누어 그 중 가장 큰 부분 배열의 합을 최소화하는 문제
You are given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

Example 1:

Input: nums = [2,4,10,1,5], k = 2

Output: 16
Explanation: The best way is to split into [2,4,10] and [1,5], where the largest sum among the two subarrays is only 16.

Example 2:

Input: nums = [1,0,2,3,5], k = 4

Output: 5
Explanation: The best way is to split into [1], [0,2], [3] and [5], where the largest sum among the two subarrays is only 5.

1) solution 그림 설명
dfs(0, 2)
├── [7] + dfs(1, 1)
│   └── [2,5,10,8] → sum = 25 → max = max(7, 25) = 25
├── [7,2] + dfs(2, 1)
│   └── [5,10,8] → sum = 23 → max = max(9, 23) = 23
├── [7,2,5] + dfs(3, 1)
│   └── [10,8] → sum = 18 → max = max(14, 18) = 18 ✅ 최소값
├── [7,2,5,10] + dfs(4, 1)
│   └── [8] → sum = 8 → max = max(24, 8) = 24

'''
class Solution:
    # 1) Recursion
    def splitArray(self, nums: list[int], k: int) -> int:
        n = len(nums)  # 배열의 길이

        # dfs(i, m): nums[i:]를 m개의 연속된 부분 배열로 나누었을 때,
        # 가장 작은 "최대 부분합"을 반환
        def dfs(i, m):
            if i == n:
                # 배열의 끝까지 왔을 때 정확히 m개의 조각으로 나눈 경우만 유효
                return 0 if m == 0 else float("inf")
            if m == 0:
                # 더 이상 나눌 수 없는데 아직 요소가 남았다면 불가능한 경우
                return float("inf")

            res = float("inf")  # 최소값을 찾기 위한 초기화
            curSum = 0  # 현재 부분 배열의 누적 합

            # nums[i:j+1]까지를 하나의 subarray로 잡고,
            # 나머지를 m-1개의 조각으로 나누는 경우 탐색
            # j는 최소한 m개의 조각을 만들 수 있도록 n - m 까지만 탐색
            for j in range(i, n - m + 1):
                curSum += nums[j]  # 부분합 누적
                # 현재 부분합과 이후 dfs 결과 중 최대값을 취하고, 그 중 최소를 선택
                res = min(res, max(curSum, dfs(j + 1, m - 1)))

            return res  # 최소화된 최대값 반환

        return dfs(0, k)  # 처음부터 시작해서 k개로 나누기
    
    # 2) Binary Search
    def splitArray(self, nums: list[int], k: int) -> int:
        # 주어진 최대 부분합(mid)로 나눌 수 있는지 확인하는 함수
        def canSplit(largest):
            subarray = 1  # 부분 배열의 개수 (처음은 하나로 시작)
            curSum = 0    # 현재 부분 배열의 합
            for num in nums:
                curSum += num
                if curSum > largest:
                    # 현재 부분합이 기준값보다 크면 새로운 부분 배열로 시작
                    subarray += 1
                    if subarray > k:
                        # k개를 초과하면 불가능
                        return False
                    curSum = num  # 새로운 부분 배열의 시작값
            return True  # k개 이하로 나눌 수 있으면 가능

        # 이분 탐색 범위: 하나의 원소가 최대값이 될 수 있으므로 최소는 max(nums),
        # 전체를 하나로 묶으면 최대는 sum(nums)
        l, r = max(nums), sum(nums)
        res = r  # 결과값 초기화

        # 이분 탐색 수행
        while l <= r:
            mid = l + (r - l) // 2  # 중간값: 가능한 최대 부분합
            if canSplit(mid):
                # mid로 나눌 수 있으면 더 작은 최대값을 찾기 위해 왼쪽 탐색
                res = mid
                r = mid - 1
            else:
                # mid로 나눌 수 없으면 더 큰 값이 필요하므로 오른쪽 탐색
                l = mid + 1

        return res  # 최소화된 최대 부분합 반환

        

if __name__=="__main__":
    sol = Solution()
    nums = [2,4,10,1,5]
    k = 2
    print(sol.splitArray(nums,k))