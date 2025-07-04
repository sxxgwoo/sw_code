'''
Two Integer Sum II
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].
'''
class Solution:
    
    # 1) Brute Force
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []
    
    # 2) ** two pointers
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
    
    # 3) Binary Search
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # 배열의 각 원소 numbers[i]에 대해,
        # numbers[i+1:] 구간에서 (target - numbers[i]) 값을 이진 탐색으로 찾음
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1   # i보다 오른쪽 구간에서 이진 탐색
            tmp = target - numbers[i]       # 찾고자 하는 값: target - 현재 수

            # 이진 탐색 시작
            while l <= r:
                mid = l + (r - l) // 2       # 중앙 인덱스

                if numbers[mid] == tmp:
                    # 값이 일치하면 정답 발견 (1-based 인덱스 반환)
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    # 더 작은 수니까 오른쪽 탐색
                    l = mid + 1
                else:
                    # 더 큰 수니까 왼쪽 탐색
                    r = mid - 1

        # 문제에서 정답이 항상 존재하므로 보통 이 부분은 실행되지 않음
        return []

    
    # sw solution
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r=0,1
        s=[]
      
        while l<len(numbers)-1:
            while r<len(numbers):
                if target == (numbers[l] + numbers[r]):
                    print(r)
                    s.append(l+1)
                    s.append(r+1)
                    return s
                r+=1
            r=l+1
            l+=1


        
if __name__ == "__main__":
    sol = Solution()
    numbers=[-5,-3,0,2,4,6,8]
    target=5
    print(sol.twoSum(numbers,target))