class Solution:
    def check(self, n, edges):
        adj = [[] for _ in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        vis = [0] * n
        res = []
        for i in range(n):
            path = []
            if vis[i] == 0:
                self.__ham_cycle(adj, vis, path + [i], i, res, 0, i)
                if path != []:
                    res.append(path)
        return res

    def __ham_cycle(self, adj, vis, path, src, res, seen, osrc):
        if seen == len(vis) - 1:
            for i in range(len(vis)):
                if src != i and vis[i] == 0:
                    return
                if osrc not in adj[src]:
                    return
            res.append(path)
            return
        vis[src] = 1
        for nbr in adj[src]:
            if vis[nbr] == 0:
                self.__ham_cycle(adj, vis, path + [nbr], nbr, res, seen + 1, osrc)
        vis[src] = 0


# print(Solution().check(7, [[0, 1], [0, 3], [1, 2], [2, 3], [3, 4], [2, 5], [4, 5], [4, 6], [5, 6]]))
