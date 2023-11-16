class BruteForceSolution:
    @staticmethod
    def daily_temperatures(temperatures: list[int]) -> list[int]:
        """
        Time: O(n^2), where n is the number of temperatures
        Space: O(n)
        """
        res = [0] * len(temperatures)

        left = 0
        right = 0

        while left < len(temperatures):
            while (
                right < len(temperatures) and temperatures[left] >= temperatures[right]
            ):
                right += 1

            if right < len(temperatures):
                res[left] = right - left

            left += 1
            right = left + 1

        return res


class StackSolution:
    @staticmethod
    def daily_temperatures(temperatures: list[int]) -> list[int]:
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
