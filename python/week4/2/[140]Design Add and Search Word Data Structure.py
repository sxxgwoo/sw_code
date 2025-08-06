'''
Design Add and Search Word Data Structure
Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
Example 1:

Input:
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]

Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true

ex) 트라이 자료구조
Trie == prefix tree
(root)
 ├─ c
 │   └─ a (word=True)  ← ★ ca 삽입으로 여기서 단어 종료 표시
 │       ├─ r (word=True)
 │       └─ t (word=True)
 └─ d
     └─ o
         └─ g (word=True)
'''
# 1) Brute Force
class WordDictionary:

    def __init__(self):
        self.store = []

    def addWord(self, word: str) -> None:
        self.store.append(word)

    def search(self, word: str) -> bool:
        for w in self.store:
            if len(w) != len(word):
                continue
            i = 0
            while i < len(w):
                if w[i] == word[i] or word[i] == '.':
                    i += 1
                else:
                    break
            if i == len(w):
                return True
        return False

# 2) DFS(Trie)
# '.'를 포함한 단어 검색 문제 (Word Dictionary)
# - addWord(word): 단어를 사전에 추가
# - search(word): 단어를 검색, '.'은 어떤 문자와도 매칭 가능

class TrieNode:
    def __init__(self):
        self.children = {}  # 각 노드가 가질 수 있는 다음 글자(자식)들을 딕셔너리로 저장
        self.word = False   # 이 노드에서 단어가 끝나는지 여부 표시

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # 루트 노드 초기화

    def addWord(self, word: str) -> None:
        cur = self.root
        # 단어의 각 글자를 순서대로 Trie에 삽입
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()  # 새로운 글자면 새로운 노드 생성
            cur = cur.children[c]             # 다음 노드로 이동
        cur.word = True                       # 단어 끝 표시

    def search(self, word: str) -> bool:
        # DFS를 이용해 검색
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                # 1) '.'인 경우: 현재 노드의 모든 자식에 대해 탐색
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):  # 하나라도 매칭되면 True
                            return True
                    return False  # 어떤 자식에서도 매칭 안되면 False
                else:
                    # 2) 일반 알파벳인 경우
                    if c not in cur.children:  # 해당 글자가 없으면 실패
                        return False
                    cur = cur.children[c]      # 다음 노드로 이동
            
            # 반복문을 다 돌았다면, 현재 노드가 단어의 끝인지 확인
            return cur.word

        # 루트에서 시작
        return dfs(0, self.root)

if __name__=="__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("day")
    wordDictionary.addWord("bay")
    wordDictionary.addWord("may")

    print(wordDictionary.search("say"))
    print(wordDictionary.search("day"))
    print(wordDictionary.search(".ay"))
    print(wordDictionary.search("b.."))
        
