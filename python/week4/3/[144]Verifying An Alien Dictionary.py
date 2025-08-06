'''
Verifying An Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabets, return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:

Input: words = ["dag","disk","dog"], order = "hlabcdefgijkmnopqrstuvwxyz"

Output: true

Explanation: The first character of the strings are same ('d'). 'a', 'i', 'o' follows the given ordering, which makes the given strings follow the sorted lexicographical order.

Example 2:

Input: words = ["neetcode","neet"], order = "worldabcefghijkmnpqstuvxyz"

Output: false

Explanation: The first 4 characters of both the strings match. But size of "neet" is less than that of "neetcode", so "neet" should come before "neetcode".
'''
from typing import List

# Comparing adjacent words
def isAlienSorted(words: List[str], order: str) -> bool:
    order_index = {c: i for i, c in enumerate(order)}
    
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        
        for j in range(len(w1)):
            if j == len(w2):
                return False
            
            if w1[j] != w2[j]:
                if order_index[w1[j]] > order_index[w2[j]]:
                    return False
                break
    return True

# ============================
# Test Case ["dag","disk","dog"], "hlabcdefgijkmnopqrstuvwxyz" -> true
# ============================
if __name__ == "__main__":
    res = isAlienSorted(["dag","disk","dog"], "hlabcdefgijkmnopqrstuvwxyz")
    
    print(res)