# Memoized dynamic programming
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        cache = [1, 2]

        if n <= 2:
            return n

        for _ in range(3, n + 1):
            cache[0], cache[1] = cache[1], cache[1] + cache[0]

        return cache[1]


# Recursive
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Time: O(2^n), at each step, 2 choices can be made. N choices have to be made.
        Space: O(n), the maximum recursion depth is n
        """

        def climb(n: int):
            if n <= 2:
                return n
            return climb(n - 1) + climb(n - 2)

        return climb(n)
