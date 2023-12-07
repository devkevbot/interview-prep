class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        """
        Let n = the amount
        Let m = the number of coins
        Time: O(n * m)
        Space: O(n * m)
        """
        cache = {}

        def dfs(i: int, amnt: int):
            if amnt == amount:
                return 1
            if amnt > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, amnt) in cache:
                return cache[(i, amnt)]

            cache[(i, amnt)] = dfs(i, amnt + coins[i]) + dfs(i + 1, amnt)
            return cache[(i, amnt)]

        return dfs(0, 0)
