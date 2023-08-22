from typing import List


# My approach: Bitwise XOR
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Time: O(n), where n is the length of nums
        Space: O(1)
        """
        seen = 0

        for num in nums:
            # XOR the bit corresponding to the value of num
            seen ^= 1 << num

            # If the bit that was set is now 0, that means it was previoussy 1.
            # Therefore, the duplcate number has been found.
            if seen & (1 << num) == 0:
                return num


# Approach: Sorting
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Time: O(nlogn), where n is the length of nums
        Space: O(n)
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]


# Approach: Set
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Time: O(n), where n is the length of nums
        Space: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


# Approach: Negative Marking
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Time: O(n), where n is the length of num
        Space: O(1)
        """
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]

        # Restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate
