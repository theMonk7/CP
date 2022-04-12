from collections import deque


def printFirstNegativeInteger(A, N, K):
    # code here
    f = l = 0
    q = deque()
    res = []
    for i in range(K):
        if A[i] < 0:
            q.append(A[i])
        l = i

    for i in range(1, N - K + 1):
        if len(q) != 0:
            res.append(q[0])
        else:
            res.append(0)
        f += 1
        l += 1
        if len(q) != 0 and A[f - 1] == q[0]:
            q.popleft()
        if A[l] < 0:
            q.append(A[l])
    if len(q) != 0:
        res.append(q[0])
    else:
        res.append(0)
    return res

print(printFirstNegativeInteger([-8, 2, 3, -6, 10],5,2))