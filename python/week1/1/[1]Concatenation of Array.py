#concatenation of arrays
# 문제 설명: 배열 nums가 주어지면, 배열 nums를 두 번 연결한 배열을 반환하는 함수를 작성하세요.
# 입력: [1,2,1]
# 출력: [1,2,1,1,2,1]
# 설명: 배열 nums를 두 번 연결한 배열을 반환합니다.

from typing import List

def getConcatenation(nums: List[int]) -> List[int]:
    return nums+nums

# test case
print(getConcatenation([1,2,1]))