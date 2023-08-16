from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time: O(nlogn), where n is the size of nums
        Space: O(1)
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            # m = (l + r) // 2 also works in Python, but can lead to overflow in other languages
            m = l + ((r - l) // 2)

            if target == nums[m]:
                return m

            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        return -1
