class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ind = -1
        try:
            ind = haystack.index(needle)
        except ValueError:
            ind = -1

        return ind
print(Solution().strStr("hello", "ll"))