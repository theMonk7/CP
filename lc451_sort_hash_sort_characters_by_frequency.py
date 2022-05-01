class Solution:
    def frequencySort(self, s: str) -> str:
        h = {}
        sa = list(s)
        for e in sa:
            if h.__contains__(e):
                h[e] += 1
            else:
                h[e] = 1

        sa = list(set(sa))
        sa.sort(key=lambda x: h[x])
        res = ""
        for e in sa:
            res += e * h[e]

        return res[::-1]