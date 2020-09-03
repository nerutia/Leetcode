# 二叉树的所有路径

# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 说明: 叶子节点是指没有子节点的节点。


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        self.r = []
        self.helper(root, [])
        return self.r


    def helper(self, root: TreeNode, path):
        path.append(str(root.val))
        tl = [i for i in path]
        tr = [i for i in path]
        if root.left == None and root.right == None:
            self.r.append("->".join(path))
            return
        if root.left:
            self.helper(root.left, tl)
        if root.right:
            self.helper(root.right, tr)




