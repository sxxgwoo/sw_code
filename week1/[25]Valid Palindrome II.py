'''
Valid Palindrome II
You are given a string s, return true if the s can be a palindrome after deleting at most one character from it.

A palindrome is a string that reads the same forward and backward.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "aca"

Output: true
Explanation: "aca" is already a palindrome.

Example 2:

Input: s = "abbadc"

Output: false
Explanation: "abbadc" is not a palindrome and can't be made a palindrome after deleting at most one character.

Example 3:

Input: s = "abbda"

Output: true
Explanation: "We can delete the character 'd'.

#slicing
s[::-1]
핵심 개념: 생략 시 기본값
슬라이싱 구문 s[start:stop:step]에서
start와 stop이 생략되었을 때의 기본값은 step의 부호에 따라 달라집니다.

| 생략된 항목  | `step > 0`일 때 기본값 | `step < 0`일 때 기본값 |
| ------- | ----------------- | ----------------- |
| `start` | `0`               | `len(s) - 1`      |
| `stop`  | `len(s)`          | `-1`              |

'''
    
class Solution:
    
    #1)** sw solution two pointers
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # 한 번이라도 다르면 왼쪽 or 오른쪽 하나 제거한 버전이 회문인지 확인
                s1 = s[l+1:r+1]
                s2 = s[l:r]
                # 한번이라도 더 다르면 false라는 뜻
                return s1 == s1[::-1] or s2 == s2[::-1]
            l += 1
            r -= 1

        return True
    
    # 2) Brute Force
    def validPalindrome(self, s: str) -> bool:
        # 먼저 원래 문자열이 이미 회문이면 바로 True 반환
        if s == s[::-1]:
            return True
        
        # 문자열의 각 인덱스 i를 한 번씩 제거해보면서 검사
        for i in range(len(s)):
            # i번째 문자를 제거한 문자열 생성
            newS = s[:i] + s[i + 1:]
            
            # 제거한 문자열이 회문이면 True 반환
            if newS == newS[::-1]:
                return True
        
        # 모든 경우를 다 확인했는데도 회문이 안 되면 False
        return False


if __name__ == "__main__":
    sol = Solution()
    s="aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    # s="aguok/epatg/bnvfq/mgmlc/upuuf/xoohd/fpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfd/hooxf/uupuc/ulmgm/qfvnb/gtape/kouga"
    # s = "abbda"
    print(sol.validPalindrome(s))
