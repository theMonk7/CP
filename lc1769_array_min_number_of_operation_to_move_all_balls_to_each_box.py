from functools import reduce
class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        hm = {0: [], 1: []}
        res = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                hm[1].append(i)
            else:
                hm[0].append(i)
        for i in range(len(boxes)):
            res.append(reduce(lambda x, y: abs(x - i) + abs(y - i), hm[1]))
        return res
print(Solution().minOperations("001011"))