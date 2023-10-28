class CascadingSolution:
    @staticmethod
    def subsets(nums: list[int]) -> list[list[int]]:
        """
        Starting from the empty subset, loop over each number in the input and
        add it to the existing subsets.

        Time: O(n*2^n), where n is the length of nums
        Space: O(n*2^n)
        There are 2^n subsets with at most n numbers in each subset.
        """
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output


class BacktrackingSolution:
    @staticmethod
    def subsets(nums: list[int]) -> list[list[int]]:
        """
        Time: O(n*2^n), where n is the length of nums
        Space: O(n*2^n)
        There are 2^n subsets with at most n numbers in each subset.
        """
        powerset = []
        subset = []

        def backtrack(i: int):
            """
            :param i: the index of the value we're making a decision on
            """
            if i >= len(nums):
                powerset.append(subset.copy())
                return

            # Decision: include the current value
            subset.append(nums[i])
            backtrack(i + 1)

            # Decision: exclude the current value
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return powerset
