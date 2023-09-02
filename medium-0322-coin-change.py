class BottomUpDynamicProgrammingSolution:
    @staticmethod
    def coin_change(coins: list[int], amount: int) -> int:
        """
        Let A = the amount to make change for

        Let C = the number of coins

        Time: O(C * A) since there are A iterations which perform C work.

        Space: O(A) since the DP cache holds A values.
        """
        # The ith index of this array is the number of coins to make an amount of i.
        #
        # The array can be filled with any arbitrarily large value, not just amount + 1, as long
        # as that value is greater than amount.
        coins_needed = [amount + 1] * (amount + 1)

        # Zero coins are needed to make an amount of 0
        coins_needed[0] = 0

        # Update the array for numbers [0, amount]
        for curr_amount in range(amount + 1):
            for coin in coins:
                if coin <= curr_amount:
                    # We can either make change of amount by using the existing number of coins or by
                    # adding 1 to the number of coins needed to make (curr_amount - coin)
                    coins_needed[curr_amount] = min(
                        coins_needed[curr_amount], 1 + coins_needed[curr_amount - coin]
                    )

        # If the amount is still the starting value, we couldn't find a way to make change.
        if coins_needed[amount] == amount + 1:
            return -1
        return coins_needed[amount]
