class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        l = r = -1
        unq = True
        ma = 0
        hm = {}
        while r < n:
            if unq:
                r += 1
                if r < n:
                    if hm.__contains__(s[r]):
                        hm[s[r]] += 1
                        unq = False
                    else:
                        hm[s[r]] = 1
                        if r - l > ma:
                            ma = r - l
            else:
                l += 1
                if hm.__contains__(s[l]):
                    hm[s[l]] -= 1
                    if hm[s[l]] == 0:
                        del hm[s[l]]
                    unq = True
                    for e in list(hm.values()):
                        if e > 1:
                            unq = False

        return ma

print(Solution().lengthOfLongestSubstring("tmmzuxt"))
