class RecursiveMemoDPSolution:
    def __init__(self):
        self.cache = {}

    def min_cost_climbing_stairs(self, cost: list[int]) -> int:
        """
        Time: O(n), where n is the length of the cost array
        Space: O(n)
        """

        n = len(cost)
        return min(self.find_lowest_cost(cost, n - 1), self.find_lowest_cost(cost, n - 2))

    def find_lowest_cost(self, cost: list[int], n: int) -> int:
        if n < 2:
            return cost[n]

        if n in self.cache:
            return self.cache[n]

        self.cache[n] = cost[n] + min(
            self.find_lowest_cost(cost, n - 1), self.find_lowest_cost(cost, n - 2)
        )

        return self.cache[n]


class BottomUpDpUnoptimizedSolution:
    @staticmethod
    def min_cost_climbing_stairs(cost: list[int]) -> int:
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


class BottUpDpOptimizedSolution:
    @staticmethod
    def min_cost_climbing_stairs(cost: list[int]) -> int:
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
