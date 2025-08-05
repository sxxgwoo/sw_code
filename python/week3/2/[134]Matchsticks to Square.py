'''
Matchsticks to Square
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You need to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Example 1:

Input: matchsticks = [1,3,4,2,2,4]

Output: true

Example 2:

Input: matchsticks = [1,5,6,3]

Output: false
'''
class Solution:
    # 1) Brute Force
    def makesquare(self, matchsticks: list[int]) -> bool:
        # 전체 길이가 4로 나누어 떨어지지 않으면 정사각형 불가
        if sum(matchsticks) % 4 != 0:
            return False

        # 각 변의 길이를 저장할 리스트
        sides = [0] * 4

        def dfs(i):
            # 모든 성냥을 다 배치했으면 4변이 같아야 정사각형
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]

            # 현재 성냥(matchsticks[i])을 4개의 변 중 하나에 놓아보기
            for side in range(4):
                sides[side] += matchsticks[i]
                # 다음 성냥으로 진행
                if dfs(i + 1):
                    return True
                # 실패 시 백트래킹
                sides[side] -= matchsticks[i]

            return False  # 모든 시도가 실패하면 False 반환

        return dfs(0)
    # 2) Pruning
    def makesquare(self, matchsticks: list[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        length = total_length // 4  # 각 변의 목표 길이
        sides = [0] * 4

        # 큰 성냥부터 배치하면 백트래킹 가지치기 효율 ↑
        matchsticks.sort(reverse=True)

        def dfs(i):
            # 모든 성냥을 다 배치하면 성공
            if i == len(matchsticks):
                return True

            for side in range(4):
                # 현재 변에 성냥을 추가했을 때 길이를 넘지 않는 경우만 시도
                if sides[side] + matchsticks[i] <= length:
                    sides[side] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[side] -= matchsticks[i]  # 백트래킹

                # 가지치기 1: 해당 변이 0이면 다른 변도 0 → 대칭이므로 중복 탐색 X
                if sides[side] == 0:
                    break

            return False

        return dfs(0)
    
if __name__=="__main__":
    sol = Solution()
    matchsticks = [1,3,4,2,2,4]
    print(sol.makesquare(matchsticks))
    