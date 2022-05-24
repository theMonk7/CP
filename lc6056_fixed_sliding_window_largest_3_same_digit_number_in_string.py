class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = 0
        r = 2
        valid = -1
        if self.checkValid(num[l:r + 1]):
            valid = num[l:r + 1]

        for i in range(len(num) - 3):
            l += 1
            r += 1
            if self.checkValid(num[l:r + 1]):
                if int(num[l:r + 1]) > int(valid):
                    valid = num[l:r + 1]
        return str(valid) if valid != -1 else ""

    def checkValid(self, ss: str) -> bool:
        s = ss[0]
        for i in range(3):
            if ss[i] != s:
                return False
        return True
