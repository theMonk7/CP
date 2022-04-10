class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        rep = []
        sum = 0
        while 1:

            while n != 0:
                a = divmod(n, 10)
                sum += a[1] * a[1]
                n = a[0]
            if sum in rep:
                return False
            elif sum == 1:
                return True
            else:
                rep.append(sum)
                n = sum
                sum = 0