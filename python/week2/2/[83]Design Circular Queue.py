'''
Design Circular Queue
Design and implement circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language.
Example 1:

Input: ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

Output: [null, true, true, true, false, 3, true, true, true, 4]
Explanation:
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear(); // return 3
myCircularQueue.isFull(); // return True
myCircularQueue.deQueue(); // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear(); // return 4
'''
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.q) == self.k:
            return False
        self.q.append(value)
        return True

    def deQueue(self) -> bool:
        if not self.q:
            return False
        self.q.pop(0)
        return True

    def Front(self) -> int:
        if self.q:
            return self.q[0]
        return -1

    def Rear(self) -> int:
        if self.q:
            return self.q[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.k


if __name__ == "__main__":
    cmds = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
    args = [[3], [1], [2], [3], [4], [], [], [], [4], []]

    res = []
    obj = None

    for cmd, arg in zip(cmds, args):
        if cmd == "MyCircularQueue":
            obj = MyCircularQueue(*arg)
            res.append(None)  # 생성자는 null
        elif cmd == "enQueue":
            res.append(obj.enQueue(*arg))
        elif cmd == "deQueue":
            res.append(obj.deQueue())
        elif cmd == "Front":
            res.append(obj.Front())
        elif cmd == "Rear":
            res.append(obj.Rear())
        elif cmd == "isEmpty":
            res.append(obj.isEmpty())
        elif cmd == "isFull":
            res.append(obj.isFull())

    print(res)
