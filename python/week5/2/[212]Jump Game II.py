'''
Jump Game II
You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i. For example, if you are at nums[i], you can jump to any index i + j where:

j <= nums[i]
i + j < nums.length
You are initially positioned at nums[0].

Return the minimum number of jumps to reach the last position in the array (index nums.length - 1). You may assume there is always a valid answer.

Example 1:

Input: nums = [2,4,1,1,1,1]

Output: 2
Explanation: Jump from index 0 to index 1, then jump from index 1 to the last index.

Example 2:

Input: nums = [2,1,2,1,0]

Output: 2
'''
class Solution:
    # 1) BFS (Greedy) 접근
    # 아이디어: "레벨 탐색"처럼 현재 점프 범위 [l, r] 안에서
    # 갈 수 있는 가장 먼 위치(farthest)를 갱신하면서 최소 점프 횟수를 구함.
    def jump(self, nums: list[int]) -> int:
        res = 0       # 점프 횟수
        l = r = 0     # 현재 점프 범위의 시작(l)과 끝(r)

        # 마지막 인덱스에 도달하기 전까지 반복
        while r < len(nums) - 1:
            farthest = 0
            # 현재 점프 범위 [l, r] 내에서 가장 멀리 갈 수 있는 위치 탐색
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            # 다음 점프 범위를 [r+1, farthest]로 이동
            l = r + 1
            r = farthest
            res += 1  # 점프 횟수 증가
        return res
    

    # 2) Dynamic Programming (Bottom-Up)
    # 아이디어: dp[i] = i번째 인덱스에서 끝까지 가기 위한 최소 점프 수
    # 뒤에서 앞으로 채우면서, 각 위치에서 도달 가능한 인덱스들의 dp값을 참고
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1000000] * n  # 큰 값으로 초기화 (무한대 대체)
        dp[-1] = 0          # 마지막 위치에서는 점프가 필요 없음

        # 뒤에서 앞으로 탐색
        for i in range(n - 2, -1, -1):
            # i에서 도달 가능한 범위 = (i+1) ~ (i+nums[i])
            end = min(n, i + nums[i] + 1)
            for j in range(i + 1, end):
                # i에서 j로 점프 후 dp[j]로 가는 경우
                dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]  # 시작 위치에서의 최소 점프 수 반환
    

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 4, 1, 1, 1, 1]
    # 출력: 2
    # 경로 예: index 0 (jump to index 1) → index 1 (jump to index 5)
    print(sol.jump(nums))