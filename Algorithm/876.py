# 链表的中间结点

# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        front, end = head, head
        while end.next:
            front = front.next
            end = end.next
            if end.next:
                end = end.next
            else:
                return head.next
        return head


