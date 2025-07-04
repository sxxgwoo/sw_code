# Contains Duplicate
# return true if nums[i] == nums[j] and |i-j| <= k
# Sliding Window Fixed Size
from typing import List

# Solution 1
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k + 1)):
            if nums[L] == nums[R]:
                return True
    return False

# Solution 2
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    mp = {}

    for i in range(len(nums)):
        if nums[i] in mp and i - mp[nums[i]] <= k:
            return True
        mp[nums[i]] = i
        
    return False

# ============================
# Test Case [1,2,3,1] -> true
# ============================
if __name__ == "__main__":
    nums = [1,2,3,1]
    k = 3
    flag = containsNearbyDuplicate(nums,k)

    print(flag)