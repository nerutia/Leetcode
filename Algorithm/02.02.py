# 返回倒数第 k 个节点

# 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        a = head
        b = head
        while k > 0:
            a = a.next
        while a != None:
            a = a.next
            b = b.next
        return b.val

# c = Solution()
# print(c.kthToLast(nums =  [-10,-3,0,5,9]))
