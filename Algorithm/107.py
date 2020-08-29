# 二叉树的层次遍历 II

# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        r = []
        st = [root]
        while len(st) > 0:
            t = []
            v = []
            while len(st) > 0:
                m = st.pop(0)
                v.append(m.val)
                if m.left:
                    t.append(m.left)
                if m.right:
                    t.append(m.right)
            r.append(v)
            st = t
        return r[::-1]




