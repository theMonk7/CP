class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        n = (coordinates[1][1] - coordinates[0][1])
        d = (coordinates[1][0] - coordinates[0][0])
        if d == 0:
            for i in range(1, len(coordinates)):
                if (coordinates[i][0] - coordinates[i - 1][0]) != d:
                    return False
        else:
            m = n / d
            for i in range(1, len(coordinates)):
                if (coordinates[i][0] - coordinates[i - 1][0]) == 0:
                    return False
                elif (coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0]) != m:
                    return False
        return True
