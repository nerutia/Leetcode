# 二叉树的层平均值

# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return None
        lv = []
        st = [root]
        while len(st) > 0:
            t = []
            v = []
            for m in st:
                v.append(m.val)
                if m.left:
                    t.append(m.left)
                if m.right:
                    t.append(m.right)
            lv.append(v)
            st = t
        return [mean(i) for i in lv]

