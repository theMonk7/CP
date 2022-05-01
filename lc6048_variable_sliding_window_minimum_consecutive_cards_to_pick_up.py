class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        hm = {}
        curr_max_el = -1
        curr_min_in = 1000000000000000

        l, r = 0, 0
        while r < len(cards):
            if hm.__contains__(cards[r]):
                if curr_min_in > r - l + 1:
                    curr_min_in = r - l + 1
                    curr_max_el = cards[r]
                hm[cards[l]] -= 1
                if hm[cards[l]] == 0:
                    del hm[cards[l]]
                l += 1

            else:
                hm[cards[r]] = 1
                r += 1
        return -1 if curr_min_in == 1000000000000000 else curr_min_in