# 从根到叶的二进制数之和

# 给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。
# 对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
# 以 10^9 + 7 为模，返回这些数字之和。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode, v = 0) -> int:
        if root == None:
            return 0
        v = 2 * v + root.val
        if root.left == None and root.right == None:
            return v
        return self.sumRootToLeaf(root.left, v) + self.sumRootToLeaf(root.right, v)


        



