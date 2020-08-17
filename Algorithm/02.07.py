# 链表相交

# 给定两个（单向）链表，判定它们是否相交并返回交点。请注意相交的定义基于节点的引用，而不是基于节点的值。
# 换句话说，如果一个链表的第k个节点与另一个链表的第j个节点是同一节点（引用完全相同），则这两个链表相交。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        la, lb = 0, 0
        t = headA
        while t:
            la += 1
            t = t.next
        t = headB
        while t:
            lb += 1
            t = t.next
        ta = headA
        tb = headB
        while la > lb:
            la -= 1
            ta = ta.next
        while lb > la:
            lb -= 1
            tb = tb.next
        while ta != tb:
            ta = ta.next
            tb = tb.next
        return ta
