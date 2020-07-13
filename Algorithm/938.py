# 二叉搜索树的范围和

# 给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
# 二叉搜索树保证具有唯一的值。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        res = 0
        if L <= root.val <= R:
            res += root.val
        if L <= root.val:       #如果当前节点比左边界小，则该节点的左子树不用遍历了（都是小于该节点的值，已超出范围）
            res += self.rangeSumBST(root.left, L, R)
        if root.val <= R:       #如果当前节点比右边界大，则该节点的右子树不用遍历了（都是大于该节点的值）
            res += self.rangeSumBST(root.right, L, R)
        return res


c = Solution()
print(c.rangeSumBST(root = [10,5,15,3,7,null,18], L = 7, R = 15))

