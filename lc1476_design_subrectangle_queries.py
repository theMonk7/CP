import copy


class SubrectangleQueries(object):

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.matrix = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.matrix[i][j] = newValue

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        if row < len(self.matrix) and col < len(self.matrix[0]):
            return self.matrix[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)