"""
Insertion sort implementation
"""

from typing import List


def insertion_sort(nums: List[int], desc=False):
    """
    Insertion sort is a divide-and-conquer algorithm.

    Algorithm:
    - Start at the 1st-indexed element.
    - Consider the subarray consisting of the 0th and 1st indexed elements.
    - We compare the 1st element to the 0th element, and swap if the sorting
    order is not met.
    - Once all swaps for the current subarray are complete, we move to the next
    subarray.
    - We compare the nth element to the (n-1)th...0th element and continue
    swapping if the sorting order is not met.

    Time Complexity:
    - In the worst case, we have a list sorted in the reverse order of what we
    want. This means that we need to compare and swap every element with every
    other element, which is O(n^2)

    Space Complexity:
    - We swap in-place, so this O(1)

    Example:
      Input: [4, 3, 2, 1], Sorting order: ascending
      Steps:
        1. Subarray: [4, 3]
            Is 3 < 4?
                Yes -> Swap with 4 -> [3, 4]
        2. Subarray: [3, 4, 2]
            Is 2 < 4?
                Yes -> Swap with 4 -> [3, 2, 4]
            Is 2 < 3?
                Yes -> Swap with 3 -> [2, 3, 4]
        3. Subarray: [2, 3, 4, 1]
            Is 1 < 4?
                Yes -> Swap with 4 -> [2, 3, 1, 4]
            Is 1 < 3?
                Yes -> Swap with 3 -> [2, 1, 3, 4]
            Is 1 < 2?
                Yes -> Swap with 2 -> [1, 2, 3, 4]
        4. Done
    """
    for i in range(1, len(nums)):
        j = i - 1

        if desc:
            while j >= 0 and (nums[j + 1] > nums[j]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1
        else:
            while j >= 0 and (nums[j + 1] < nums[j]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1


if __name__ == "__main__":
    nums = [4, 3, 2, 1]
    insertion_sort(nums)
    assert nums == [1, 2, 3, 4]

    nums = []
    insertion_sort(nums)
    assert nums == []

    nums = [1]
    insertion_sort(nums)
    assert nums == [1]

    nums = [1, 2]
    insertion_sort(nums)
    assert nums == [1, 2]

    nums = [2, 1]
    insertion_sort(nums)
    assert nums == [1, 2]

    nums = [1, 2, 3, 4]
    insertion_sort(nums, desc=True)
    assert nums == [4, 3, 2, 1]
