from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getTopView(root):
    # Write your code here.
    if root is None:
        return []

    hm = {}
    q = deque()
    q.append([root, 0])
    while len(q) != 0:
        t = q.popleft()
        if hm.__contains__(t[1]):
            pass
        else:
            hm[t[1]] = t[0].val
        if t[0].left:
            q.append([t[0].left, t[1] - 1])
        if t[0].right:
            q.append([t[0].right, t[1] + 1])
    res = []
    for e in sorted(list(hm.keys())):
        res.append(hm[e])
    return res


head = TreeNode(1)
head.left = TreeNode(2)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.left.right.left = TreeNode(6)
head.right = TreeNode(3)
head.right.left = TreeNode(8)
head.right.right = TreeNode(7)
print(getTopView(head))