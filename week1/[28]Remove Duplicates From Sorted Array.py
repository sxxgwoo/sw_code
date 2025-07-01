'''
Remove Duplicates From Sorted Array
You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.

After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

Note:

The order of the unique elements should remain the same as in the original array.
It is not necessary to consider elements beyond the first k positions of the array.
To be accepted, the first k elements of nums must contain all the unique elements.
Return k as the final result.

Example 1:

Input: nums = [1,1,2,3,4]

Output: [1,2,3,4]
Explanation: You should return k = 4 as we have four unique elements.

Example 2:

Input: nums = [2,10,10,30,30,30]

Output: [2,10,30]
Explanation: You should return k = 3 as we have three unique elements.
'''
class Solution:
    # 1) ** Two Pointers - I
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)          # 배열 길이
        l = r = 0              # l: 유일값을 채울 위치, r: 전체 순회 포인터

        # 전체 배열 순회
        while r < n:
            nums[l] = nums[r]  # 현재 r 위치 값을 l 위치로 복사
            # r이 가리키는 값이 동일한 동안 계속 r 이동 (중복 건너뛰기)
            while r < n and nums[r] == nums[l]:
                r += 1
            l += 1             # 다음 유일값을 채울 위치로 이동

        return l               # 중복 제거된 길이

    
    # 2) Two Pointers - II
    def removeDuplicates(self, nums: list[int]) -> int:
        # 왼쪽 포인터 l은 중복 없이 채워야 할 위치
        l = 1

        # 오른쪽 포인터 r은 배열 전체를 순회하며 중복 여부를 검사
        for r in range(1, len(nums)):
            # 이전 숫자와 다르면 → 새로운 숫자!
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]  # 새로운 숫자를 l 위치에 덮어쓰기
                l += 1             # 다음 덮어쓸 위치로 이동

        # 중복을 제거한 실제 길이 l 반환
        return l
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2,3,4]
    print(sol.removeDuplicates(nums))
    print(nums) # in-place로 space complexity 낮춤
