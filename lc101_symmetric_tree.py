# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def isSymmetricIterative(self, root):
        if root is None:
            return True
        q = deque()
        q.append([root.left, root.right])
        while len(q) != 0:
            popped = q.popleft()
            l = popped[0]
            r = popped[1]
            if not l and not r:
                continue
            elif not l or not r:
                return False
            else:
                if l.val == r.val:
                    q.append([l.left,r.right])
                    q.append([l.right, r.left])
                else:
                    return False
        return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.checker(root.left, root.right)

    def checker(self, l, r):
        if l is None and r is None:
            return True
        elif l is None or r is None:
            return False
        else:
            return l.val == r.val and (self.checker(l.left, r.right)) and (self.checker(l.right, r.left))
