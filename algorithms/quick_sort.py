from partition import partition


def quick_sort(arr: list[int], left_index: int, right_index: int):
    """
    Sorts the array in-place in ascending order.

    Let n = the number of elements in the array
    Time: O(n log n) average case, O(n^2) worst case
    """
    if right_index - left_index <= 0:
        return

    pivot_index = partition(arr, left_index, right_index)
    quick_sort(arr, left_index, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, right_index)


def main():
    arr = [1, 5, 2, 4, 3]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]


if __name__ == "__main__":
    main()
