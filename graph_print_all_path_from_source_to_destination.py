def print_all_paths_s_t_d(n, edges, s, d):
    visited = [0] * n
    adj_list = [[] for _ in range(n)]
    res = []
    for e in edges:
        adj_list[e[0]].append((e[1], e[2]))
        adj_list[e[1]].append((e[0], e[2]))
    ans_k = []
    for i in range(1):

        if visited[i] == 0:
            re = []
            __find_all_path(visited, adj_list, i, d, 0, [i], re)
            ans_k.append(re)
        # if re != []:

    return ans_k


def __find_all_path(visited, adj, s, d, path_sum, path, res):
    # global INT_MAX
    # global INT_MIN
    # global best_path
    if s == d:
        # if path_sum > INT_MIN:
        #     INT_MIN = path_sum
        #     best_path = path
        # print(path_sum)
        res.append(path)
        return
    visited[s] = 1
    # res.append(s)
    for e in adj[s]:
        if visited[e[0]] == 0:
            __find_all_path(visited, adj, e[0], d, e[1] + path_sum, path + [e[0]], res)
    visited[s] = 0


INT_MAX = 1000000000000000000000
INT_MIN = -100000000000000000000
best_path = []

edges = [[0,1,10],[1,2,10],[2,3,10],[0,3,40],[3,4,2],[4,5,3],[5,6,3],[4,6,8]]
# edges = [[0, 1, 10], [2, 3, 20], [4, 6, 5], [4, 5, 12], [5, 6, 15]]

print(print_all_paths_s_t_d(7, edges, 0, 6))
# print(INT_MIN, best_path)
