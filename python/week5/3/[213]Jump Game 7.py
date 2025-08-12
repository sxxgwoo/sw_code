'''
Jump Game VII

You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

Example 1:

Input: s = "00110010", minJump = 2, maxJump = 4

Output: true

Explanation: The order of jumps is: indices 0 -> 4 -> 7.

Example 2:

Input: s = "0010", minJump = 1, maxJump = 1

Output: false
'''
# Dynamic Programming (Bottom-Up) : SH proof
def canReach(s: str, minJump: int, maxJump: int) -> bool:
    n = len(s)
    dp = [False] * n # dp 배열을 만들어서 각 인덱스에서 n-1까지 도달 가능한지 여부를 저장

    if(s[-1] == "1"):
        return False

    dp[-1] = True
    
    for i in range(n-1,-1,-1):
        if(s[i] == "1"):
            continue

        if(i + minJump > n-1):
            continue

        for j in range(i + minJump, min(i + maxJump + 1, n)):
            if(dp[j] == True):
                dp[i] = True
                break
    
    return dp[0]

# Dynamic Programming (Sliding Window)
def canReach(s: str, minJump: int, maxJump: int) -> bool:
    n = len(s)
    
    if s[n - 1] == '1':
        return False

    dp = [False] * n # dp 배열을 만들어서 각 인덱스가 0에서 부터 도달 가능한지 여부를 저장
    dp[0] = True
    
    cnt = 0 # cnt는 현재 범위 내에서 True가 된 dp의 개수를 추적하는 변수

    # 1부터 n-1까지 반복하며 각 위치가 도달 가능한지 판단
    for i in range(1, n): 
        # 현재 위치 i에서 minJump 이상 떨어진 곳에서 dp가 True라면, 현재 위치로 올 수 있음
        # i - minJump는 최소 점프 거리만큼 떨어진 위치
        if i >= minJump and dp[i - minJump]:
            cnt += 1  # 해당 범위 내에 True가 된 dp가 있으므로 cnt를 1 증가시킴
        
        # 현재 위치 i가 maxJump를 넘어설 때, dp[i - maxJump - 1]이 True라면 범위를 벗어났으므로 cnt를 1 감소
        if i > maxJump and dp[i - maxJump - 1]:
            cnt -= 1
        
        # cnt가 0보다 크면 현재 위치 i는 도달 가능하고, 해당 위치가 장애물이 아니라면 dp[i]를 True로 설정
        if cnt > 0 and s[i] == '0':
            dp[i] = True  # 해당 위치에 도달할 수 있음을 dp[i]로 기록

    return dp[n - 1]

# ============================
# Test Case "00110010", 2, 4 -> True
# ============================
if __name__ == "__main__":
    res = canReach("00110010", 2, 4 )
    
    print(res)

