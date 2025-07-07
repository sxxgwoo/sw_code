# Valid Anagram
# 문제 설명: 두 문자열 s와 t가 주어지면, s와 t가 애너그램인지 확인하는 함수를 작성하세요.
# 애너그램은 두 문자열이 같은 문자로 이루어져 있고 그 문자의 개수가 같은 경우를 말합니다.
# 입력: s = "anagram", t = "nagaram"
# 출력: True
# 설명: s와 t는 애너그램입니다.

# 방법 1
# def isAnagram(s: str, t: str) -> bool:
#     return sorted(s) == sorted(t)

# 방법 2
from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# test case
print(isAnagram("anagram", "nagaram")) # True
print(isAnagram("rat", "car")) # False