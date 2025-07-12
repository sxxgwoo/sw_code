'''
Median of Two Sorted Arrays

You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

Your solution must run in O(log(m+n)) time.

Example 1:

Input: nums1 = [1,2], nums2 = [3]

Output: 2.0

Explanation: Among [1, 2, 3] the median is 2.

Example 2:

Input: nums1 = [1,3], nums2 = [2,4]

Output: 2.5

Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.
'''
from typing import List

# Two Pointers
def findMedianSortedArrays(nums1, nums2):
    len1, len2 = len(nums1), len(nums2)
    i = j = 0
    median1 = median2 = 0

    for _ in range((len1 + len2) // 2 + 1):
        median2 = median1
        if i < len1 and j < len2:
            if nums1[i] > nums2[j]:
                median1 = nums2[j]
                j += 1
            else:
                median1 = nums1[i]
                i += 1
        elif i < len1:
            median1 = nums1[i]
            i += 1
        else:
            median1 = nums2[j]
            j += 1

    if (len1 + len2) % 2 == 1:
        return float(median1)
    else:
        return (median1 + median2) / 2.0
    
# Binary Search
def get_kth(a: List[int], m: int, b: List[int], n: int, k: int, a_start: int = 0, b_start: int = 0) -> int:
    if m > n:
        return get_kth(b, n, a, m, k, b_start, a_start)
    if m == 0:
        return b[b_start + k - 1]
    if k == 1:
        return min(a[a_start], b[b_start])
    
    i = min(m, k // 2)
    j = min(n, k // 2)
    
    if a[a_start + i - 1] > b[b_start + j - 1]:
        return get_kth(a, m, b, n - j, k - j, a_start, b_start + j)
    else:
        return get_kth(a, m - i, b, n, k - i, a_start + i, b_start)

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    left = (len(nums1) + len(nums2) + 1) // 2
    right = (len(nums1) + len(nums2) + 2) // 2
    return (get_kth(nums1, len(nums1), nums2, len(nums2), left) +
            get_kth(nums1, len(nums1), nums2, len(nums2), right)) / 2.0

# ============================
# Test Case [1,3], [2,4] -> 2.5
# ============================
if __name__ == "__main__":
    res = findMedianSortedArrays([1,3], [2,4])

    print(res)