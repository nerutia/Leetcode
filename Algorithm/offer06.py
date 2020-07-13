# 从尾到头打印链表

# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]





c = Solution()
print(c.reversePrint(head = [1,3,2]))



