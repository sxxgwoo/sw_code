# Group Anagrams
# 문제 설명: 문자열 배열 strs가 주어지면, 애너그램 그룹을 반환하는 함수를 작성하세요.
# 애너그램 그룹은 같은 문자로 이루어져 있는 문자열들의 그룹을 말합니다.
# 입력: ["eat","tea","tan","ate","nat","bat"]
# 출력: [["eat","tea","ate"],["tan","nat"],["bat"]]
# 설명: "eat", "tea", "ate"는 애너그램 그룹입니다.
# "tan", "nat"는 애너그램 그룹입니다.
# "bat"는 애너그램 그룹이 아닙니다.

from typing import List
from collections import defaultdict
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)

    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)

    return list(groups.values())

# test case
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["eat","tea","ate"],["tan","nat"],["bat"]]