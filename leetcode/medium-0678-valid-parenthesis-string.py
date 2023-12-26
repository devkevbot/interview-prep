class Solution:
    @staticmethod
    def check_valid_string(s: str) -> bool:
        """
        Let n = the length of the input string
        Time: O(n)
        Space: O(1)
        """

        # These variables represent the range of open brackets
        # that exist in the input.
        open_min, open_max = 0, 0

        for c in s:
            if c == "(":
                open_min += 1
                open_max += 1
            elif c == ")":
                open_min -= 1
                open_max -= 1
            else:
                # Interpret the wild card as a )
                open_min -= 1
                # Interpret the wild card as a (
                open_max += 1

            if open_min < 0:
                # There are two reasons why open_min could be less than zero:
                #
                # 1. We assumed that one too many wildcards was a ).
                #   In this case, we could just assume that one wildcard was a _ instead.
                #
                # 2. There are more ) than (, in which case our open_max will be negative, and we will exit
                #   in the next if check.
                open_min = 0
            if open_max < 0:
                return False

        return open_min == 0
