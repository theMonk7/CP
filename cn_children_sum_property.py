def changeTree(root):
    # Write your code here.
    if root is None:
        return
    c_sum = 0
    if root.left:
        c_sum += root.left.data
    if root.right:
        c_sum += root.right.data
    if c_sum < root.data:
        if root.left:
            root.left.data = root.data
        if root.right:
            root.right.data = root.data
    changeTree(root.left)
    changeTree(root.right)
    tot = 0
    if root.left:
        tot += root.left.data
    if root.right:
        tot += root.right.data
    if root.left or root.right:
        root.data = tot
