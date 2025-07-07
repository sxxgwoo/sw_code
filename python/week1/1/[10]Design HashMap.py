# Design HashMap
# 문제 설명: 해시 테이블을 사용하여 정수 키와 정수 값을 저장하고 검색하는 클래스를 작성하세요.
# 해시 테이블은 정수 키와 정수 값을 저장하고 검색하는 데 사용됩니다.
# 입력: put(1, 1), put(2, 2), get(1), get(3), put(2, 1), get(2)
# 출력: 1, -1, 1, -1, 1
# 설명: 1을 키로 1을 값으로 저장하고 2를 키로 2를 값으로 저장하고 1을 키로 검색하고 3을 키로 검색하고 2를 키로 1을 값으로 저장하고 2를 키로 검색합니다.

class MyHashMap:

    def __init__(self):
        # 버킷 개수(B)는 적절히 조절 가능합니다.
        self._B = 1000
        # 각 버킷은 (key, value) 튜플을 담는 리스트
        self._buckets = [[] for _ in range(self._B)]

    def _idx(self, key: int) -> int:
        # 간단한 해시 함수: modulo
        return key % self._B

    def put(self, key: int, value: int) -> None:
        """
        key가 이미 존재하면 value를 갱신하고,
        없으면 새 (key, value) 쌍을 추가합니다.
        """
        b = self._buckets[self._idx(key)]
        for i, (k, v) in enumerate(b):
            if k == key:
                b[i] = (key, value)
                return
        b.append((key, value))

    def get(self, key: int) -> int:
        """
        key가 존재하면 해당 value를, 없으면 -1을 반환합니다.
        """
        b = self._buckets[self._idx(key)]
        for k, v in b:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        key가 존재하면 해당 (key, value) 쌍을 삭제합니다.
        """
        b = self._buckets[self._idx(key)]
        for i, (k, v) in enumerate(b):
            if k == key:
                b.pop(i)
                return

# test case
myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
print(myHashMap.get(1)) # 1
print(myHashMap.get(3)) # -1
myHashMap.put(2, 1)
print(myHashMap.get(2)) # 1
myHashMap.remove(2)
print(myHashMap.get(2)) # -1