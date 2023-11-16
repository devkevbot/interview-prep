import math


class Solution:
    def min_eating_speed(self, piles: list[int], h: int) -> int:
        """
        Let n = the number of piles
        Let m = the max of value in piles
        Time: O(log(m) * n)
        Space: O(1)
        """
        left = 1
        right = max(piles)
        # Speed of k bananas per hour
        k = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            hours = self.hours_needed_to_eat_piles(piles, mid)
            # We have enough time and could possibly eat slower.
            if hours <= h:
                k = min(k, mid)
                right = mid
            # We don't have enough time and need to eat faster
            else:
                left = mid + 1

        return k

    def hours_needed_to_eat_piles(self, piles: list[int], speed: int) -> int:
        hours = 0
        for amount in piles:
            hours += math.ceil(amount / speed)
        return hours
