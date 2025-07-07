# Encode and Decode Strings
# 문제 설명: 문자열 배열 strs를 주어지면, 문자열 배열을 하나의 문자열로 인코딩하고 디코딩하는 함수를 작성하세요.
# 입력: ["hello","world"]
# 출력: "5#hello5#world"
# 설명: 문자열 배열을 인코딩하면 "5#hello5#world"가 됩니다.

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        We prefix each string with its length and a delimiter '#'.
        """
        # e.g. ["hello","world"] -> "5#hello5#world"
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string back to a list of strings.
        We read the length prefix up to the '#' delimiter, then extract that many characters.
        """
        res = []
        i = 0
        n = len(s)
        while i < n:
            # read length
            j = i
            # move j until delimiter
            while j < n and s[j] != "#":
                j += 1
            length = int(s[i:j])
            # extract the string of that length after '#'
            start = j + 1
            res.append(s[start:start + length])
            # advance i past this segment
            i = start + length
        return res
    
# test case
solution = Solution()
print(solution.encode(["hello","world"])) # "5#hello5#world"
print(solution.decode("5#hello5#world")) # ["hello","world"]