# User function Template for python3
class Solution:
    def check(self, N, M, Edges):
        # code here
        visited = [0] * (N + 1)
        adj = [[] for _ in range(N + 1)]
        for e in Edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        res = []
        for i in range(1, N + 1):
            path = []
            if visited[i] == 0:
                self.dfs(adj, visited, i, path + [i], 0, res)
        return len(res)

    def dfs(self, adj, vis, s, path, vis_ct, res):
        if vis_ct == len(vis) - 2:
            for i in range(1, len(vis)):
                if i != s and vis[i] == 0:
                    return
            res.append(path)
            return

        vis[s] = 1
        for nbr in adj[s]:
            if vis[nbr] == 0:
                self.dfs(adj, vis, nbr, path + [nbr], vis_ct + 1, res)
        vis[s] = 0

print(Solution().check(
10, 14,
[[2,1],[10,2],[6,3],[5,4],[10,5], [10,6],[6,7],[6,8],[10,9],[4,9],[3,8],[3,7],[5,9],[6,5]]))