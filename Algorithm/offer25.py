# 合并两个排序的链表

# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
        



