# 735. Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/
# Problem description
# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions.
# If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode.

# Solution 1: Stack Simulation
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    """
    스택을 이용한 O(n) 시뮬레이션 풀이
    양수(→) 소행성이 스택에 쌓이고, 음수(←) 소행성이 오면 충돌을 처리합니다.
    """
    stack: List[int] = []
    
    for a in asteroids:
        # 현재 소행성이 양수이거나, 스택이 비어 있거나, 스택 최상단이 음수이면
        # 충돌이 일어나지 않으므로 그냥 push
        if a > 0 or not stack or stack[-1] < 0:
            stack.append(a)
        else:
            # a < 0 이고 stack[-1] > 0 인 경우에만 충돌 가능
            while True:
                top = stack[-1]
                # 1) top(양수) 크기가 더 크면 a가 파괴
                if top > -a:
                    # a 소행성은 사라지고, 더 이상 처리할 필요 없음
                    break
                # 2) 크기가 같으면 둘 다 파괴
                elif top == -a:
                    stack.pop()
                    break
                else:
                    # 3) a의 절댓값이 더 크면 스택 최상단 파괴, 계속 충돌 검사
                    stack.pop()
                    # 스택이 비었거나 최상단이 음수가 되면 a를 추가하고 종료
                    if not stack or stack[-1] < 0:
                        stack.append(a)
                        break
            # while문에서 break 시, a를 추가했거나 a가 파괴된 상태
            # 다음 소행성으로 넘어감
    
    return stack

# Test cases
print(asteroidCollision([5, 10, -5]))  # [5, 10]
print(asteroidCollision([8, -8]))  # []
print(asteroidCollision([10, 2, -5]))  # [10]
print(asteroidCollision([-2, -1, 1, 2]))  # [-2, -1, 1, 2]