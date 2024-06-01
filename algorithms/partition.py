def partition(arr: list[int], left_pointer: int, right_pointer: int):
    """
    Partition logic used for Quick Sort and Quick Select. Returns a pivot index
    used when sorting in ascending order.
    """

    pivot_index = right_pointer

    pivot = arr[pivot_index]

    right_pointer -= 1

    while True:
        while arr[left_pointer] < pivot:
            left_pointer += 1

        while arr[right_pointer] > pivot:
            right_pointer -= 1

        if left_pointer >= right_pointer:
            break
        else:
            arr[left_pointer], arr[right_pointer] = (
                arr[right_pointer],
                arr[left_pointer],
            )

            left_pointer += 1

    arr[left_pointer], arr[pivot_index] = arr[pivot_index], arr[left_pointer]

    return left_pointer
