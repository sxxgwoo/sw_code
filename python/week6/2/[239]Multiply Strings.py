'''
Multiply Strings
You are given two strings num1 and num2 that represent non-negative integers.

Return the product of num1 and num2 in the form of a string.

Assume that neither num1 nor num2 contain any leading zero, unless they are the number 0 itself.

Note: You can not use any built-in library to convert the inputs directly into integers.

Example 1:

Input: num1 = "3", num2 = "4"

Output: "12"
Example 2:

Input: num1 = "111", num2 = "222"

Output: "24642"
'''
class Solution:
    # 1. Multiplication (문자열 곱셈 직접 구현)
    def multiply(self, num1: str, num2: str) -> str:
        # 곱할 수 중 하나라도 "0"이면 결과는 무조건 "0"
        if "0" in [num1, num2]:
            return "0"

        # 결과 자리수는 최대 len(num1) + len(num2)
        res = [0] * (len(num1) + len(num2))

        # 곱셈을 뒤에서부터 (일의 자리부터) 하기 위해 문자열 뒤집기
        num1, num2 = num1[::-1], num2[::-1]

        # 각 자리수 곱셈 수행 (전통적인 수학 곱셈 방식)
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                # 현재 자리수의 곱
                digit = int(num1[i1]) * int(num2[i2])

                # 결과 배열에 더해주기 (자리 맞추기: i1+i2 위치)
                res[i1 + i2] += digit

                # 올림 처리 (carry)
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10  # 한 자리만 남기기

        # 결과 배열 뒤집기 (앞쪽부터 큰 자리수)
        res = res[::-1]

        # 앞쪽의 leading zero 제거
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        # 남은 자리들을 문자열로 변환
        res = map(str, res[beg:])
        return "".join(res)


# ===== 실행 예시 =====
if __name__ == "__main__":
    sol = Solution()

    num1 = "111"
    num2 = "222"
    print(sol.multiply(num1, num2))  # 기대값: "24642"

    num1 = "3"
    num2 = "4"
    print(sol.multiply(num1, num2))  # 기대값: "12"