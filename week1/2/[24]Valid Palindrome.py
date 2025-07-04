'''
Valid Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

"A".lower() -> "a"
.isalpha() (알파벳만), .isdigit() (숫자만)
.isalnum()은 문자열 메서드로, 해당 문자열이 알파벳(a-z, A-Z) 또는 숫자(0-9) 로만 구성되어 있는지를 확인해 줍니다.

#slicing
s[start:stop:step]

ord()는 문자 하나를 입력받아 그 문자의 유니코드(Unicode) 정수 값을 반환하는 내장 함수입니다.
print(ord('a'))   # 97
print(ord('A'))   # 65
print(ord('0'))   # 48
print(ord('한'))  # 54620
print(ord('!'))   # 33
'''

class Solution:
    # 1) Reverse String
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        
        # 주어진 문자열에서 알파벳 또는 숫자인 문자만 골라 소문자로 추가
        for c in s:
            if c.isalnum():               # 영문자 또는 숫자인지 확인
                newStr += c.lower()       # 모두 소문자로 변환해서 이어붙임
        
        # newStr이 뒤집은 문자열과 같은지 확인 → 회문 여부 판단
        return newStr == newStr[::-1]     # True면 회문, False면 아님

    # 2) Two pointers
    # 두 포인터 방식으로 주어진 문자열이 회문인지 검사하는 함수
    def isPalindrome(self, s: str) -> bool:
        # 왼쪽 포인터(l)는 문자열의 시작, 오른쪽 포인터(r)는 끝에서 시작
        l, r = 0, len(s) - 1

        while l < r:
            # 왼쪽 포인터가 알파벳이나 숫자가 아닐 경우 오른쪽으로 이동
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # 오른쪽 포인터가 알파벳이나 숫자가 아닐 경우 왼쪽으로 이동
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # 알파벳 또는 숫자인 경우, 대소문자 구분 없이 비교
            if s[l].lower() != s[r].lower():
                return False  # 다르면 회문이 아님
            # 다음 문자로 이동
            l, r = l + 1, r - 1

        return True  # 끝까지 다 확인하면 회문임

    # 문자가 알파벳 또는 숫자인지 판별하는 함수
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or   # 대문자
                ord('a') <= ord(c) <= ord('z') or   # 소문자
                ord('0') <= ord(c) <= ord('9'))     # 숫자

    

if __name__ == "__main__":
    sol = Solution()
    s = "Was it a car or a cat I saw?"
    print(sol.isPalindrome(s))