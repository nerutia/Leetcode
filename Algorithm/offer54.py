# 二叉搜索树的第k大节点

# 给定一棵二叉搜索树，请找出其中第k大的节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.vals=[]
        def inorder(node):
            if node:
                inorder(node.left)
                self.vals.append(node.val)
                inorder(node.right)
        inorder(root)
        return self.vals[len(self.vals)-k]

        
        



