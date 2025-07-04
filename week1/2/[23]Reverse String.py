'''
Reverse String
#two pointers
You are given an array of characters which represents a string s. Write a function which reverses a string.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["n","e","e","t"]

Output: ["t","e","e","n"]
Example 2:

Input: s = ["r","a","c","e","c","a","r"]

Output: ["r","a","c","e","c","a","r"]

문법 range
range(시작, 끝 전까지, 증가폭)
for i in range(4, -1, -1):  # i는 4, 3, 2, 1, 0 순서로 반복됨
for i in range(4, 2, -1):  # i는 4, 3 순서로 반복됨

'''

class Solution:
    # 1) array
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = []
        for i in range(len(s) - 1, -1, -1):
            tmp.append(s[i])
        for i in range(len(s)):
            s[i] = tmp[i]

    # 2)** two pointers
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    
if __name__ == "__main__":
    sol = Solution()
    s = ["n","e","e","t"]
    sol.reverseString(s)
    print(s)