# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]):
        if len(nums) == 0:
            return None
        m_ind = -1
        m = -1
        for i in range(len(nums)):
            if nums[i] > m:
                m = nums[i]
                m_ind = i
        head = TreeNode(m)
        head.left = self.constructMaximumBinaryTree(nums[:m_ind])
        head.right = self.constructMaximumBinaryTree(nums[m_ind+1:])
        return head