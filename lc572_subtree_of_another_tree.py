# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root is None:
            return False

        if root.val == subRoot.val:
            if self.matcher(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def matcher(self, r1, r2):
        if r1 is None and r2 is None:
            return True
        elif r1 is None or r2 is None:
            return False
        else:
            return r1.val == r2.val and self.matcher(r1.left, r2.left) and self.matcher(r1.right, r2.right)
