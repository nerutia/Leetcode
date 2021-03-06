# 二叉搜索树中的搜索

# 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        h = root
        while h:
            if h.val == val:
                return h
            if h.val < val:
                h = h.right
            elif h.val > val:
                h = h.left
        return None


