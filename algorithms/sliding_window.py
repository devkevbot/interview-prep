"""
Sliding Window implementations
"""


def find_duplicates_in_window(nums, k):
    """
    Returns a boolean indicating whether or not any window of size k contained
    two or more same-valued elements.

    Time Complexity:
    O(n)

    Space Complexity:
    O(k)
    """

    window = set()

    left = 0

    for right in range(len(nums)):
        if right - left + 1 > k:
            window.remove(nums[left])
            left += 1

        if nums[right] in window:
            return True

        window.add(nums[right])

    return False


def find_longest_subarray_of_same_elements(nums):
    """
    Given an input array, find the length of the longest subarray which contains
    the same values.

    Time Complexity:
    O(n) since we visit each element once.

    Space Complexity:
    O(1) since we don't create an auxiliary data structures.
    """

    length = 0
    left = 0

    for right in range(len(nums)):
        if nums[right] != nums[left]:
            left = right
        length = max(length, right - left + 1)

    return length


def find_min_subarray_sum_gte_target(nums, target):
    """
    Given an input array, return the minimum length subarray where the sum is >=
    the target. Assume all values are positive.

    Time Complexity:
    O(n) - The right pointer always visits every element. In the worst case, the
    left pointer will also visit every element, so O(2n) which reduces to O(n).

    Space Complexity:
    O(1) since we don't create an auxiliary data structure.
    """

    length = float("inf")
    left = 0
    total = 0

    for right in range(len(nums)):
        total += nums[right]

        # If true, we have a valid subarray
        while total >= target:
            # Update the min length
            length = min(length, right - left + 1)

            # Shrink subarray
            total -= nums[left]
            left += 1

    return 0 if length == float("inf") else length


if __name__ == "__main__":
    nums = [5, 6, 2, 1, 2]
    assert find_duplicates_in_window(nums, 3)
    assert not find_duplicates_in_window(nums, 2)

    nums = [1, 2, 2, 2, 1]
    assert find_longest_subarray_of_same_elements(nums) == 3

    nums = [1, 2, 1, 2, 2]
    assert find_longest_subarray_of_same_elements(nums) == 2

    nums = [4, 4, 4, 4, 4]
    assert find_longest_subarray_of_same_elements(nums) == 5

    nums = [2, 3, 1, 2, 4, 3]
    assert find_min_subarray_sum_gte_target(nums, 6) == 2
