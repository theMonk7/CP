class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        s = 0
        for i in range(len(columnTitle)):
            s = s + pow(26,i) * (ord(columnTitle[len(columnTitle)-i-1]) - 64)
        return s