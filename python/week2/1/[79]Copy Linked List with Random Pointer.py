# 138. Copy List with Random Pointer   
# https://leetcode.com/problems/copy-list-with-random-pointer/
# Problem description
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
# Return the head of the copied linked list.
# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
# val: an integer representing Node.val

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
# Solution 1: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)

def copyRandomList(head: 'Node') -> 'Node':
    """
    원본 노드를 키로, 복제 노드를 값으로 가지는 해시맵을 만들어
    next/random 포인터를 올바르게 연결하는 방법.
    """
    if not head:
        return None

    # 1) 모든 노드에 대한 복제본을 생성하여 해시맵에 저장
    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    # 2) next, random 포인터를 지정
    curr = head
    while curr:
        copy = old_to_new[curr]
        copy.next = old_to_new.get(curr.next)      # None 처리 포함
        copy.random = old_to_new.get(curr.random)
        curr = curr.next

    # 3) 복제 리스트의 헤드 반환
    return old_to_new[head]

# Solution 2: Space-Optimized Two-Pass
# Time Complexity: O(n)
# Space Complexity: O(1)

# def copyRandomList(head: 'Node') -> 'Node':
#     """
#     1) 각 원본 노드 뒤에 복제 노드를 끼워넣고,
#     2) 복제 노드의 random 포인터를 연결한 뒤,
#     3) 원본 리스트와 복제 리스트를 분리하는 공간 최적화 방법.
#     """
#     if not head:
#         return None

#     # 1) 복제 노드를 원본 노드 사이사이에 끼워넣음
#     curr = head
#     while curr:
#         nxt = curr.next
#         copy = Node(curr.val)
#         curr.next = copy
#         copy.next = nxt
#         curr = nxt

#     # 2) random 포인터 설정
#     curr = head
#     while curr:
#         if curr.random:
#             # 원본 curr.random 뒤에 있는 복제 노드를 가리키도록
#             curr.next.random = curr.random.next
#         curr = curr.next.next

#     # 3) 두 리스트(원본 / 복제)를 분리
#     orig, copy_head = head, head.next
#     while orig:
#         copy = orig.next
#         orig.next = copy.next           # 원본의 next 복원
#         orig = orig.next
#         if orig:
#             copy.next = orig.next       # 복제의 next 연결
#     return copy_head

def build_list(data):
    """
    data: [[val, random_index], ...]
    random_index가 None이면 random=None
    """
    nodes = [Node(val) for val, _ in data]
    for i, (_, r) in enumerate(data):
        nodes[i].next = nodes[i+1] if i+1 < len(nodes) else None
        nodes[i].random = nodes[r] if r is not None else None
    return nodes[0] if nodes else None

def print_list(head):
    """
    head를 [[val, random_index], ...] 형태로 출력
    """
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    out = []
    for node in nodes:
        if node.random is None:
            ri = None
        else:
            ri = nodes.index(node.random)
        out.append([node.val, ri])
    print(out)

# 예제 1
data1 = [[3, None], [7, 3], [4, 0], [5, 1]]
head1 = build_list(data1)
copy1 = copyRandomList(head1)
print("Original:", end=" ")
print_list(head1)    # 기대: [[3,None],[7,3],[4,0],[5,1]]
print("Copied:  ", end=" ")
print_list(copy1)    # 기대: [[3,None],[7,3],[4,0],[5,1]]
print()

# 예제 2
data2 = [[1, None], [2, 2], [3, 2]]
head2 = build_list(data2)
copy2 = copyRandomList(head2)
print("Original:", end=" ")
print_list(head2)    # 기대: [[1,None],[2,2],[3,2]]
print("Copied:  ", end=" ")
print_list(copy2)    # 기대: [[1,None],[2,2],[3,2]]