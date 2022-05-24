# Following is the Binary Tree node structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def addLeftNodes(root, res):
    temp = root.left
    while temp:
        if not isLeaf(temp):
            res.append(temp.data)
        if temp.left:
            temp = temp.left
        else:
            temp = temp.right


def addRightNodes(root, res):
    temp = root.right
    ress = []
    while temp:
        if not isLeaf(temp):
            ress.append(temp.data)
        if temp.right:
            temp = temp.right
        else:
            temp = temp.left
    for i in range(len(ress)):
        res.append(ress.pop())


def addLeaves(root, res):
    if root:
        if isLeaf(root):
            res.append(root.data)
        addLeaves(root.left, res)
        addLeaves(root.right, res)


def isLeaf(root):
    return root and root.left is None and root.right is None


def traverseBoundary(root):
    # Write your code here.
    res = []
    if not isLeaf(root):
        res.append(root.data)

    addLeftNodes(root, res)
    addLeaves(root, res)
    addRightNodes(root, res)
    return res


head = BinaryTreeNode(1)
head.left = BinaryTreeNode(2)
head.left.left = BinaryTreeNode(4)
head.left.right = BinaryTreeNode(5)
head.left.right.left = BinaryTreeNode(6)
head.right = BinaryTreeNode(3)
# head.right.left = BinaryTreeNode(8)
head.right.right = BinaryTreeNode(7)
print(traverseBoundary(head))
