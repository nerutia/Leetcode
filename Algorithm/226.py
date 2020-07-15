# 翻转二叉树

# 翻转一棵二叉树。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        t = root.left
        root.left = root.right
        root.right = t
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

