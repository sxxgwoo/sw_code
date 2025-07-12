'''
Decode String

You are given an encoded string s, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. There will not be input like 3a, 2[4], a[a] or a[2].

The test cases are generated so that the length of the output will never exceed 100,000.

Example 1:

Input: s = "2[a3[b]]c"

Output: "abbbabbbc"

Example 2:

Input: s = "axb3[z]4[c]"

Output: "axbzzzcccc"

Example 3:

Input: s = "ab2[c]3[d]1[x]"

Output: "abccdddx"
'''

# Recursion

def decodeString(s: str) -> str:
    i = 0

    def helper():
        nonlocal i # 바깥쪽 함수의 local 변수를 참조

        res = ""
        k = 0
        
        while i < len(s):
            c = s[i]
            
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                i += 1
                res += k * helper()
                k = 0
            elif c == "]":
                return res
            else:
                res += c
            
            i += 1
        return res
    
    return helper()

# One Stack
def decodeString(s: str) -> str:
    stack = []

    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s[i])
        else:
            substr = ""
            while stack[-1] != "[":
                substr = stack.pop() + substr
            stack.pop()

            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(int(k) * substr)

    return "".join(stack)

# ============================
# Test Case "2[a3[b]]c" -> "abbbabbbc"
# ============================
if __name__ == "__main__":
    res = decodeString("2[a3[b]]c")

    print(res)