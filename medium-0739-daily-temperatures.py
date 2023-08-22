from typing import List


# Brute-force approach
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Time: O(n^2), where n is the number of temperatures
        Space: O(n)
        """
        res = [0] * len(temperatures)

        l = 0
        r = 0

        while l < len(temperatures):
            while r < len(temperatures) and temperatures[l] >= temperatures[r]:
                r += 1

            if r < len(temperatures):
                res[l] = r - l

            l += 1
            r = l + 1

        return res


# Stack approach
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Time: O(n), where n is the number of temperatures
        Space: O(n)
        """
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # While the current temperature is > the temp at the top of the stack
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                res[stack_index] = i - stack_index
            # The current temperature is <= the temp at the top of the stack
            stack.append((temp, i))
        return res
