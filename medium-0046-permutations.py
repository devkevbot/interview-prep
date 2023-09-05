class BacktrackingSolution:
    @staticmethod
    def permute(nums: list[int]) -> list[list[int]]:
        permutations = []

        def helper(curr_perm, choices):
            if not choices:
                permutations.append(curr_perm.copy())
                return

            for choice in choices:
                curr_perm.append(choice)
                helper(curr_perm, choices - {choice})
                curr_perm.pop()

        helper([], set(nums))
        return permutations


class BacktrackingAlternateSolution:
    @staticmethod
    def permute(nums: list[int]) -> list[list[int]]:
        """
        Let n = the amount of numbers in the input

        Time: O(n * n!) - There are n! permutations. For each permutation, O(n) work is needed
        to copy it into the output array.

        Space: O(n) - If we disregard the memory needed to hold the output,
        then the space complexity is bound by the depth of the recursive call stack, which is n.
        """
        permutations = []

        def helper(curr_perm):
            if len(curr_perm) == len(nums):
                permutations.append(curr_perm.copy())
                return

            for num in nums:
                if num not in curr_perm:
                    curr_perm.append(num)
                    helper(curr_perm)
                    curr_perm.pop()

        helper([])
        return permutations
