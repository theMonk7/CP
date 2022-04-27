class Solution:
    def countLatticePoints(self, circles: list[list[int]]) -> int:
        sol_set = set()

        for circle in circles:
            x_range = [(circle[0] - circle[2]) // 1, (circle[0] + circle[2]) // 1]
            y_range = [(circle[1] - circle[2]) // 1, (circle[1] + circle[2]) // 1]
            r = circle[2]
            for x in range(x_range[0], x_range[1] + 1):
                for y in range(y_range[0], y_range[1] + 1):
                    if (x - circle[0]) * (x - circle[0]) + (y - circle[1]) * (y - circle[1]) <= r * r:
                        sol_set.add((x, y))
        return len(sol_set)

print(Solution().countLatticePoints([[2,2,1]]))