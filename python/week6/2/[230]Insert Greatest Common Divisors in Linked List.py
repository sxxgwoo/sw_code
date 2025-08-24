'''
Insert Greatest Common Divisors in Linked List
You are given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the head of the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

Example 1:

Input: head = [12,3,4,6]

Output: [12,3,3,1,4,2,6]
Example 2:

Input: head = [2,1]

Output: [2,1,1]
'''
if __name__ == "__main__":
    sol = Solution()