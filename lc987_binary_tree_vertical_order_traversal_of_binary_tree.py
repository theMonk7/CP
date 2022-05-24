# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        vert = collections.defaultdict(list)
        q = collections.deque()
        q.append([root, 0, 0])

        while len(q) != 0:
            n = len(q)
            for i in range(n):
                t = q.popleft()
                vert[t[2]].append([t[1], t[0].val])
                if t[0].left:
                    q.append([t[0].left, t[1] + 1, t[2] - 1])
                if t[0].right:
                    q.append([t[0].right, t[1] + 1, t[2] + 1])
        k = list(vert.keys())
        k.sort()
        res = []
        for e in k:
            y = [el[1] for el in sorted(vert[e])]
            res.append(y)
        return res
