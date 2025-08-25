'''
Reverse Integer
You are given a signed 32-bit integer x.

Return x after reversing each of its digits. After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.

Solve the problem without using integers that are outside the signed 32-bit integer range.

Example 1:

Input: x = 1234

Output: 4321
Example 2:

Input: x = -1234

Output: -4321
Example 3:

Input: x = 1234236467

Output: 0
'''
'''
Reverse Integer
You are given a signed 32-bit integer x.
Return x after reversing each of its digits.

조건:
- 뒤집은 값이 32-bit signed integer 범위를 벗어나면 0을 반환
- 범위: [-2^31, 2^31 - 1] = [-2147483648, 2147483647]
'''

class Solution:
    def reverse(self, x: int) -> int:
        # 재귀적으로 숫자를 뒤집는 함수
        def rec(n: int, rev: int) -> int:
            # n이 0이 되면 역순 완성 → rev 반환
            if n == 0:
                return rev
            # 맨 끝 자리를 rev에 붙이고, n을 10으로 나눈 몫으로 재귀 진행
            rev = rev * 10 + n % 10
            return rec(n // 10, rev)

        # 부호 처리 (음수면 sign = -1)
        sign = -1 if x < 0 else 1
        x = abs(x)

        # 재귀를 통해 숫자 뒤집기
        reversed_num = rec(x, 0)
        reversed_num *= sign  # 원래 부호 복원

        # 32-bit signed integer 범위 체크
        if reversed_num < -(1 << 31) or reversed_num > (1 << 31) - 1:
            return 0

        return reversed_num


# ===== 실행 예시 =====
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.reverse(1234))         # 기대 출력: 4321

    # Example 2
    print(sol.reverse(-1234))        # 기대 출력: -4321

    # Example 3 (범위 초과 → 0 반환)
    print(sol.reverse(1234236467))   # 기대 출력: 0