class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        cnt = 0
        num = str(num)
        for i in range(len(num) - k + 1):
            if int(num[i:i + k]) != 0:
                if int(num) % int(num[i:i + k]) == 0:
                    cnt += 1
        return cnt

print(Solution().divisorSubstrings(240,2))
