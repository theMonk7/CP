class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        return max(list(map(lambda x: len(x.split(" ")), sentences)))
