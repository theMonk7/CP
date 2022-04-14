from collections import deque


class Solution:
    # @param A : tuple of integers
    # @param B : integer window size
    # @return a list of integers

    def slidingMaximum(self, A, B):
        if B >= len(A):
            return [max(A)]
        q = deque()
        for i in range(B):
            if len(q) != 0 and A[i] > q[len(q) - 1]:
                while len(q) > 0 and q[len(q) - 1] < A[i]:
                    q.pop()
            q.append(A[i])
        res = [q[0]]
        for i in range(1, len(A) - B + 1):
            if A[i - 1] == q[0]:
                q.popleft()
            if len(q) > 0 and q[len(q) - 1] < A[i + B - 1]:
                while len(q) > 0 and q[len(q) - 1] < A[i + B - 1]:
                    q.pop()

            q.append(A[i + B - 1])
            res.append(q[0])
        return res
