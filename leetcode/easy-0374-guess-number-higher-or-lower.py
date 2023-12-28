# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Let n = the input `n`
        Time: O(log n)
        Space: O(1)
        """
        low, high = 1, n
        while low < high:
            mid = low + (high - low) // 2
            if guess(mid) == 1:
                low = mid + 1
            else:
                high = mid
        return low
