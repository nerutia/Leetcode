# N叉树的后序遍历

# 给定一个 N 叉树，返回其节点值的后序遍历。

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        st = [root]
        res = []
        # st is a stack, st is not empty
        while st and st[0]:
            t = st.pop()
            res.append(t.val)
            st.extend(t.children)
        return res[::-1]
        

