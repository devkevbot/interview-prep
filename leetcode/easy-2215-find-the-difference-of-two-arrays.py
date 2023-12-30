class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        """
        Let n = the length of the input `nums1`
        Let m = the length of the input `nums2`
        Time: O(n + m)
        Space: O(n + m)
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
