class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profits = 0
        best_buy = prices[0]
        for el in prices:
            if el < best_buy:
                best_buy = el
            if el - best_buy > max_profits:
                max_profits = el - best_buy
        return max_profits
