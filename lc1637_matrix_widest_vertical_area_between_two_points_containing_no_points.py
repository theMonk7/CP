class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        rows = [e[0] for e in points]
        rows.sort()
        m = 0
        for i in range(1,len(rows)):
            if rows[i] - rows[i-1] > m:
                m = rows[i] - rows[i-1]
        return m