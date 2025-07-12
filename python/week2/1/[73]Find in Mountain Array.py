# 1095. Find in Mountain Array
# https://leetcode.com/problems/find-in-mountain-array/
# Problem description
# (This problem is an interactive problem.)
# You may recall that an array arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Solution 1: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

def _binary_search(mountainArr: list[int], left: int, right: int, target: int, ascending: bool) -> int:
    """
    지정된 구간 [left..right]에서 target을 이진 탐색.
    ascending=True이면 오름차순, False면 내림차순 배열로 간주.
    """
    while left <= right:
        mid = (left + right) // 2
        val = mountainArr[mid]
        if val == target:
            return mid
        # 오름차순일 때
        if ascending:
            if val < target:
                left = mid + 1
            else:
                right = mid - 1
        # 내림차순일 때
        else:
            if val > target:
                left = mid + 1
            else:
                right = mid - 1
    return -1

def findInMountainArray(target: int, mountainArr: list[int]) -> int:
    """
    mountainArr는 봉우리(peak)를 기준으로 좌측이 오름차순,
    우측이 내림차순인 배열입니다.
    1) 먼저 이진 탐색으로 봉우리 인덱스를 찾고,
    2) 봉우리 왼쪽(오름차순)에서 target을 이진 탐색,
    3) 못 찾으면 봉우리 오른쪽(내림차순)에서 이진 탐색합니다.
    전체 get 호출은 O(log n) 수준으로 100회 이내 보장됩니다.
    """
    n = len(mountainArr)
    
    # 1. 봉우리 인덱스 찾기 (오르막-내리막 경계)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        # mid와 mid+1 비교해서 경사 방향 판단
        if mountainArr[mid] < mountainArr[mid + 1]:
            # 오른쪽이 더 크면 아직 오르막
            left = mid + 1
        else:
            # 아니면 내리막 혹은 peak 위치
            right = mid
    peak = left  # peak 인덱스
    
    # 2. 왼쪽 구간(0..peak) 오름차순 이진 탐색
    res = _binary_search(mountainArr, 0, peak, target, ascending=True)
    if res != -1:
        return res
    
    # 3. 오른쪽 구간(peak+1..n-1) 내림차순 이진 탐색
    return _binary_search(mountainArr, peak + 1, n - 1, target, ascending=False)


# Test cases
mountainArr = [2,4,5,2,1]
target = 2
print(findInMountainArray(2, [2,4,5,2,1])) # 0 
print(findInMountainArray(6, [1,2,3,4,2,1])) # -1