class BacktrackingSolution:
    @staticmethod
    def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
        """
        Let n = the number of candidates
        Let t = target value
        Let m = the minimal value among the candidates
        Time: O(n ^ ((t / m) + 1))
        Space: O(t / m) (doesn't count space used to hold the output
        """
        combinations = []

        def helper(start, curr_comb, total):
            if total > target:
                return
            if total == target:
                combinations.append(curr_comb.copy())
                return

            for i in range(start, len(candidates)):
                curr_comb.append(candidates[i])
                helper(i, curr_comb, total + candidates[i])
                curr_comb.pop()

        helper(0, [], 0)
        return combinations
