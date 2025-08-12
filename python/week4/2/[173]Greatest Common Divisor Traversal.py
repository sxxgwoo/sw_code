'''
Greatest Common Divisor Traversal
You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.

Example 1:

Input: nums = [4,3,12]

Output: true
Explanation: There exists three possible pairsof indices. For each pair, the sequence of traversals are:

(0,1) -> [0,2,1]
(0,2) -> [0,2]
(1,2) -> [1,2]

Example 2:

Input: nums = [2,3,7]

Output: false
'''
class UnionFind:
    def __init__(self, n):
        self.n = n                              # 현재 남아있는 그룹(집합)의 개수
        self.Parent = list(range(n + 1))        # 부모 노드(자기 자신으로 초기화)
        self.Size = [1] * (n + 1)               # 각 집합의 크기(Union 시 큰 쪽에 합침)

    def find(self, node):
        """경로 압축을 이용해 루트 부모 찾기"""
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        """두 노드를 같은 집합으로 합치기"""
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:  # 이미 같은 집합이면 합칠 필요 없음
            return False
        self.n -= 1   # 집합 개수 감소
        # 항상 더 큰 집합 쪽이 부모가 되도록 설정 (Union by Size)
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

    def isConnected(self):
        """전체가 하나의 집합이면 True"""
        return self.n == 1

class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        uf = UnionFind(len(nums))  # nums 길이만큼의 노드로 Union-Find 초기화

        factor_index = {}  # 소인수 f → 해당 소인수를 가진 첫 번째 index 매핑
        for i, n in enumerate(nums):
            f = 2
            # n의 소인수를 하나씩 찾으면서 처리
            while f * f <= n:
                if n % f == 0:  # f가 소인수라면
                    if f in factor_index:
                        # 같은 소인수를 가진 이전 index와 현재 index를 Union
                        uf.union(i, factor_index[f])
                    else:
                        # 처음 나온 소인수면 현재 index 저장
                        factor_index[f] = i
                    # 같은 소인수로 더 나눠지지 않을 때까지 나누기
                    while n % f == 0:
                        n = n // f
                f += 1
            # 마지막에 남은 n이 1보다 크면(즉, 소인수) 처리
            if n > 1:
                if n in factor_index:
                    uf.union(i, factor_index[n])
                else:
                    factor_index[n] = i

        # 모든 노드가 연결되어 있으면 True
        return uf.isConnected()

    
if __name__=="__main__":
    sol = Solution()
    nums = [4,3,12]
    print(sol.canTraverseAllPairs(nums))