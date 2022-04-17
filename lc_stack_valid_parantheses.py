from collections import deque


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q = deque()
        for b in s:
            if (b == ")" or b == "}" or b == "]") and len(q) == 0:
                return False
            elif (b == ")" or b == "}" or b == "]") and (
                    (q[-1] == "(" and b == ")") or (q[-1] == "{" and b == "}") or (q[-1] == "[" and b == "]")):
                q.pop()
            else:
                q.append(b)
        return len(q) == 0
