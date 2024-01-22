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
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            result = guess(mid)
            if result == 0:
                return mid
            if result == -1:
                high = mid - 1
            else:
                low = mid + 1
