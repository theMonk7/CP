def dfsOfGraph(V, adj):
    # code here
    visited = [0] * (V)
    dfs_op = []
    for i in range(1):
        if visited[i] == 0:
            dfs(i, visited, dfs_op, adj)
    return dfs_op


def dfs(node, visited, dfs_op, adj_list):
    visited[node] = 1
    dfs_op.append(node)
    for e in adj_list[node]:
        if visited[e] == 0:
            dfs(e, visited, dfs_op, adj_list)

print(dfsOfGraph(5,[[1, 2, 3], [0], [0, 4], [0], [2], []]))