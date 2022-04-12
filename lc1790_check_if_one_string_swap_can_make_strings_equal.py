class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        elif len(s1) != len(s2):
            return False
        else:
            pos = []
            for i in range(len(s1)):
                if s1[i] != s2[i] and len(pos) <= 2:
                    pos.append(i)

            if len(pos) == 1:
                return False
            else:
                k = list(s1)
                t = k[pos[0]]
                k[pos[0]] = k[pos[1]]
                k[pos[1]] = t
                return s2 == "".join(k)



