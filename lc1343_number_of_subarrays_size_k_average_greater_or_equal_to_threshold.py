class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """

        l = r = 0
        s = 0
        cnt = 0
        for i in range(k):
            s += arr[i]
            r = i
        if s >= threshold * k:
            cnt += 1
        for i in range(len(arr) - k):
            l += 1
            r += 1
            s = s + arr[r] - arr[l - 1]
            if s >= threshold * k:
                cnt += 1
        return cnt