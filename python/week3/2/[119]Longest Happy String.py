'''
Longest Happy String
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
if __name__=="__main__":
    sol = Solution()
    