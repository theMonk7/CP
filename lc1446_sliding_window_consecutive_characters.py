class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = r = -1
        po = 0
        hm = {}
        while r < len(s):
            if len(hm) == 1:
                if r - l > po:
                    po = r - l
                r += 1
                if r < len(s):
                    if hm.__contains__(s[r]):
                        hm[s[r]] += 1
                    else:
                        hm[s[r]] = 1
            elif len(hm) < 1:
                r += 1
                if r < len(s):
                    if hm.__contains__(s[r]):
                        hm[s[r]] += 1
                    else:
                        hm[s[r]] = 1
            else:
                l += 1
                if hm.__contains__(s[l]):
                    hm[s[l]] -= 1
                    if hm[s[l]] == 0:
                        del hm[s[l]]
        return po
