'''
Lemonade Change

At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

You are given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

Example 1:

Input: bills = [5,10,5,5,20]

Output: true

Explanation:
From first customer, we collect one $5 bill.
From second customer, we collect $10 bill and give back $5 bill.
From third and fourth customers, we collect two $5 bills.
From fifth customer, we collect $20 bill and give back one $10 bill and $5 bill.

Example 2:

Input: bills = [5,20,10,5]

Output: false
'''
from typing import List

# Iteration
def lemonadeChange(bills: List[int]) -> bool:
    five, ten = 0, 0
    for b in bills:
        if b == 5:
            five += 1
        elif b == 10:
            five, ten = five - 1, ten + 1
        elif ten > 0:
            five, ten = five - 1, ten - 1
        else:
            five -= 3
        if five < 0:
            return False
    return True

# SH proof
def lemonadeChange(bills: List[int]) -> bool:
    change = {5:0, 10:0, 20:0}

    for pay in bills:
        change[pay] += 1
        if(pay == 10 and change[5] == 0):
            return False
        if(pay == 10 and change[5] > 0):
            change[5] -= 1

        if(pay == 20 and change[5] == 0):
            return False

        elif(pay == 20 and change[10] > 0 and change[5] > 0):
            change[5] -= 1
            change[10] -= 1
        
        elif(pay == 20 and change[10] == 0 and change[5] >= 3):
            change[5] -= 3

        elif(pay == 20 and change[10] == 0 and change[5] < 3):
            return False

    return True

# ============================
# Test Case [5,20,10,5] -> False
# ============================
if __name__ == "__main__":
    res = lemonadeChange([5,20,10,5])
    
    print(res)