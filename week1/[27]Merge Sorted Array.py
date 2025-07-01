'''
Merge Sorted Array
You are given two integer arrays nums1 and nums2, both sorted in non-decreasing order, along with two integers m and n, where:

m is the number of valid elements in nums1,
n is the number of elements in nums2.
The array nums1 has a total length of (m+n), with the first m elements containing the values to be merged, and the last n elements set to 0 as placeholders.

Your task is to merge the two arrays such that the final merged array is also sorted in non-decreasing order and stored entirely within nums1.
You must modify nums1 in-place and do not return anything from the function.

nums1에는 길이가 m + n인 공간이 주어지고,
그 중 앞 m개는 정렬된 값, 뒤 n개는 0 (혹은 빈 공간)으로 남아있음.
nums2는 길이 n의 정렬된 배열.

이 두 배열을 정렬된 상태로 nums1에 in-place로 병합하는 함수.


Example 1:

Input: nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2

Output: [1,2,10,20,20,40]
Example 2:

Input: nums1 = [0,0], m = 0, nums2 = [1,2], n = 2

Output: [1,2]
'''
class Solution:
    
    # 1) ** Three Pointers Without Extra Space - II
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        last = m + n - 1          # nums1의 마지막 인덱스 (가장 뒤부터 채울 예정)
        i, j = m - 1, n - 1       # i는 nums1의 유효 구간 끝, j는 nums2의 끝

        # nums2가 빌 때까지 반복 (j가 -1보다 크면 아직 비교할 값 있음)
        while j >= 0:
            # nums1[i]가 더 크면 뒤로 옮김
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                # nums2[j]가 더 크거나 같으면 옮김
                nums1[last] = nums2[j]
                j -= 1
                
            last -= 1  # 하나 채울 때마다 뒤로 이동
            
    # 2) Three Pointers With Extra Space
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
     
        # nums1의 앞 m개를 복사해 새로운 배열에 저장
        nums1_copy = nums1[:m]

        # 포인터: idx는 최종 결과를 쓸 위치, i는 nums1_copy, j는 nums2
        idx = 0
        i = j = 0

        # 총 m+n개의 자리를 모두 채울 때까지 반복
        while idx < m + n:
            # 조건 1: nums2를 다 썼거나, nums1_copy[i]가 더 작거나 같은 경우
            if j >= n or (i < m and nums1_copy[i] <= nums2[j]):
                nums1[idx] = nums1_copy[i]  # nums1_copy에서 값 가져오기
                i += 1
            else:
                nums1[idx] = nums2[j]       # nums2에서 값 가져오기
                j += 1

            idx += 1  # 다음 자리에 쓰기 위해 증가


if __name__ == "__main__":
    sol = Solution()
    nums1, nums2 = [10,20,20,40,0,0], [1,2]
    m, n = 4, 2
    print(sol.merge(nums1, m, nums2, n))
    print(nums1)