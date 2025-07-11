'''
Guess Number Higher Or Lower
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

0: your guess is equal to the number I picked (i.e. num == pick).
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
Return the number that I picked.

Example 1:

Input: n = 5, pick = 3

Output: 3
Example 2:

Input: n = 15, pick = 10

Output: 10
Example 3:

Input: n = 1, pick = 1

Output: 1
'''