class Solution:
    @staticmethod
    def combination_sum_2(candidates: list[int], target: int) -> list[list[int]]:
        """
        Let n = the number of candidates
        Time: O(2 ^ n)
        Space: O(?)
        """
        candidates.sort()
        combinations = []

        def helper(start, curr_comb, total):
            if total > target:
                return
            if total == target:
                combinations.append(curr_comb.copy())
                return

            prev = -1
            for i in range(start, len(candidates)):
                # Skip duplicates
                if prev == candidates[i]:
                    continue

                curr_comb.append(candidates[i])
                # i + 1 because once a candidate is chosen, it cannot be reused
                helper(i + 1, curr_comb, total + candidates[i])
                curr_comb.pop()

                prev = candidates[i]

        helper(0, [], 0)
        return combinations
