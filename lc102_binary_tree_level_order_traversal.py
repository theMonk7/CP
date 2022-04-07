# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        result = []
        global q
        q = deque()
        q.append(root)

        while len(q) != 0:
            temp = []

            while len(q) != 0:
                temp.append(q.popleft())
            result.append(list(map(self.fun, temp)))
        return result

    def fun(self, el):
        if el.left:
            q.append(el.left)
        if el.right:
            q.append(el.right)
        return el.val