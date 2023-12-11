class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Let n = the length of prices
        Time: O(n)
        Space: O(n)
        """
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2 (need cooldown day)

        dp = {}  # key=(i, can_buy) val=max_profit

        def dfs(i: int, can_buy: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, can_buy) in dp:
                return dp[(i, can_buy)]

            cooldown = dfs(i + 1, can_buy)
            if can_buy:
                buy = dfs(i + 1, not can_buy) - prices[i]
                dp[(i, can_buy)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not can_buy) + prices[i]
                dp[(i, can_buy)] = max(sell, cooldown)
            return dp[(i, can_buy)]

        return dfs(0, True)
