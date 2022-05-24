class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    maxi = -5000000

    def maxPathSum(self, root: TreeNode) -> int:
        self.fun(root)
        return self.maxi

    def fun(self, root):
        if root is None:
            return 0
        lh = self.fun(root.left)
        rh = self.fun(root.right)
        self.maxi = max(self.maxi, lh + rh + root.val)

        return max(0, root.val + max(lh, rh))