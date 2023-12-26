class Solution:
    @staticmethod
    def merge_triplets(triplets: list[list[int]], target: list[int]) -> bool:
        """
        Let n = the number of triplets
        Time: O(n)
        Space: O(1)
        """

        # These variables will be set to True if and only if any triplet in the input contains
        # target's values at the appropriate position.
        matches_first = False
        matches_second = False
        matches_third = False

        for triplet in triplets:
            # If the triplet contains a value larger than the target, we can't use it to merge, so skip.
            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                continue
            if triplet[0] == target[0]:
                matches_first = True
            if triplet[1] == target[1]:
                matches_second = True
            if triplet[2] == target[2]:
                matches_third = True

        # We can only form a solution if all of target's values exist.
        return matches_first and matches_second and matches_third
