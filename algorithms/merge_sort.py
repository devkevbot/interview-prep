"""
Merge sort implementation
"""

from typing import List


def merge_sort(arr: List[int], desc=False):
    """
    Merge Sort is a divide-and-conquer algorithm.

    Algorithm:
    - Recursively split the input array into half-length subarrays
        - Base case: when the subarray length is 1 (it's already sorted!)
        - One half will be in the interval [start, mid)
        - The other half will in the interval [mid, end]
        - Return the subarray
    - Merge the subarrays back together, sorting while merging
        - Use one pointer to the input array to keep track of the write position
        - Use one pointer on each subarray to keep track of the read positions
        - While the read pointers are in bounds of the subarrays' length
            - Based on the sort order, pick the smallest/largest element at the
              current position of the left/right subarrays and insert it into
              the write position
                - Increment the write position
                - Increment the read position for the subarray that had an element taken from it
        - Once one subarray has been exhausted, add the remaining elements from the other subarray
            - Loop through the subarray
                - Grab the element at that subarray's read position
                - Increment the read position for the subarray that had an
                  element taken from it
                - Increment the write position

    Time Complexity:
    - We divide the array log(n) times
    - We iterate through at most n elements in a given level of recursion
    - Overall: O(nlogn)

    Space Complexity:
    - O(n) since we only ever create memory during the current level of recursion, which is approximately O(n)

    Example:
        Input: [4, 3, 2, 1], Sorting order: ascending, In-place
        Steps:
            1. Divide array recursively
               [4, 3, 2, 1]
               [4, 3] [2, 1]
               [4] [3] [2] [1]
            2. Merge subarrays
                Input = [4, 3, 2, 1]
                         ^
                Left: [4] Right: [3]
                       ^          ^
                Is 4 <= 3 ?
                    No -> Update input array [3, 3, 2, 1]
                    Left: [4], Right: [3]
                           ^             ^
                    Right pointer is out of bounds, so drain left subarray
                    Update input arr -> [3, 4, 2, 1]

                -- Repeat for remaining subararys --
                ...
                Final mutated input arr -> [1, 2, 3, 4]
            3. Done
    """
    return merge_sort_range(arr, 0, len(arr), desc)


def merge_sort_range(arr: List[int], left: int, right: int, desc: bool):
    if (right - left + 1) <= 1:
        return arr

    mid = (right + left) // 2

    merge_sort_range(arr, left, mid, desc)
    merge_sort_range(arr, mid + 1, right, desc)

    merge_subarrays(arr, left, mid, right, desc)

    return arr


def merge_subarrays(arr: List[int], left: int, mid: int, right: int, desc: bool):
    left_arr = arr[left : mid + 1]
    right_arr = arr[mid + 1 : right + 1]

    left_curr_pos = 0
    right_curr_pos = 0
    arr_curr_pos = left

    # Iterate through arr, inserting the next element based on the values in the
    # left and right arrays
    while left_curr_pos < len(left_arr) and right_curr_pos < len(right_arr):
        if desc:
            if left_arr[left_curr_pos] >= right_arr[right_curr_pos]:
                arr[arr_curr_pos] = left_arr[left_curr_pos]
                left_curr_pos += 1
            else:
                arr[arr_curr_pos] = right_arr[right_curr_pos]
                right_curr_pos += 1
            arr_curr_pos += 1
        else:
            if left_arr[left_curr_pos] <= right_arr[right_curr_pos]:
                arr[arr_curr_pos] = left_arr[left_curr_pos]
                left_curr_pos += 1
            else:
                arr[arr_curr_pos] = right_arr[right_curr_pos]
                right_curr_pos += 1
            arr_curr_pos += 1

    # At this point, one of the two subarrays will have no elements and the
    # remaining subarray has at least one.

    # Drain remaining element from left arr (if any)
    while left_curr_pos < len(left_arr):
        arr[arr_curr_pos] = left_arr[left_curr_pos]
        left_curr_pos += 1
        arr_curr_pos += 1

    # Drain remaining element from right arr (if any)
    while right_curr_pos < len(right_arr):
        arr[arr_curr_pos] = right_arr[right_curr_pos]
        right_curr_pos += 1
        arr_curr_pos += 1


if __name__ == "__main__":
    nums = [4, 3, 2, 1]
    assert merge_sort(nums) == [1, 2, 3, 4]

    nums = []
    assert merge_sort(nums) == []

    nums = [1]
    assert merge_sort(nums) == [1]

    nums = [1, 2]
    assert merge_sort(nums) == [1, 2]

    nums = [2, 1]
    assert merge_sort(nums) == [1, 2]

    nums = [1, 2, 3, 4]
    assert merge_sort(nums, desc=True) == [4, 3, 2, 1]
