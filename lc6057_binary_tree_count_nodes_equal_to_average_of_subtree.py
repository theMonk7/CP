class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    cnt = 0

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.helper(root)
        return self.cnt

    def helper(self, root):
        if root is None:
            return [0, 0]

        lt = self.helper(root.left)
        rt = self.helper(root.right)

        avg = (lt[0] + rt[0] + root.val) // (lt[1] + rt[1] + 1)
        if avg == root.val:
            self.cnt += 1
        return [lt[0] + rt[0] + root.val, (lt[1] + rt[1] + 1)]
