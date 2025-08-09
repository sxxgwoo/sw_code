'''
Course Schedule II
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 3, prerequisites = [[1,0]]

Output: [0,1,2]
Explanation: We must ensure that course 0 is taken before course 1.

Example 2:

Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

Output: []
Explanation: It's impossible to finish all courses.
'''
class Solution:
    #1. Cycle Detection (DFS)
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # 각 과목별로 "선수 과목 리스트"를 저장하는 그래프 생성
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        output = []       # 최종 수강 순서 (위상 정렬 결과)
        visit, cycle = set(), set()
        # visit: 이미 처리 완료된 과목(DFS 탐색 끝난 노드)
        # cycle: 현재 DFS 경로에 있는 과목(사이클 감지용)

        def dfs(crs):
            # 현재 DFS 경로에 같은 과목이 다시 나타나면 → 사이클 존재
            if crs in cycle:
                return False
            # 이미 처리 완료된 과목이면 다시 볼 필요 없음
            if crs in visit:
                return True

            # 현재 과목을 경로에 추가(사이클 체크용)
            cycle.add(crs)
            # 선수 과목들 먼저 탐색
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            # 경로에서 제거 (다른 경로 탐색할 때 영향 안 주도록)
            cycle.remove(crs)
            # 처리 완료 표시
            visit.add(crs)
            # 선수 과목을 먼저 넣었으므로, 현재 과목은 나중에 추가
            output.append(crs)
            return True

        # 모든 과목에 대해 DFS 실행
        for c in range(numCourses):
            if dfs(c) == False:  # 사이클 발견 시 빈 배열 반환
                return []

        return output  # DFS 후 결과 리스트 반환

    #2. Topological Sort (DFS)
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # 인접 리스트(adj): 각 과목에서 갈 수 있는 다음 과목 목록 저장
        adj = [[] for i in range(numCourses)]
        # 진입 차수(indegree): 각 과목으로 들어오는 간선(필요한 선수과목 수) 개수
        indegree = [0] * numCourses

        # 그래프 구성
        for nxt, pre in prerequisites:
            indegree[nxt] += 1       # nxt 과목의 진입 차수 +1
            adj[pre].append(nxt)     # pre 과목에서 nxt 과목으로 간선 추가

        output = []  # 수강 순서 저장 리스트

        # DFS 함수: 현재 node를 수강한 후 다음 과목들 탐색
        def dfs(node):
            output.append(node)      # 현재 과목 수강 순서에 추가
            indegree[node] -= 1      # 방문 처리(진입 차수 감소)
            for nei in adj[node]:    # 현재 과목을 선수로 하는 다음 과목들 확인
                indegree[nei] -= 1   # 해당 과목의 진입 차수 1 감소
                if indegree[nei] == 0:  # 더 이상 선수과목이 없으면 바로 수강 가능
                    dfs(nei)         # 재귀적으로 다음 과목 탐색

        # 진입 차수가 0인 과목부터 시작
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        # 모든 과목을 수강했으면 output 반환, 아니면 [] 반환(사이클 존재)
        return output if len(output) == numCourses else []



if __name__=="__main__":
    sol = Solution()
    numCourses = 3
    # prerequisites = [[1,0]]
    prerequisites = [[0,1],[1,2],[2,0]]

    print(sol.findOrder(numCourses,prerequisites))