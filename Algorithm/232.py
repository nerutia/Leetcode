#  用栈实现队列

#  使用栈实现队列的下列操作：

# push(x) -- 将一个元素放入队列的尾部。
# pop() -- 从队列首部移除元素。
# peek() -- 返回队列首部的元素。
# empty() -- 返回队列是否为空。


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.front = []
        self.end = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if len(self.end) != 0 or len(self.front) == 0:
            return self.end.append(x)
        while len(self.front) > 0:
            self.end.append(self.front.pop())
        self.end.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.front) != 0:
            return self.front.pop()
        while len(self.end) > 1:
            self.front.append(self.end.pop())
        return self.end.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        t = self.pop()
        self.front.append(t)
        return t


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.front) == 0 and len(self.end) == 0



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
param_2 = obj.pop()
# param_3 = obj.peek()
param_4 = obj.empty()

print(param_2)
print(param_4)
