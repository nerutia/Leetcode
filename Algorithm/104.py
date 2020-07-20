# 二叉树的最大深度

# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

        """
        self.depth = 0
        def gd(root, d):
            if root:
                self.depth = max(self.depth, d)
                gd(root.left, d+1)
                gd(root.right, d+1)
        if root:
            gd(root, 1)
        return self.depth
        """



