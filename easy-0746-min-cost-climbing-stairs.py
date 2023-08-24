from typing import List


# Recursive solution with memoization
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Time: O(n), where n is the length of the cost array
        Space: O(n)
        """
        self.cache = {}

        n = len(cost)

        return min(self.findLowestCost(cost, n - 1), self.findLowestCost(cost, n - 2))

    def findLowestCost(self, cost, n) -> int:
        if n < 2:
            return cost[n]

        if n in self.cache:
            return self.cache[n]

        self.cache[n] = cost[n] + min(
            self.findLowestCost(cost, n - 1), self.findLowestCost(cost, n - 2)
        )

        return self.cache[n]


# Bottom-up DP with linear space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Time: O(n), where n is the length of the cost array
        Space: O(n)
        """
        n = len(cost)

        cache = [0] * n

        for i, val in enumerate(cost):
            if i < 2:
                cache[i] = val
            else:
                cache[i] = val + min(cache[i - 1], cache[i - 2])

        return min(cache[n - 1], cache[n - 2])


# Bottom-up DP with constant space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Time: O(n), where n is the length of the cost array
        Space: O(1)
        """
        n = len(cost)

        first = cost[0]
        second = cost[1]

        for i in range(2, n):
            curr = cost[i] + min(first, second)
            first, second = second, curr

        return min(first, second)
