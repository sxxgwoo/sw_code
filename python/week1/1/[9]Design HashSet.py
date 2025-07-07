# Design HashSet
# 문제 설명: 해시 테이블을 사용하여 정수 집합을 구현하는 클래스를 작성하세요.
# 해시 테이블은 정수를 저장하고 검색하는 데 사용됩니다.
# 입력: add(1), add(2), contains(1), remove(2), contains(2)
# 출력: True, False, True, False, False
# 설명: 1을 추가하고 2를 추가하고 1을 포함하는지 확인하고 2를 제거하고 2를 포함하는지 확인합니다.

class MyHashSet:
    # bucket_count: hash table의 버킷(슬롯) 수
    def __init__(self):
        self._B = 1000
        self._buckets = [[] for _ in range(self._B)]

    def _idx(self, key: int) -> None:
        return key % self._B

    def add(self, key: int) -> None:
        b = self._buckets[self._idx(key)]
        # 이미 있으면 추가 안 함
        for x in b:
            if x == key:
                return
        b.append(key)

    def remove(self, key: int) -> None:
        b = self._buckets[self._idx(key)]
        for i, x in enumerate(b):
            if x == key:
                b.pop(i)
                return

    def contains(self, key: int) -> bool:
        b = self._buckets[self._idx(key)]
        for x in b:
            if x == key:
                return True
        return False

# test case
myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1)) # True
print(myHashSet.contains(3)) # False
myHashSet.add(2)
print(myHashSet.contains(2)) # True
myHashSet.remove(2)
print(myHashSet.contains(2)) # False