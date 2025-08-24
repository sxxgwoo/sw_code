'''
Hand of Straights
You are given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize.

You want to rearrange the cards into groups so that each group is of size groupSize, and card values are consecutively increasing by 1.

Return true if it's possible to rearrange the cards in this way, otherwise, return false.

Example 1:

Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4

Output: true
Explanation: The cards can be rearranged as [1,2,3,4] and [2,3,4,5].

Example 2:

Input: hand = [1,2,3,3,4,5,6,7], groupSize = 4

Output: false
Explanation: The closest we can get is [1,2,3,4] and [3,5,6,7], but the cards in the second group are not consecutive.
'''
from collections import Counter
def merge(left, right):
    result = []
    i = j = 0

    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def msort(arr):
    if(len(arr) <= 1):
        return arr

    mid = len(arr) // 2
    left = msort(arr[:mid])
    right = msort(arr[mid:])

    return merge(left, right)

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # hand.sort()
        msort(hand)
        while hand:
            try:
                base = hand[0]
                for i in range(groupSize):
                    hand.remove(base+i)
            except:
                return False
        return True


    # 2) Sorting + Counter
    # 아이디어:
    # - hand를 정렬한 뒤, 가장 작은 수부터 시작해서
    #   [num, num+1, ..., num+groupSize-1] 연속 구간을 하나의 그룹으로 만든다.
    # - Counter로 각 숫자의 남은 개수를 관리하며, 필요한 만큼 차감한다.
    # - 어떤 단계에서든 필요한 카드가 부족하면 False.
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # 전체 카드 수가 groupSize로 나누어 떨어지지 않으면 불가능
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)   # 각 숫자의 개수
        # hand.sort()             # 작은 수부터 차례로 그룹을 만들기 위해 정렬
        msort(hand)
        # 정렬된 순서대로 확인
        for num in hand:
            # 이미 이전에 다른 그룹을 만들면서 모두 소진됐다면 스킵
            if count[num] == 0:
                continue

            # num을 시작으로 연속된 groupSize개의 수를 하나의 그룹으로 만든다.
            # 각 숫자가 최소 1개 이상 남아 있어야 한다.
            for x in range(num, num + groupSize):
                if count[x] == 0:        # 필요한 숫자가 없으면 실패
                    return False
                count[x] -= 1            # 해당 숫자 1장 사용

        # 모든 그룹을 성공적으로 만들었다면 True
        return True
if __name__ == "__main__":
    sol = Solution()
    hand = [1,2,4,2,3,5,3,4]
    groupSize = 4
    print(sol.isNStraightHand(hand,groupSize))