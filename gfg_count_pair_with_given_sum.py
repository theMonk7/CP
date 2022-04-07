class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        h_map = {}
        ans = 0
        for i in range(n):
            if h_map.__contains__(k - arr[i]):
                ans += h_map[k - arr[i]]

            if h_map.__contains__(arr[i]):
                h_map[arr[i]] += 1
            else:
                h_map[arr[i]] = 1
        return ans        