class CascadingSolution:
    @staticmethod
    def subsets(nums: list[int]) -> list[list[int]]:
        """
        Starting from the empty subset, loop over each number in the input and
        add it to the existing subsets.

        Let n = the length of nums
        Time: O(n*2^n)
        Space: O(n*2^n)
        There are 2^n subsets with at most n numbers in each subset.
        """
        powerset = [[]]
        for num in nums:
            powerset += [curr + [num] for curr in powerset]
        return powerset


class BacktrackingSolution:
    @staticmethod
    def subsets(nums: list[int]) -> list[list[int]]:
        """
        Let n = the length of nums
        Time: O(n*2^n)
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


class BitwiseSolution:
    @staticmethod
    def subsets(nums: list[int]) -> list[list[int]]:
        """
        Let n = the length of nums
        Time: O(n*2^n)
        Space: O(n*2^n)
        There are 2^n subsets with at most n numbers in each subset.
        """
        n = len(nums)
        powerset = []
        for i in range(2**n):
            # Checks if the jth bit is set
            subset = [nums[j] for j in range(n) if (i >> j) & 1]
            powerset.append(subset)
        return powerset
