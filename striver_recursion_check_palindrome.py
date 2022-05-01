def rec_check_palindrome(s, n, i):
    if i > n // 2:
        return True
    return s[i] == s[n - i - 1] and rec_check_palindrome(s, n, i + 1)


s = "abbaabb"
n = len(s)
print(rec_check_palindrome(s, n, 0))


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: list[int]) -> list[int]:
        bob = [0] * len(aliceArrows)
        return [self.winner(numArrows, aliceArrows, bob, 0)]

    def winner(self, num: int, alice: list[int], bob: list[int], ind: int) -> int:
        if num == 0:
            return 0
        maxi = 0
        max_bobi = []
        for i in range(ind, len(alice)):
            if num > alice[i]:
                bob[i] = alice[i] + 1
                num = num - (alice[i] + 1)
                maxi = max(maxi, i + self.winner(num, alice, bob[:], i + 1))
                bob[i] = 0
                num = num + (alice[i] + 1)

        return maxi


print(Solution().maximumBobPoints(9, [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0]))
