# 化栈为队

# 实现一个MyQueue类，该类用两个栈来实现一个队列。

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sin = []
        self.sout = []
        self.lin = 0
        self.lout = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.sin.append(x)
        self.lin += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.lout != 0:
            t = self.sout[self.lout-1]
            self.sout.pop()
            self.lout -= 1
            return t
        while self.lin > 1:
            self.lin -= 1
            self.sout.append(self.sin[self.lin])
            self.lout += 1
            self.sin.pop()
        t = self.sin.pop()
        self.lin -= 1
        return t

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.lout == 0:
            while self.lin != 0:
                self.lin -= 1
                self.sout.append(self.sin[self.lin])
                self.lout += 1
                self.sin.pop()
        return self.sout[self.lout-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.lin + self.lout == 0


# Your MyQueue object will be instantiated and called as such:
queue = MyQueue()
queue.push(1)
queue.push(2)
queue.peek()
queue.pop()
queue.empty()


