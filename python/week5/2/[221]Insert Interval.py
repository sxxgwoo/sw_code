'''
Insert Interval
You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

You are given another interval newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return intervals after adding newInterval.

Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

Example 1:

Input: intervals = [[1,3],[4,6]], newInterval = [2,5]

Output: [[1,6]]
Example 2:

Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]

Output: [[1,2],[3,5],[6,7],[9,10]]
'''
class Solution:
    # 1) Greedy 방식
    # 아이디어:
    # - intervals는 이미 start 기준으로 정렬되어 있고, 겹치지 않음
    # - newInterval을 순회하면서 적절한 위치에 삽입/병합
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []

        for i in range(len(intervals)):
            # case 1: newInterval이 intervals[i]보다 완전히 왼쪽에 있음 (더 이상 병합 불필요)
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]  # 뒤에 나머지 붙여서 종료

            # case 2: newInterval이 intervals[i]보다 완전히 오른쪽에 있음
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])  # 그냥 기존 interval 추가

            # case 3: newInterval과 intervals[i]가 겹침 → 병합
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),  # 시작은 더 작은 값
                    max(newInterval[1], intervals[i][1]),  # 끝은 더 큰 값
                ]

        # 모든 interval 확인 후 newInterval 추가
        res.append(newInterval)
        return res
    

    # 2) Binary Search + 병합
    # 아이디어:
    # - newInterval의 시작 위치를 이진 탐색으로 찾아 삽입
    # - 이후 전체 intervals에서 겹치는 구간 병합
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:  # intervals가 비어있으면 그대로 반환
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        # newInterval[0]을 기준으로 삽입 위치 탐색
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        # newInterval 삽입
        intervals.insert(left, newInterval)

        # 병합 과정
        res = []
        for interval in intervals:
            # res가 비었거나, 겹치지 않으면 새로운 구간 추가
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # 겹치면 끝 값을 확장
                res[-1][1] = max(res[-1][1], interval[1])
        return res


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 2], [3, 5], [9, 10]]
    newInterval = [6, 7]
    # 출력: [[1,2],[3,5],[6,7],[9,10]]
    print(sol.insert(intervals, newInterval))