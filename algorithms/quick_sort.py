"""
Quick sort implementation
"""

from typing import List


def quick_sort_lomuto(arr: List[int], start: int, end: int, desc=False):
    """
    Algorithm:
        - Pick a pivot value
        - Iterate through all values up until the pivot
            - Assign one pointer to indicate where to insert the next element (i.e., "left")
            - If the iterated value is <= the pivot, then we swap the iterated value with value at the position
            of the insertion pointer
        - Once we reach the pivot, we swap the pivot value with the value at the insertion pointer
        - We then recursively call quick sort on the subarray [start, left - 1] and [left + 1, end]

    Time Complexity:
    - In the worst case, our naive implementation will choose a pivot that causes one partition to be n-1 elements long.
    - This means that we'll have n levels of recursion, and for each level we will being doing O(n) work.
    - Overall, this means we have O(n^2) time complexity.

    Space Complexity:
    - Similar reasoning to tine complexity.
    - If we pick a bad pivot, we'll have n levels of recursion.
    - O(n)

    Example:
        Input: [4,2,3,1], Sorting order: ascending
        Steps:
            1. Assign pivot and left pointers
            [4, 2, 3, 1]
             ^        ^
             l        p
            2. Iterate
                Is 4 <= 1?
                    No -> continue
                Is 2 <= 1?
                    No -> continue
                is 3 <= 1?
                    No -> continue
            3. Swap pivot with left
            [1, 2, 3, 4]
            4. Recursively call
    """
    # We have a length one arr
    if end - start + 1 <= 1:
        return arr

    pivot = arr[end]
    left = start

    # Partition
    for i in range(start, end):
        if desc:
            if arr[i] > pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
        else:
            if arr[i] < pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1

    # Swap pivot and the last inserted element
    arr[end] = arr[left]
    arr[left] = pivot

    # left - 1 because the element at left is already in the correct spot
    quick_sort_lomuto(arr, start, left - 1, desc)
    quick_sort_lomuto(arr, left + 1, end, desc)

    return arr


def quick_sort_hoare_partition(arr: List[int], start: int, end: int):
    if end - start <= 0:
        return arr

    left, right = start, end
    mid = (start + end) // 2
    pivot = arr[mid]

    while left <= right:
        while arr[left] < pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    quick_sort_hoare_partition(arr, start, right)
    quick_sort_hoare_partition(arr, left, end)

    return arr


def quick_sort_inplace(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot - 1)
        quick_sort_inplace(arr, pivot + 1, high)


# Optimized for O(logn) space complexity
def quick_sort_iterative(arr):
    stack = []
    stack.append((0, len(arr) - 1))

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))


def partition(arr, low, high):
    pivot_index = low
    pivot = arr[high]

    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1

    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    return pivot_index


if __name__ == "__main__":
    nums = [4, 2, 3, 1]
    assert quick_sort_lomuto(nums, 0, len(nums) - 1) == [1, 2, 3, 4]

    nums = [1, 2, 3, 4]
    assert quick_sort_lomuto(nums, 0, len(nums) - 1, desc=True) == [4, 3, 2, 1]

    nums = [4, 3, 2, 1]
    assert quick_sort_hoare_partition(nums, 0, len(nums) - 1) == [1, 2, 3, 4]

    nums = [4, 3, 2, 1]
    quick_sort_inplace(nums, 0, len(nums) - 1)
    assert nums == [1, 2, 3, 4]
