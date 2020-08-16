# 二叉搜索树的最近公共祖先

# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 本题与offer68-2相同

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        l, r = self.lowestCommonAncestor(root.left,p,q), self.lowestCommonAncestor(root.right,p,q)
        if l and r:
            return root
        if l:
            return l
        return r