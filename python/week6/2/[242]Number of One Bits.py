'''
Number of One Bits
You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.

Example 1:

Input: n = 00000000000000000000000000010111

Output: 4
Example 2:

Input: n = 01111111111111111111111111111101

Output: 30
'''
class Solution:
    # 방법 1. 모든 32비트 자리 확인
    def hammingWeight(self, n: int) -> int:
        res = 0
        # 0~31번째 비트 확인 (32비트 정수라 가정)
        for i in range(32):
            # (1 << i)는 i번째 비트가 1인 값
            # n과 & 연산하면 해당 비트가 켜져있는지 확인 가능
            if (1 << i) & n:
                res += 1  # 1비트면 카운트 증가
        return res
    
    # 방법 2. Brian Kernighan 알고리즘
    def hammingWeight(self, n: int) -> int:
        """
        핵심 아이디어:
        n & (n - 1)은 n의 최하위 1비트를 제거한 값이 된다.
        따라서 while 루프를 돌며 1비트 개수를 직접 세는 방식.
        """
        res = 0
        while n:
            n &= n - 1  # 가장 오른쪽 1비트 제거
            res += 1    # 제거할 때마다 카운트 증가
        return res
if __name__ == "__main__":
    sol = Solution()
    
    # 10진수 그대로 넣기
    n = 23   # 23의 이진수는 10111 → 1의 개수 = 4
    print(sol.hammingWeight(n))  # 출력: 4

    # 2진수 리터럴로 넣기
    n = 0b10111  # 동일하게 23
    print(sol.hammingWeight(n))  # 출력: 4

    # 두 번째 예시 (30개 1비트)
    n = 0b01111111111111111111111111111101
    print(sol.hammingWeight(n))  # 출력: 30