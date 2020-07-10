# 最小高度树

# 给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# TODO
class Solution:
    # 给定的是有序数组
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        t = self.createTree(nums)
        self.showTree(t)
        return t


    def createTree(self, n: List[int]):
        l = len(n)
        if l <= 0:
            return None
        root = TreeNode(n[l//2])
        root.left = self.createTree(n[:l//2])
        root.right = self.createTree(n[l//2+1:])
        return root


    def showTree(self, root: TreeNode):
        if root.val != None:
            print(root.val)
        if root.left != None:
            self.showTree(root.left)
        if root.right != None:
            self.showTree(root.right)



c = Solution()
print(c.sortedArrayToBST(nums =  [-10,-3,0,5,9]))

