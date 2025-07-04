'''
Merge Strings Alternately
You are given two strings, word1 and word2. Construct a new string by merging them in alternating order, starting with word1 — take one character from word1, then one from word2, and repeat this process.

If one string is longer than the other, append the remaining characters from the longer string to the end of the merged result.

Return the final merged string.

Example 1:

Input: word1 = "abc", word2 = "xyz"

Output: "axbycz"
Example 2:

Input: word1 = "ab", word2 = "abbxxc"

Output: "aabbbxxc"
==================================================
"".join(res) 의 뜻
python
복사
편집
"구분자".join(리스트/튜플/문자열 등 이터러블)
"".join(res)은 리스트 res의 모든 요소를 빈 문자열("")로 이어붙인다는 뜻입니다.

res 안에는 반드시 문자열(str) 요소들만 있어야 합니다.

예시 1: 가장 기본적인 쓰임
python
복사
편집
res = ['h', 'e', 'l', 'l', 'o']
joined = "".join(res)
print(joined)  # 출력: 'hello'
예시 2: 구분자 있는 버전
python
복사
편집
words = ['apple', 'banana', 'orange']
sentence = ", ".join(words)
print(sentence)  # 출력: 'apple, banana, orange'
'''

class Solution:
    
    # 1) ** Two Pointers - I
    # 두 문자열 word1, word2를 번갈아가며 병합하는 함수
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0                # 두 문자열의 인덱스 포인터 초기화
        res = []                   # 결과를 담을 리스트

        # 두 문자열 모두 끝나지 않았을 동안 반복
        while i < len(word1) and j < len(word2):
            res.append(word1[i])   # word1에서 한 글자 추가
            res.append(word2[j])   # word2에서 한 글자 추가
            i += 1
            j += 1

        # 남은 부분 처리 (한쪽이 더 길 경우)
        res.append(word1[i:])      # word1이 남았다면 전부 추가
        res.append(word2[j:])      # word2가 남았다면 전부 추가

        # 리스트를 문자열로 합쳐서 반환
        return "".join(res)

    
    # 2) sw solution
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lw1,lw2 = len(word1), len(word2)
        maxl=max(lw1,lw2)
        s=""
        for i in range(maxl):
            if lw1>lw2:
                if i > lw2-1:
                    s+=word1[i]
                    continue
                    s+=word2[i]
                else:
                    s+=word1[i]
                    s+=word2[i]
            else:
                if i > lw1-1:
                    s+=word2[i]
                    continue
                    s+=word1[i]
                else:
                    s+=word1[i]
                    s+=word2[i]
        return s
    
    
        
        
        
if __name__ == "__main__":
    sol = Solution()
    # word1 = "abc"
    # word2 = "xyz"
    
    word1 = "ab"
    word2 = "abbxxc"
    print(sol.mergeAlternately(word1,word2))