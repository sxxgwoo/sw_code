'''
Kth Largest Element in a Stream

Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

Implement the following methods:

constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

Example 1:

Input:
["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

Output:
[null, 3, 3, 3, 5, 6]

Explanation:
KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
kthLargest.add(3);   // return 3
kthLargest.add(5);   // return 3
kthLargest.add(6);   // return 3
kthLargest.add(7);   // return 5
kthLargest.add(8);   // return 6
'''
from typing import List

# Sorting
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

    def merge(self, lst1, lst2):
        i = j = 0
        res = []

        while i < len(lst1) and j < len(lst2):
            if(lst1[i] > lst2[j]):
                res.append(lst2[j])
                j += 1
            else:
                res.append(lst1[i])
                i += 1
        
        if(i == len(lst1)):
            res.extend(lst2[j:])
        if(j == len(lst2)):
            res.extend(lst1[i:])
        
        return res

    def mergeSort(self, lst):
        if(len(lst) <= 1):
            return lst
        
        mid = len(lst) // 2
        res1 = self.mergeSort(lst[:mid])
        res2 = self.mergeSort(lst[mid:])
        
        return self.merge(res1, res2)

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.mergeSort(self.arr)
        return self.arr[len(self.arr) - self.k]

# SH proof
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = self.mergeSort(nums)

    def merge(self, lst1, lst2):
        i = j = 0
        res = []

        while i < len(lst1) and j < len(lst2):
            if(lst1[i] > lst2[j]):
                res.append(lst2[j])
                j += 1
            else:
                res.append(lst1[i])
                i += 1
        
        if(i == len(lst1)):
            res.extend(lst2[j:])
        if(j == len(lst2)):
            res.extend(lst1[i:])
        
        return res

    def mergeSort(self, lst):
        if(len(lst) <= 1):
            return lst
        
        mid = len(lst) // 2
        res1 = self.mergeSort(lst[:mid])
        res2 = self.mergeSort(lst[mid:])

        return self.merge(res1, res2)
        
    def add(self, val: int) -> int:
        if(self.k > len(self.nums) + 1):
            return -1

        for i in range(len(self.nums)):
            if(self.nums[i] >= val):
                res = self.nums[:i] + [val] + self.nums[i:]
                self.nums = res
                return res[-self.k]
        
        self.nums.append(val)
        return self.nums[-self.k]

# ============================
# Test Case ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
# -> [null, 3, 3, 3, 5, 6]
# ============================
if __name__ == "__main__":
    obj = KthLargest(3, [1, 2, 3, 3])
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(6))
    print(obj.add(7))
    print(obj.add(8))