"""
Binary search implementation
"""

from typing import List


def binary_search(arr: List[int], target: int):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return True
    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]

    assert binary_search(nums, 1)
    assert binary_search(nums, 2)
    assert binary_search(nums, 3)
    assert binary_search(nums, 4)
    assert binary_search(nums, 5)
    assert not binary_search(nums, 6)
