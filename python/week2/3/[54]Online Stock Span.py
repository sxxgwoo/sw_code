'''
Online Stock Span

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.

Example 1:

Input: ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]

Output: [null, 1, 1, 1, 2, 1, 4, 6]

Explanation:
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80); // return 1
stockSpanner.next(60); // return 1
stockSpanner.next(70); // return 2
stockSpanner.next(60); // return 1
stockSpanner.next(75); // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85); // return 6
'''

# Brute Force
class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        i = len(self.arr) - 2
        while i >= 0 and self.arr[i] <= price:
            i -= 1
        return len(self.arr) - i - 1

# Monotonic Decreasing Stack
class StockSpanner:

    def __init__(self):
        self.stack = []  # pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span

# ============================
# Test Case ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
#           [[], [100], [80], [60], [70], [60], [75], [85]] -> [null, 1, 1, 1, 2, 1, 4, 6]
# ============================
if __name__ == "__main__":
    obj = StockSpanner()
    param_1 = obj.next(100)
    param_2 = obj.next(80)
    param_3 = obj.next(60)
    param_4 = obj.next(70)
    param_5 = obj.next(60)
    param_6 = obj.next(75)
    param_7 = obj.next(85)

    print(param_1, param_2, param_3, param_4, param_5, param_6, param_7)