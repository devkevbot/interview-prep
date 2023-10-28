from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(n^2) - Given n input elements, each outer iteration of the list requires a full inner iteration. (n outer loops * n work per loop)
        Space: O(1) - No additional memory is allocated.
        """
        for i, outer in enumerate(nums):
            for j, inner in enumerate(nums):
                if outer + inner == target and i != j:
                    return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(n) - Given n input elements, in the worst case, all n elements are iterated.
        Space: O(n) - Given n input elements, in the worst case, all n elements are stored in the hashmap.
        """
        seen_at = {}
        for i, val in enumerate(nums):
            want = target - val
            if want in seen_at and seen_at[want] != i:
                return [i, seen_at[want]]
            seen_at[val] = i
