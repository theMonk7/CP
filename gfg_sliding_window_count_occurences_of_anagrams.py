class Solution:

    def search(self, pat, txt):
        # code here
        hm_pat = {}
        for e in pat:
            self.insertHM(hm_pat, e)

        cnt = 0
        f = l = 0
        hm = {}
        for i in range(len(pat)):
            self.insertHM(hm, txt[i])
            l = i

        for i in range(len(txt) - len(pat)):
            if hm == hm_pat:
                cnt += 1
            f += 1
            l += 1
            hm[txt[f - 1]] -= 1
            self.insertHM(hm, txt[l])
            if hm[txt[f - 1]] == 0:
                del hm[txt[f - 1]]
        if hm == hm_pat:
            cnt += 1
        return cnt

    def insertHM(self, hm, val):
        if hm.__contains__(val):
            hm[val] += 1
        else:
            hm[val] = 1
