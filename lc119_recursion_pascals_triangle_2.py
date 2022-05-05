class Solution:
    pofd= 43
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        arr = self.getRow(rowIndex-1)
        return [1] + [arr[i] + arr[i+1] for i in range(len(arr)-1)]  + [1]
