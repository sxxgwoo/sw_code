'''
Reverse Bits
Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

Example 1:

Input:  n = 00000000000000000000000000010101 (21)
Output:    2818572288 (10101000000000000000000000000000)
Explanation:
- 입력 n = 21 = 000...010101 (2진수)
- 비트를 반전 → 10101000000000000000000000000000
- 10진수로는 2818572288
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # 총 32비트 기준으로 반복
        for i in range(32):
            # i번째 비트를 추출 (오른쪽으로 i번 시프트 후, 마지막 비트만 취함)
            bit = (n >> i) & 1
            # 추출한 비트를 반대편 자리(31 - i)에 채워 넣음
            res |= (bit << (31 - i))
        return res


# ===== 실행 예시 =====
if __name__ == "__main__":
    sol = Solution()

    # 예시 1: n = 21 (000...010101)
    n = 21
    print(sol.reverseBits(n))
    # 기대 출력: 2818572288

    # 예시 2: n = 43261596
    # 원래: 00000010100101000001111010011100
    # 뒤집힘: 00111001011110000010100101000000 (964176192)
    n = 43261596
    print(sol.reverseBits(n))  # 기대 출력: 964176192