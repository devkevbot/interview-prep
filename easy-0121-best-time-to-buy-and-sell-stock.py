from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time: O(n), where n is the length of prices
        Space: O(1), no memory allocated grows with respect to input
        """
        max_profit = 0

        r = 0
        l = 0

        while r < len(prices):
            profit = prices[r] - prices[l]

            max_profit = max(max_profit, profit)

            if profit < 0:
                l = r

            r += 1

        return max_profit
