class NegativeMarkingSolution:
    @staticmethod
    def find_duplicate(nums: list[int]) -> int:
        """
        Time: O(n), where n is the length of num
        Space: O(1)
        """
        duplicate = -1

        for num in nums:
            curr = abs(num)
            # The value at an index will be turned negative once it has been visited once before.
            # Therefore, if a negative value is encountered, the duplicate has been found.
            if nums[curr] < 0:
                duplicate = curr
                break
            nums[curr] = -nums[curr]

        # Restore numbers if modifying the input is not allowed
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate


class SortingSolution:
    @staticmethod
    def find_duplicate(nums: list[int]) -> int:
        """
        Time: O(n * log n), where n is the length of nums
        Space: O(n)
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]


class SetSolution:
    @staticmethod
    def find_duplicate(nums: list[int]) -> int:
        """
        Time: O(n), where n is the length of nums
        Space: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


class BitwiseSolution:
    @staticmethod
    def find_duplicate(nums: list[int]) -> int:
        """
        Note, this solution only works in Python.

        Time: O(n), where n is the length of nums
        Space: O(n), since the integer used for storage can grow up to size of len(nums) - 1.
        """
        seen = 0

        for num in nums:
            if seen & (1 << num) != 0:
                return num
            seen |= 1 << num
