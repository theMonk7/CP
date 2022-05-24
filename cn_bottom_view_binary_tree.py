from collections import defaultdict
from collections import deque


def bottomView(root):
    # Write your code here.
    # This function returns a list of nodes which is the required bottom view of the tree.
    if root is None:
        return []
    hm = defaultdict()
    q = deque()
    q.append([root, 0])
    while len(q) != 0:
        t = q.popleft()
        hm[t[1]] = t[0].data
        if t[0].left:
            q.append([t[0].left, t[1] - 1])
        if t[0].right:
            q.append([t[0].right, t[1] + 1])
    res = []
    for e in sorted(list(hm.keys())):
        res.append(hm[e])
    return res
