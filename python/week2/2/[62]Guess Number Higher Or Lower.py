'''
Guess Number Higher Or Lower
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

0: your guess is equal to the number I picked (i.e. num == pick).
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
Return the number that I picked.

Example 1:

Input: n = 5, pick = 3

Output: 3
Example 2:

Input: n = 15, pick = 10

Output: 10
Example 3:

Input: n = 1, pick = 1

Output: 1
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# --- 로컬용 guess API 시뮬레이션 ---
pick = None  # 전역으로 숨겨놓은 정답

def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1

# --- 실제 풀이 클래스 ---
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while True:
            m = (l + r) // 2
            res = guess(m)
            if res > 0:
                l = m + 1  # 너무 작음 → 오른쪽으로
            elif res < 0:
                r = m - 1  # 너무 큼 → 왼쪽으로
            else:
                return m  # 정답 찾음

# --- 테스트 코드 ---
if __name__ == "__main__":
    sol = Solution()

    # 예시 테스트 1
    pick = 3
    print(f"Pick: {pick}, Found: {sol.guessNumber(5)}")  # → 3

    # 예시 테스트 2
    pick = 10
    print(f"Pick: {pick}, Found: {sol.guessNumber(15)}")  # → 10

    # 예시 테스트 3
    pick = 1
    print(f"Pick: {pick}, Found: {sol.guessNumber(1)}")  # → 1