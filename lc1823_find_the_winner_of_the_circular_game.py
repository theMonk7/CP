class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n + 1)]
        return self.solver(arr, k, 0)

    def solver(self, arr, k, ind) -> int:
        if len(arr) == 1:
            return arr[0]
        ind = (ind + k - 1) % len(arr)
        return self.solver(arr[:ind] + arr[ind + 1:], k, ind)