'''
Valid Palindrome II
You are given a string s, return true if the s can be a palindrome after deleting at most one character from it.

A palindrome is a string that reads the same forward and backward.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "aca"

Output: true
Explanation: "aca" is already a palindrome.

Example 2:

Input: s = "abbadc"

Output: false
Explanation: "abbadc" is not a palindrome and can't be made a palindrome after deleting at most one character.

Example 3:

Input: s = "abbda"

Output: true
Explanation: "We can delete the character 'd'.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        cnt=0
        t=0
        print(len(s))
        while l<r and cnt<=1:
            
            if s[l] != s[r]:
                print(f'{l}, 안녕{s[l]}')
                print(f'{r}, 안녕{s[r]}')
                
                cnt+=1
                if s[l+1] == s[r]:
                    l+=1
                elif s[l] == s[r-1]:
                    r-=1
            else:
                t+=1
                print(t)
                l+=1
                r-=1
            # print(cnt)
  
        return (cnt<=1)

if __name__ == "__main__":
    sol = Solution()
    s="aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    print(sol.validPalindrome(s))
