class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        i = m
        j = n
        res = ""
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res += str1[i - 1]
                i -= 1
                j -= 1
            else:
                if dp[i][j] == dp[i - 1][j]:
                    i -= 1
                else:
                    j -= 1
        res = res[::-1]
        i = j = r = 0
        final = ""
        while r < len(res):
            if str1[i] == str2[j] == res[r]:
                final += str1[i]
                i += 1
                j += 1
                r += 1
            else:
                if str1[i] == res[r] and str2[j] != res[r]:
                    final += str2[j]
                    j += 1
                elif str2[j] == res[r] and str1[i] != res[r]:
                    final += str1[i]
                    i += 1
                else:
                    final += str1[i]
                    final += str2[j]
                    i += 1
                    j += 1
        final += str1[i:]
        final += str2[j:]
        return final
print(Solution().shortestCommonSupersequence(
"leetcode",
"molejjteet"))