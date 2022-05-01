class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}
        for e in s:
            if hm.__contains__(e):
                hm[e] += 1
            else:
                hm[e] = 1
        for i in range(len(s)):
            if hm[s[i]] == 1:
                return i
        return -1