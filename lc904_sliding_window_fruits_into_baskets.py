class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # this is equivalent to variable sliding window with at most 2 unique characters
        n = len(fruits)
        hm = {}
        k = 2
        l = r = -1
        ma = 0
        while r < n:
            if len(hm) <= k:
                if r - l > ma:
                    ma = r - l
                r += 1
                if r < n:
                    if hm.__contains__(fruits[r]):
                        hm[fruits[r]] += 1
                    else:
                        hm[fruits[r]] = 1
            else:
                l += 1
                if l < n:
                    if hm.__contains__(fruits[l]):
                        hm[fruits[l]] -= 1
                        if hm[fruits[l]] == 0:
                            del hm[fruits[l]]
        return ma

