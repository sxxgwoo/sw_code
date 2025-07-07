# Longest Common Prefix
# 문제 설명: 문자열 배열 strs가 주어지면, 모든 문자열의 가장 긴 공통 접두사를 반환하는 함수를 작성하세요.
# 입력: ["flower","flow","flight"]
# 출력: "fl"
# 설명: "flower", "flow", "flight"의 가장 긴 공통 접두사는 "fl"입니다.

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
        if not strs:
            return ""
        
        # 가장 짧은 문자열 찾기
        shortest = min(strs, key=len)
        end = len(shortest)

        for i in range(end):
            ch = shortest[i]
            for s in strs:
                if s[i] != ch:
                    return shortest[:i]
        
        return shortest

# test case
print(longestCommonPrefix(["flower","flow","flight"])) # "fl"
print(longestCommonPrefix(["dog","racecar","car"])) # ""