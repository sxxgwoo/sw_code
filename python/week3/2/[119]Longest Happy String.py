'''
Longest Happy String
a, b, c 개수만큼 각각 a, b, c 문자를 사용할 수 있을 때,
	•	연속해서 같은 문자가 3번 나오지 않도록
	•	가능한 가장 긴 문자열(해피 스트링, happy string)을 만들어라.
	•	여러 답이 있으면 아무거나 반환해도 된다.

#Heap Properties #Push and Pop #Heapify
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
You are given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: a = 3, b = 4, c = 2

Output: "bababcabc"
Example 2:

Input: a = 0, b = 1, c = 5

Output: "ccbcc"
'''
class MaxHeap:
    def __init__(self):
        self.data = []  # 내부 배열을 사용하여 힙 저장

    def push(self, val):
        # 새로운 값을 마지막에 추가 후 위로 올리면서 최대 힙 유지
        self.data.append(val)
        self._sift_up(len(self.data) - 1)

    def pop(self):
        # 비어 있으면 None 반환
        if not self.data:
            return None
        # 루트(최대값)와 마지막 값 교환 후 pop
        self._swap(0, len(self.data) - 1)
        val = self.data.pop()  # 원래 루트
        self._sift_down(0)  # 루트부터 아래로 내려서 최대 힙 유지
        return val

    def _sift_up(self, idx):
        # 부모보다 값이 크면 위로 올리기
        parent = (idx - 1) // 2
        # 첫 번째 원소까지 거슬러 올라가며 힙 조건 만족할 때까지 반복
        while idx > 0 and self.data[idx][0] > self.data[parent][0]:
            self._swap(idx, parent)
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        # 자식 노드들과 비교하며 아래로 내려가기
        n = len(self.data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx

            # 왼쪽 자식이 존재하고 현재보다 크면 largest 갱신
            if left < n and self.data[left][0] > self.data[largest][0]:
                largest = left
            # 오른쪽 자식도 비교해서 더 큰 쪽을 largest로
            if right < n and self.data[right][0] > self.data[largest][0]:
                largest = right

            # 자식보다 크면 멈춤
            if largest == idx:
                break

            # 현재 값과 더 큰 자식 값 교환
            self._swap(idx, largest)
            idx = largest

    def _swap(self, i, j):
        # 내부 배열에서 두 인덱스 값 교환
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def __bool__(self):
        # 힙이 비어 있는지 여부 반환
        return bool(self.data)

    def __len__(self):
        return len(self.data)


class Solution:
    # 1) Greedy (Max-Heap) 방법
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        최대 힙을 이용한 탐욕적(greedy) 알고리즘
        1. 가장 많이 남은 문자를 우선 사용
        2. 연속 3회 같은 문자가 되지 않도록 두 번째로 많은 문자 사용
        """
        res = ""
        maxHeap = MaxHeap()

        # (남은 개수, 문자) 형태로 힙에 삽입
        for count, char in [(a, "a"), (b, "b"), (c, "c")]:
            if count > 0:
                maxHeap.push((count, char))

        while maxHeap:
            count, char = maxHeap.pop()  # 가장 많이 남은 문자 꺼냄

            # 마지막 두 글자가 동일하면 다른 문자를 사용해야 함
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:  # 다른 문자가 없으면 종료
                    break
                count2, char2 = maxHeap.pop()  # 두 번째로 많은 문자 사용
                res += char2
                count2 -= 1  # 하나 사용했으므로 감소
                if count2 > 0:
                    maxHeap.push((count2, char2))
                # 꺼냈던 첫 번째 문자 다시 넣기
                maxHeap.push((count, char))
            else:
                # 연속 3회가 아니면 바로 사용
                res += char
                count -= 1
                if count > 0:
                    maxHeap.push((count, char))

        return res
    
    # 2) Greedy (Recursion) 방법
    def longestDiverseStringRecursive(self, a: int, b: int, c: int) -> str:
        """
        재귀적인 탐욕 알고리즘
        - 항상 가장 개수가 많은 문자를 먼저 배치
        - 연속 3회가 안 되도록 2번째 문자를 1개만 사용
        """
        def rec(max1, max2, max3, char1, char2, char3):
            # 개수 순으로 내림차순 정렬 (max1 >= max2 >= max3 보장)
            if max1 < max2:
                return rec(max2, max1, max3, char2, char1, char3)
            if max2 < max3:
                return rec(max1, max3, max2, char1, char3, char2)
            
            # 두 번째 문자가 없으면 첫 번째 문자만 2개까지
            if max2 == 0:
                return [char1] * min(2, max1)

            # 첫 번째 문자는 최대 2개, 두 번째 문자는 필요시 1개
            use1 = min(2, max1)
            use2 = 1 if max1 - use1 >= max2 else 0

            res = [char1] * use1 + [char2] * use2

            # 남은 개수로 재귀 호출
            return res + rec(max1 - use1, max2 - use2, max3, char1, char2, char3)

        return ''.join(rec(a, b, c, 'a', 'b', 'c'))

# import heapq
# class Solution:
#     # 1) Greedy (Max-Heap) 방법
#     def longestDiverseString(self, a: int, b: int, c: int) -> str:
#         res = ""
#         maxHeap = []
#         # 음수로 넣어서 max heap처럼 사용
#         for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
#             if count != 0:
#                 heapq.heappush(maxHeap, (count, char))

#         while maxHeap:
#             count, char = heapq.heappop(maxHeap)
#             # 마지막 두 글자와 같으면 다른 문자 먼저 써야 함
#             if len(res) > 1 and res[-1] == res[-2] == char:
#                 if not maxHeap:
#                     break
#                 count2, char2 = heapq.heappop(maxHeap)
#                 res += char2
#                 count2 += 1  # 사용했으니 개수 감소 (음수라서 +1)
#                 if count2:
#                     heapq.heappush(maxHeap, (count2, char2))
#                 heapq.heappush(maxHeap, (count, char))
#             else:
#                 res += char
#                 count += 1
#                 if count:
#                     heapq.heappush(maxHeap, (count, char))

#         return res

    

if __name__ == "__main__":
    sol = Solution()

    a,b,c=3,4,2
    print(sol.longestDiverseString(a, b, c)) 
    
    a,b,c=0,1,5
    print(sol.longestDiverseString(a, b, c)) 

