'''
Plus One
You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.

Example 1:

Input: digits = [1,2,3,4]

Output: [1,2,3,5]
Explanation 1234 + 1 = 1235.

Example 2:

Input: digits = [9,9,9]

Output: [1,0,0,0]
'''
class Solution:
    # 1. sw sol
    def plusOne(self, digits: list[int]) -> list[int]:
        n=len(digits)
        res=0
        for i in range(n):
            res+=digits[i]*(10**(n-1-i))
        res +=1
        plus=[]
        for i in str(res):
            plus.append(int(i))
        return plus
    
    #2. recursion
    def plusOne(self, digits: list[int]) -> list[int]:
        if not digits:
            return [1]

        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]
if __name__ == "__main__":
    sol = Solution()
    digits = [1,2,3,4]
    print(sol.plusOne(digits))
    digits = [9,9,9]
    print(sol.plusOne(digits))