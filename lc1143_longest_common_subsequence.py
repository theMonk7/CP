class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        # res = []
        # return self.lcs_rec2(n1,text1,n2,text2)
        return self.lcs_dp(n1, text1, n2, text2)
        # m = 0
        # print(res)
        # for e in res:
        #     if len(e) > m:
        #         m = len(e)
        # return m

    def lcs_rec(self, n1, t1, n2, t2, lc, res):
        if n1 == 0 or n2 == 0:
            res.append("".join(lc))
            return

        if t1[n1 - 1] == t2[n2 - 1]:
            lc.append(t1[n1 - 1])
            self.lcs_rec(n1 - 1, t1, n2 - 1, t2, lc[:], res)
        else:
            self.lcs_rec(n1 - 1, t1, n2, t2, lc[:], res)
            self.lcs_rec(n1, t1, n2 - 1, t2, lc[:], res)

    def lcs_rec2(self, n1, t1, n2, t2):
        if n1 == 0 or n2 == 0:
            return 0

        if t1[n1 - 1] == t2[n2 - 1]:

            return 1 + self.lcs_rec2(n1 - 1, t1, n2 - 1, t2)
        else:
            t = self.lcs_rec2(n1 - 1, t1, n2, t2)
            k = self.lcs_rec2(n1, t1, n2 - 1, t2)
            return max(t, k)

    def lcs_dp(self, n1, t1, n2, t2):
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        prev = [0] * (n1 + 1)
        curr = [0] * (n1 + 1)
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if t1[j - 1] == t2[i - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            # prev = curr[:]
        print(self.__print_selected_subsequence(dp, t1, t2))
        # for e in dp:
        #     print(e)
        return dp[n2][n1]

    def __print_selected_subsequence(self, dp, t1, t2):
        n1 = len(t1)
        n2 = len(t2)
        i = n2
        j = n1
        res = []
        while i > 0 and j > 0:
            if t1[j - 1] == t2[i - 1]:
                res.append(t1[j - 1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        k = "".join(res)
        return k[::-1]


s1 = "abcdeffd"
s2 = "acdefgfd"
# print(Solution().lcs_dp(len(s1), s1, len(s2), s2))


def search(arr, n, tar):
    l = 0
    r = n - 1
    lg = n
    while l <= r:
        m = (l + r) // 2

        if arr[m] >= tar:
            r = m - 1
            lg = m
        else:
            l = m + 1
    return n - lg
# print(search([1,2,5,6,7],5,9))
def isBadVersion(m):
    if m >= 7:
        return True
    else:
        return False


def firstBadVersion(self, n: int) -> int:

    l = 1
    r = n
    bad = 0
    while l <= r:
        m = (l + r) // 2
        if isBadVersion(m):
            bad = m
            r = m - 1
        else:
            l = m + 1
    return bad
# print(firstBadVersion(10,7))

    def mySqrt(x: int) -> int:

        l = 1
        r = x
        while l <= r:
            m = (l + r) // 2
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m - 1
            elif m * m == x:
                return m
        return r