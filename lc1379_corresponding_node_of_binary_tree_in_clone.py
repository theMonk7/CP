# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        if cloned is None or original is None:
            return None

        elif cloned.val == original.val == target.val:
            return cloned
        a = self.getTargetCopy(original.left, cloned.left, target)
        b = self.getTargetCopy(original.right, cloned.right, target)
        return a if b is None else b
