# 二叉搜索树的最近公共祖先

# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findRoute(r, x):
            res = [r]
            while r.val != x.val:
                if r.val < x.val:
                    r = r.right
                else:
                    r = r.left
                res.append(r)
            return res

        rl = findRoute(root, p)
        rr = findRoute(root, q)
        n = min(len(rl), len(rr))
        pos = n - 1
        for i in range(n):
            if rl[i].val != rr[i].val:
                pos = i - 1
                break
        return rl[pos]
        



c = Solution()
print(c.lowestCommonAncestor(root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8))


