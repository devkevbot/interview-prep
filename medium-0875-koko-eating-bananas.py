import math


class Solution:
    @staticmethod
    def min_eating_speed(piles: list[int], h: int) -> int:
        """
        Time: O(log(max(piles)) * n), where n is the number of piles
        Space: O(1)
        """

        def is_fast_enough(_piles: list[int], hours_given: int, bph: int) -> bool:
            hours_needed = 0
            for pile in _piles:
                hours_needed += math.ceil(pile / bph)
            return hours_needed <= hours_given

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if is_fast_enough(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return right
