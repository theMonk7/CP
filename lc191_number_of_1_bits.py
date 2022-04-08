class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        a = str(bin(n))
        for c in a:
            if c == "1":
                cnt += 1
        return cnt

print(Solution().hammingWeight(11111110000))