class Solution:
    @staticmethod
    def max_profit(prices: list[int]) -> int:
        """
        Let n = the length of prices
        Time: O(n)
        Space: O(1)
        """

        profit = 0
        lowest = prices[0]

        for price in prices[1:]:
            if price < lowest:
                lowest = price
            elif price - lowest > profit:
                profit = price - lowest

        return profit
