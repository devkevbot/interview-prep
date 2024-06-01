from partition import partition


def quick_select(
    arr: list[int], kth_lowest_value: int, left_index: int, right_index: int
) -> int:
    """
    Returns the kth lowest value in the array. The lowest value corresponds to k = 0.

    Let n = the number of elements in array
    Time: O(n)
    """
    if right_index - left_index <= 0:
        return arr[left_index]

    pivot_index = partition(arr, left_index, right_index)

    if kth_lowest_value < pivot_index:
        return quick_select(arr, kth_lowest_value, left_index, pivot_index - 1)
    elif kth_lowest_value > pivot_index:
        return quick_select(arr, kth_lowest_value, pivot_index + 1, right_index)
    else:
        return arr[pivot_index]


def main():
    arr = [1, 5, 4, 2, 3]
    assert quick_select(arr, 0, 0, len(arr) - 1), 1
    assert quick_select(arr, 1, 0, len(arr) - 1), 2
    assert quick_select(arr, 2, 0, len(arr) - 1), 3
    assert quick_select(arr, 3, 0, len(arr) - 1), 4
    assert quick_select(arr, 4, 0, len(arr) - 1), 5


if __name__ == "__main__":
    main()
