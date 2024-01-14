# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Let n = the input `n`
        Time: O(log n)
        Space: O(1)
        """
        # [1, 2, 3, 4, 5], bad = 2
        # iter | space  | midpoint value | isBadVersion(midPoint) |
        # 0      [1, 5]         3                   true
        # 1      [1, 3]         2                   true
        # 2      [1, 2]         1                   false
        # 3      [2, 2]         2                   n/a             => return true since range has same left and right

        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
