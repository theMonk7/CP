class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = list(str(n))
        if len(k) == 1:
            return 0
        return reduce(lambda x,y: int(x) * int(y), k) - reduce(lambda x,y: int(x) + int(y), k)