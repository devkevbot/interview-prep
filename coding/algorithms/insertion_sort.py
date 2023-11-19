def insertion_sort(arr: list[int]) -> list[int]:
    """
    Stable: yes
    Let n = the length of the input
    Time: O(n^2)
    Space: O(1)
    """

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr


if __name__ == "__main__":
    nums = [69, 1337, 420, 1, 10]
    nums = insertion_sort(nums)

    assert nums == [
        1,
        10,
        69,
        420,
        1337,
    ], "expected nums to be sorted in ascending order"
