# 将有序数组转换为二叉搜索树

# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def makeTree(l, r):
            if l > r:
                return None
            h = TreeNode(nums[(l+r)//2])
            h.left = makeTree(l,(l+r)//2-1)
            h.right = makeTree((l+r)//2+1,r)
            return h
        return makeTree(0,len(nums)-1)


