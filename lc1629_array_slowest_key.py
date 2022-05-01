class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        l = list(zip(releaseTimes, keysPressed))
        mapper = [(l[i][0], l[i][1]) if i == 0 else (l[i][0] - l[i - 1][0], l[i][1]) for i in range(len(l))]
        return max(mapper, key=lambda x: (x[0], x[1]))[1]
