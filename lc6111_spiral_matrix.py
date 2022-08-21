class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def spiralMatrix(self, m: int, n: int, head) -> list[list[int]]:

        mat = [[-1] * (n) for _ in range(m)]
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        drc = 0
        temp = head
        while temp != None:

            if drc == 0:
                for i in range(left, right + 1):
                    if temp == None:
                        break
                    print(mat[top][i])
                    # temp = temp.next
                top += 1
            elif drc == 1:
                for i in range(top, bottom + 1):
                    if temp == None:
                        break
                    print(mat[i][right])
                    # temp = temp.next
                right -= 1
            elif drc == 2:
                for i in range(right, left - 1, -1):
                    if temp == None:
                        break
                    print(mat[bottom][i])
                    # temp = temp.next
                bottom -= 1
            elif drc == 3:
                for i in range(bottom, top - 1, -1):
                    if temp == None:
                        break
                    print(mat[i][left])
                    # temp = temp.next
                left += 1
            drc = (drc + 1) % 4
        return mat

# print(Solution().spiralMatrix(3,5,ListNode()))
arr = []
for i in range(1,21):
    for j in range(1,21):
        prob = 1/2 * (i / (i+j)) + 1/2 * ((20-i) / (20-i+20-j))
        arr.append([prob,i,j])
