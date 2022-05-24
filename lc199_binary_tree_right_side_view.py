# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        d = deque()
        d.append(root)
        res = []
        while len(d) != 0:
            temp = []
            n = len(d)
            for i in range(n):
                t = d.popleft()
                temp.append(t.val)
                if t.left:
                    d.append(t.left)
                if t.right:
                    d.append(t.right)
            res.append(temp)
        return [e[len(e) - 1] for e in res]

    def rightSideViewDFS(self, root: TreeNode) -> list[int]:
        res = []
        self.getRightView(root, res, 0)
        return res

    def getRightView(self, root, res, level) -> list[int]:
        if root is None:
            return []
        
