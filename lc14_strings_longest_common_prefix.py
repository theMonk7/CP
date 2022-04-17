class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        pat = []
        a, b = min(strs), max(strs)
        for i in range(min(len(a), len(b))):
            if a[i] == b[i]:
                pat.append(a[i])
            else:
                break
        return "".join(pat)
