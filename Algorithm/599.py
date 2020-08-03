# N叉树的最大深度



# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return max([self.maxDepth(i) for i in root.children]) + 1




c = Solution()
print(c.maxDepth(nums1=[1,3],nums2=[2]))