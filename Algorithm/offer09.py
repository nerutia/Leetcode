# 用两个栈实现队列

# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead,
# 分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

class CQueue:

    def __init__(self):
        self.append_stack = []
        self.delete_stack = []


    def appendTail(self, value: int) -> None:
        self.append_stack.append(value)


    def deleteHead(self) -> int:
        if len(self.delete_stack) == 0:
            if len(self.append_stack) == 0:
                return -1
            else:
                while len(self.append_stack) > 0:
                    tmp_val = self.append_stack.pop()
                    self.delete_stack.append(tmp_val)
                return self.delete_stack.pop()
        return self.delete_stack.pop()



# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(value)
param_2 = obj.deleteHead()


