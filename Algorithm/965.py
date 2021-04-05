# 单值二叉树

# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
# 只有给定的树是单值二叉树时，才返回 true；否则返回 false。

# 已评论https://leetcode-cn.com/problems/univalued-binary-tree/comments/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode, c = None) -> bool:
        if root == None:
            return True
        if c != None and root.val != c:
            return False
        return self.isUnivalTree(root.left, root.val) and self.isUnivalTree(root.right, root.val)
        # 简写为一行：
        # return root == None or ((c == None or root.val == c) and self.isUnivalTree(root.left, root.val) and self.isUnivalTree(root.right, root.val))


