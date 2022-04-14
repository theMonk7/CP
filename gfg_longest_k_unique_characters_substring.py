# User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        hm = {}
        l, r = -1, -1
        ma = -1
        # if hm.__contains__(s[r]):
        #         hm[s[r]] += 1
        #     else:
        #         hm[s[r]] = 1
        while r < len(s):

            if len(hm) == k:
                if r - l > ma:
                    ma = r - l
                r += 1
                if r < len(s):
                    self.hm_adder(hm, s[r])
            elif len(hm) > k:
                l += 1
                if hm.__contains__(s[l]):
                    hm[s[l]] -= 1
                    if hm[s[l]] == 0:
                        del hm[s[l]]
            else:
                r += 1
                if r < len(s):
                    self.hm_adder(hm, s[r])
        return ma

    def hm_adder(self, hm, val):
        if hm.__contains__(val):
            hm[val] += 1
        else:
            hm[val] = 1


print(Solution().longestKSubstr([0],2))