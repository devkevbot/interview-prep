class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Time: O(n) - In the worst case (no duplicates), must iterate through all elements
        Space: O(n) - In the worst case (no duplicates), must iterate (and store) all elements
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
