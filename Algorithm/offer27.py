# 二叉树的镜像

# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        self.rotateTree(root)
        return root

    def rotateTree(self, root: TreeNode):
        if root == None:
            return
        t = root.left
        root.left = root.right
        root.right = t
        self.rotateTree(root.left)
        self.rotateTree(root.right)




