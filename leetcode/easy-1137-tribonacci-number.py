class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Let n = the input `n`
        Time: O(n)
        Space: O(1)
        """
        cache = [0, 1, 1]

        if n < 0:
            return 0
        if n <= 2:
            return cache[n]

        for _ in range(3, n + 1):
            cache[0], cache[1], cache[2] = (
                cache[1],
                cache[2],
                cache[0] + cache[1] + cache[2],
            )

        return cache[2]
