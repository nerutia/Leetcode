#  从上到下打印二叉树 II

#  从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        p,q = [root],[]
        r = []
        while len(p) > 0:
            t = []
            while len(p) > 0:
                tt = p.pop(0)
                t.append(tt.val)
                if tt.left:
                    q.append(tt.left)
                if tt.right:
                    q.append(tt.right)
            r.append(t)
            p = q
            q = []
        return r
            




        



