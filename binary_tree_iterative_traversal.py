from collections import deque


class TreeNode:

    def __init__(self, val: int):
        self.value = val
        self.left = None
        self.right = None


head = TreeNode(1)
head.left = TreeNode(2)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.left.left.right = TreeNode(6)
head.right = TreeNode(3)
head.right.left = TreeNode(8)
head.right.left.left = TreeNode(10)


def iterative_preorder(head: TreeNode) -> list[TreeNode]:
    inorder_values = []
    if head is None:
        return inorder_values
    q = deque()
    q.append(head)
    # note for level order we use queue and for inorder iterative we use stack
    while len(q) != 0:
        temp = q.pop()
        inorder_values.append(temp.value)
        if temp.right:  # append right first since in stack this will pop out after left since it went in first
            q.append(temp.right)
        if temp.left:  # went in last will come out first LIFO stack
            q.append(temp.left)
    return inorder_values


def iterative_inorder(head: TreeNode) -> list[TreeNode]:
    inorder_values = []
    if head is None:
        return inorder_values
    stk = deque()
    temp = head
    while True:
        if temp is not None:
            stk.append(temp)
            temp = temp.left
        else:
            if len(stk) == 0:
                break
            temp = stk.pop()
            inorder_values.append(temp.value)
            temp = temp.right
    return inorder_values


def iterative_postorder(head: TreeNode) -> list[TreeNode]:
    post_order = []
    if head is None:
        return post_order
    stk1 = deque()
    stk2 = deque()
    stk1.append(head)
    while len(stk1) != 0:
        t = stk1.pop()
        stk2.append(t)
        if t.left:
            stk1.append(t.left)
        if t.right:
            stk1.append(t.right)
    post_order = [stk2[i].value for i in range(len(stk2) - 1, -1, -1)]
    return post_order


def pre_in_post(head: TreeNode):
    preo = []
    ino = []
    posto = []
    if head is None:
        return
    stk = [[head, 1]]
    while len(stk) != 0:
        temp = stk.pop()
        if temp[1] == 1:
            preo.append(temp[0].value)
            temp[1] += 1
            stk.append(temp)
            # push left elements
            if temp[0].left:
                stk.append([temp[0].left, 1])
        elif temp[1] == 2:
            ino.append(temp[0].value)
            temp[1] += 1
            stk.append(temp)
            # push right elements
            if temp[0].right:
                stk.append([temp[0].right, 1])
        elif temp[1] == 3:
            posto.append(temp[0].value)
    print(f"PREORDER :{preo}")
    print(f"INORDER  :{ino}")
    print(f"POSTORDER:{posto}")


print(f"PREORDER :{iterative_preorder(head)}")
print(f"INORDER  :{iterative_inorder(head)}")
print(f"POSTORDER:{iterative_postorder(head)}")
pre_in_post(head)
