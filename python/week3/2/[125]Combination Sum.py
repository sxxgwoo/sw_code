'''
Combination Sum
#Tree Maze #Combinations
You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

Input: 
nums = [2,5,6,9] 
target = 9

Output: [[2,2,5],[9]]
Explanation:
2 + 2 + 5 = 9. We use 2 twice, and 5 once.
9 = 9. We use 9 once.

Example 2:

Input: 
nums = [3,4,5]
target = 16

Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]
Example 3:

Input: 
nums = [3]
target = 5

Output: []

Combination Sum 문제
- 주어진 배열 nums의 원소들을 사용해서 합이 target이 되는 모든 조합을 구하는 문제
- 각 숫자는 무제한으로 사용할 수 있다.
- 조합에서 숫자의 순서는 상관없다(즉, [2,2,5]와 [2,5,2]는 동일한 조합).
'''

class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []  # 최종적으로 모든 조합을 담을 리스트

        # DFS(깊이 우선 탐색) + 백트래킹
        # i: 현재 탐색할 nums의 인덱스
        # cur: 현재까지 선택한 숫자 조합
        # total: 현재까지 선택한 숫자의 합
        def dfs(i, cur, total):
            # 1) 합이 target과 같으면 정답에 추가
            if total == target:
                res.append(cur.copy())  # 현재 조합을 복사해서 저장
                return
            
            # 2) 인덱스를 벗어나거나 합이 target을 초과하면 종료 (백트래킹)
            if i >= len(nums) or total > target:
                return

            # 3) 현재 숫자를 선택하는 경우
            cur.append(nums[i])               # 숫자 추가
            dfs(i, cur, total + nums[i])      # 같은 숫자를 계속 사용할 수 있으므로 i 유지
            cur.pop()                         # 원상복구 (백트래킹)

            # 4) 현재 숫자를 선택하지 않고 다음 숫자로 넘어가는 경우
            dfs(i + 1, cur, total)

        # DFS 탐색 시작
        dfs(0, [], 0)
        return res

# 실행 예시
if __name__=="__main__":
    sol = Solution()
    nums = [2, 5, 6, 9]
    target = 9
    print(sol.combinationSum(nums, target))  # 출력: [[2, 2, 5], [9]]
    