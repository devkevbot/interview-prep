class MemoizedDPSolution:
    @staticmethod
    def climb_stairs(n: int) -> int:
        """
        Let n = the input n
        Time: O(n)
        Space: O(1)
        """
        if n < 0:
            return 0
        if n <= 1:
            return 1

        # Initialized to way to make 0 steps and 1 step, respectively
        cache = [1, 1]

        # Find the ways to climb n steps
        for _ in range(2, n + 1):
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
