# 递增顺序查找树

# 给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def modify(root):
            if root == None:
                return
            if root.left == None:
                root.right = modify(root.right)
                return root
            new_root = modify(root.left)
            root.left = None
            t = new_root
            while t and t.right:
                t = t.right
            t.right = root
            root.right = modify(root.right)
            return new_root
        return modify(root)

        # 大佬做法
        # 第二行保证了res迭代到最左下的节点，且令其为新的root.
        # def increasingBST(self, root, tail = None):
        #     if not root: return tail
        #     res = self.increasingBST(root.left, root)
        #     root.left = None
        #     root.right = self.increasingBST(root.right, tail)
        #     return res

