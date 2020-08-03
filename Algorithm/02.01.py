# 移除重复节点

# 编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head == None:
            return
        s = set([head.val])
        t = head
        while t.next:
            if t.next.val in s:
                t.next = t.next.next
                continue
            s.add(t.next.val)
            t = t.next
        return head



c = Solution()
print(c.removeDuplicateNodes([1, 2, 3, 3, 2, 1]))