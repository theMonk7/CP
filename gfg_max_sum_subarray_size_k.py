class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here
        f, l = 0, K-1
        s = 0
        ma = s
        for i in range(f, l+1):
            s += Arr[i]
        ma = s
        for i in range(1,N-K+1):
            f += 1
            l += 1
            s = s - Arr[f-1] + Arr[l]
            if s > ma:
                ma = s
        return ma