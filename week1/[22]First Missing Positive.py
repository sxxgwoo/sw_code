'''
First Missing Positive
You are given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [-2,-1,0]

Output: 1
Example 2:

Input: nums = [1,2,4]

Output: 3
Example 3:

Input: nums = [1,2,4,5,6,3,1]

Output: 7
'''
class Solution:

    # 1) sw solution
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()

        if nums[-1]<=0:
            return 1
        for i in range(1,nums[-1]+2):
            if i in nums:
                continue
            return i
        
    # 2) Brute Force
    def firstMissingPositive(self, nums: list[int]) -> int:
        missing = 1
        while True:
            flag = True
            for num in nums:
                if missing == num:
                    flag = False
                    break

            if flag:
                return missing
            missing += 1

    # 3) Boolean Array
    def firstMissingPositive(self, nums: list[int]) -> int:
        '''
        예시 1: nums = [3, 4, -1, 1]
        Step 1. 초기화
        n = 4 (배열 길이)
        seen = [False, False, False, False] (1부터 4까지 있는지 체크할 리스트)

        Step 2. 값 체크
        num = 3 → 1~4 사이 → seen[2] = True → seen = [False, False, True, False]
        num = 4 → 1~4 사이 → seen[3] = True → seen = [False, False, True, True]
        num = -1 → 무시 (음수)
        num = 1 → 1~4 사이 → seen[0] = True → seen = [True, False, True, True]

        Step 3. 결과 확인
        seen[0] = True → 1 있음
        seen[1] = False → 2 없음 → 정답은 2
        ✔ 결과: 2
        seen은 그냥 1,2,...,n 개 양수 
        '''
        n = len(nums)  # 배열의 길이를 저장
        seen = [False] * n  # 길이 n만큼의 False 리스트를 만들어, 각 숫자의 존재 여부를 표시할 준비

        # 1부터 n까지의 숫자가 리스트에 있는지 확인
        for num in nums:
            if num > 0 and num <= n:
                # 만약 1 <= num <= n 이라면, seen[num - 1] 을 True로 표시 (숫자 num이 있다는 뜻)
                seen[num - 1] = True

        # seen 배열을 순회하면서 False인 첫 번째 인덱스를 찾음
        for num in range(1, n + 1):
            if not seen[num - 1]:
                # 만약 seen[num - 1]이 False라면, 숫자 num이 없다는 뜻이므로 반환
                return num

        # 1부터 n까지 모든 숫자가 존재한다면, 그 다음 숫자인 n + 1이 첫 번째로 없는 양의 정수
        return n + 1
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,4,5,6,3,1]
    print(sol.firstMissingPositive(nums))