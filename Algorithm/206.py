# 反转链表

# 反转一个单链表。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode, last = None) -> ListNode:
        # 输入为空
        if not head:
            return None
        # 当前为末位节点
        if not head.next:
            head.next = last
            return head
        # 其他情况
        t = head.next
        head.next = last
        return self.reverseList(t, head)

        

