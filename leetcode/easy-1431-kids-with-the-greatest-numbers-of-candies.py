class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        """
        Let n = the length of the input `candies`
        Time: O(n)
        Space: O(n)
        """
        max_candies = max(candies)
        res = [False] * len(candies)
        for i, val in enumerate(candies):
            if val + extraCandies >= max_candies:
                res[i] = True
        return res
