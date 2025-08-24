'''
Maximum Sum Circular Subarray
You are given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:

Input: nums = [-2,4,-5,4,-5,9,4]

Output: 15
Explanation: Subarray [-2,4,9,4] has maximum sum 15.

Example 2:

Input: nums = [2,3,-4]

Output: 5
문제 요약
	•	정수 배열 nums가 원형(circular) 구조로 주어짐.
	•	원형 배열이란, 끝과 처음이 연결된 배열을 의미함.
예: [a, b, c]라면 c 다음은 다시 a.
	•	이 배열에서 가능한 연속된 부분 배열(subarray) 중에서,
원형을 고려했을 때 합이 가장 큰 값을 구하는 문제.
'''
class Solution:
    # 1) Kadane's Algorithm 변형
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        # globMax: 지금까지의 최대 부분합
        # globMin: 지금까지의 최소 부분합
        # curMax: 현재까지 고려한 구간에서의 최대 부분합
        # curMin: 현재까지 고려한 구간에서의 최소 부분합
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0  # 배열 전체 합

        for num in nums:
            # 최대 부분합 (Kadane’s 알고리즘)
            curMax = max(curMax + num, num)
            globMax = max(globMax, curMax)

            # 최소 부분합 (Kadane’s 알고리즘 응용)
            curMin = min(curMin + num, num)
            globMin = min(globMin, curMin)

            total += num  # 전체 합 누적

        # 원형 배열 최대 부분합 = max(일반 최대 부분합, 전체합 - 최소 부분합)
        # 단, 모두 음수라면 total - globMin은 잘못된 값이므로 globMax 반환
        return max(globMax, total - globMin) if globMax > 0 else globMax
    

    # 2) Prefix & Suffix Sums 방식
    # 아이디어: 배열을 두 부분(prefix + suffix)로 나누어 연결한 원형 subarray 고려
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        n = len(nums)

        # 오른쪽에서 시작하는 suffix의 최대합 배열 (i~끝까지 중 최대)
        right_max = [0] * n
        right_max[-1] = nums[-1]
        suffix_sum = nums[-1]

        # 뒤에서 앞으로 누적합을 계산하면서 각 위치의 suffix 최대값 갱신
        for i in range(n - 2, -1, -1):
            suffix_sum += nums[i]
            right_max[i] = max(right_max[i + 1], suffix_sum)

        max_sum = nums[0]  # 전체 최대 subarray 합
        cur_max = 0        # Kadane’s 알고리즘용 현재 최대
        prefix_sum = 0     # 앞에서부터 누적합

        for i in range(n):
            # Kadane’s 알고리즘으로 일반 최대 subarray 합 구하기
            cur_max = max(cur_max, 0) + nums[i]
            max_sum = max(max_sum, cur_max)

            # prefix 합 갱신
            prefix_sum += nums[i]

            # 원형 subarray 고려: prefix(i까지) + suffix(i+1부터 끝)
            if i + 1 < n:
                max_sum = max(max_sum, prefix_sum + right_max[i + 1])

        return max_sum
    

if __name__ == "__main__":
    sol = Solution()
    nums = [-2, 4, -5, 4, -5, 9, 4]
    # 정답: 15 (예: [-2, 4, 9, 4])
    print(sol.maxSubarraySumCircular(nums))