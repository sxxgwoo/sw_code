'''
Meeting Rooms
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
Note:

(0,8),(8,10) is not considered a conflict at 8
'''
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
# 별도 정렬 함수 (버블 정렬, start 기준 오름차순)
def sort_intervals(intervals: list[Interval]) -> list[Interval]:
    n = len(intervals)
    for i in range(n):
        for j in range(0, n - i - 1):
            if intervals[j].start > intervals[j + 1].start:
                intervals[j], intervals[j + 1] = intervals[j + 1], intervals[j]
    return intervals

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        # 회의 시작 시간을 기준으로 정렬
        # intervals.sort(key=lambda i: i.start)
        # 별도의 정렬 함수 사용
        intervals = sort_intervals(intervals)

        # 인접한 회의들끼리 겹치는지 확인
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]  # 이전 회의
            i2 = intervals[i]      # 현재 회의

            # 이전 회의 종료 시간이 현재 회의 시작 시간보다 크면 충돌 발생
            if i1.end > i2.start:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    # 튜플 리스트를 Interval 객체 리스트로 변환
    raw_intervals = [(0, 30), (5, 10), (15, 20)]
    intervals = [Interval(start, end) for start, end in raw_intervals]

    # 기대값: False (겹치는 회의 있음)
    print(sol.canAttendMeetings(intervals))

    raw_intervals2 = [(5, 8), (9, 15)]
    intervals2 = [Interval(start, end) for start, end in raw_intervals2]

    # 기대값: True (겹치는 회의 없음)
    print(sol.canAttendMeetings(intervals2))