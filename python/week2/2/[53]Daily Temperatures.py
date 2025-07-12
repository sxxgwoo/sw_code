'''
Daily Temperatures
주어진 매일의 온도 리스트에서, 각 날마다 이후 며칠 후에 더 따뜻한 날이 오는지를 구하는 문제
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
'''

class Solution:

    # 1) sw solution Brute Force
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res =[]
        warm = 0
        step = 0
        for i in range(len(temperatures)-1):
            for j in range(i+1,len(temperatures)):
                if temperatures[i]<temperatures[j]:
                    warm+=1
                    break
                step+=1
            if warm == 0:
                res.append(0)
            else:
                res.append(step+warm)
            warm = 0
            step = 0
        res.append(0)
        return res
    
    # 2) Stack
    # 2) Stack
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # 결과 리스트를 0으로 초기화 (모든 날에 대해 기본값은 0)
        res = [0] * len(temperatures)
        
        # 스택을 사용해 (temperature, index) 쌍을 저장
        # 스택은 "내려가는 순서"로 유지됨
        stack = []

        for i, t in enumerate(temperatures):
            # 현재 온도가 스택의 top에 있는 온도보다 높다면,
            # 더 따뜻한 날을 찾은 것이므로 스택을 pop하면서 결과를 기록
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                # 현재 인덱스 i에서 이전 인덱스를 빼면, 기다린 일 수가 됨
                res[stackInd] = i - stackInd
            # 현재 (온도, 인덱스)를 스택에 추가
            stack.append((t, i))
        
        # 스택에 남아 있는 인덱스들은 끝까지 더 따뜻한 날이 없었던 경우이므로 0으로 유지됨
        return res

if __name__=="__main__":
    sol = Solution()
    temperatures = [30,38,30,36,35,40,28]
    print(sol.dailyTemperatures(temperatures))