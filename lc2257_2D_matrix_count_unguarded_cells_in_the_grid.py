class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:

        maze = [[0] * n for i in range(m)]
        for g in guards:
            maze[g[0]][g[1]] = "G"
        for w in walls:
            maze[w[0]][w[1]] = "W"

        self.marker(maze, m, n, 0)
        self.marker(maze, n, m, 1)
        self.marker(maze, m, n, 2)
        self.marker(maze, n, m, 3)
        print(maze)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 0:
                    cnt += 1
        return cnt

    def marker(self, maze: list[list[object]], m: int, n: int, pos):
        is_g = False
        if pos == 0:
            for i in range(m):
                is_g = False
                for j in range(n):
                    if maze[i][j] == "G":
                        is_g = True
                    elif maze[i][j] == "W":
                        is_g = False
                    elif maze[i][j] == 1:
                        continue
                    else:
                        if is_g:
                            maze[i][j] = 1
        elif pos == 1:
            for i in range(m):
                is_g = False
                for j in range(n):
                    if maze[j][i] == "G":
                        is_g = True
                    elif maze[j][i] == "W":
                        is_g = False
                    elif maze[j][i] == 1:
                        continue
                    else:
                        if is_g:
                            maze[j][i] = 1
        elif pos == 2:
            for i in range(m - 1, -1, -1):
                is_g = False
                for j in range(n - 1, -1, -1):
                    if maze[i][j] == "G":
                        is_g = True
                    elif maze[i][j] == "W":
                        is_g = False
                    elif maze[i][j] == 1:
                        continue
                    else:
                        if is_g:
                            maze[i][j] = 1
        else:
            for i in range(m - 1, -1, -1):
                is_g = False
                for j in range(n - 1, -1, -1):
                    if maze[j][i] == "G":
                        is_g = True
                    elif maze[j][i] == "W":
                        is_g = False
                    elif maze[j][i] == 1:
                        continue
                    else:
                        if is_g:
                            maze[j][i] = 1

print(Solution().countUnguarded(m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1]]))