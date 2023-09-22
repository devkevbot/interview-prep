class MemoizedDPSolution:
    @staticmethod
    def climb_stairs(n: int) -> int:
        """
        Let n = the input n
        Time: O(n)
        Space: O(1)
        """
        cache = [1, 2]

        if n <= 1:
            return cache[0]
        if n == 2:
            return cache[1]

        for _ in range(3, n + 1):
            cache[0], cache[1] = cache[1], cache[0] + cache[1]

        return cache[1]


class RecursiveSolution:
    def climb_stairs(self, n: int) -> int:
        """
        Note: this solution will cause TLE

        Let n = the input n
        Time: O(2^n), at each step, 2 choices can be made and n choices have to be made.
        Space: O(n), the maximum recursion depth is n.
        """

        if n <= 2:
            return n

        return self.climb_stairs(n - 1) + self.climb_stairs(n - 2)
