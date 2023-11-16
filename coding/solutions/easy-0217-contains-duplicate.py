from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time: O(n) - In the worst case (no duplicates), must iterate through all elements
        Space: O(n) - In the worst case (no duplicates), must iterate (and store) all elements in a set
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
