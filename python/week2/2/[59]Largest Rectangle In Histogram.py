'''
Largest Rectangle In Histogram
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:

Input: heights = [7,1,7,2,2,4]

Output: 8
Example 2:

Input: heights = [1,3,7]

Output: 7
'''
class Solution:
    # 1) Brute Force
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)       # 전체 막대의 수
        maxArea = 0            # 가장 큰 직사각형 넓이를 저장할 변수

        for i in range(n):
            height = heights[i]  # 현재 막대의 높이를 기준으로 함
                
            # 오른쪽으로 확장 가능한 가장 먼 인덱스를 찾음
            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= height:
                rightMost += 1

            # 왼쪽으로 확장 가능한 가장 먼 인덱스를 찾음
            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1

            # 실제 사용할 인덱스로 조정 (루프에서 한 칸 더 간 상태이므로 보정)
            rightMost -= 1
            leftMost += 1

            # 넓이 계산: (오른쪽 - 왼쪽 + 1) * 높이
            width = rightMost - leftMost + 1
            area = height * width

            # 최대 넓이 갱신
            maxArea = max(maxArea, area)

        return maxArea  
    
    # 2) stack
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        maxArea = 0          # 최대 직사각형 넓이를 저장할 변수
        stack = []           # 인덱스를 저장하는 스택

        # 모든 막대를 순회 (마지막 막대 뒤에도 한번 더 순회)
        for i in range(n + 1):
            # 현재 막대의 높이가 스택의 top에 있는 막대보다 작거나 같을 때
            # 또는 마지막까지 도달했을 때
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]  # 스택에서 하나 꺼내 해당 높이로 직사각형 계산
                # 스택이 비었다면 왼쪽으로는 모두 포함 가능하므로 너비는 i
                # 그렇지 않으면 이전 인덱스 다음부터 현재 인덱스 전까지가 너비
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)  # 넓이 갱신
            stack.append(i)  # 현재 인덱스를 스택에 추가
        
        return maxArea
    
if __name__=="__main__":
    sol = Solution()
    heights = [7,1,7,2,2,4]
    print(sol.largestRectangleArea(heights))