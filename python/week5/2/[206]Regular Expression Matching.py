'''
Regular Expression Matching
You are given an input string s consisting of lowercase english letters, and a pattern p consisting of lowercase english letters, as well as '.', and '*' characters.

Return true if the pattern matches the entire input string, otherwise return false.

'.' Matches any single character
'*' Matches zero or more of the preceding element.
Example 1:

Input: s = "aa", p = ".b"

Output: false
Explanation: Regardless of which character we choose for the '.' in the pattern, we cannot match the second character in the input string.

Example 2:

Input: s = "nnn", p = "n*"

Output: true
Explanation: '*' means zero or more of the preceding element, 'n'. We choose 'n' to repeat three times.

Example 3:

Input: s = "xyz", p = ".*z"

Output: true
Explanation: The pattern ".*" means zero or more of any character, so we choose ".." to match "xy" and "z" to match "z".
'''
if __name__ == "__main__":
    sol = Solution()