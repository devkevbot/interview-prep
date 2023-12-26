def kadanes_max_sum(nums: list[int]):
    """
    Kadane's implementation that finds the maximum sum of a subarray and returns
    the sum itself.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    max_sum = nums[0]
    curr_sum = 0

    for n in nums:
        curr_sum = max(curr_sum, 0)
        curr_sum += n
        max_sum = max(max_sum, curr_sum)
    return max_sum


def kadanes_min_sum(nums: list[int]):
    """
    Kadane's implementation that finds the minimum sum of a subarray and returns
    the sum itself.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    min_sum = nums[0]
    curr_sum = 0

    for n in nums:
        curr_sum = min(curr_sum, 0)
        curr_sum += n
        min_sum = min(min_sum, curr_sum)
    return min_sum


def kadanes_max_sum_sliding_window(nums: list[int]):
    """
    Kadane's implementation that finds the maximum sum of a subarray and returns
    the start and end indices of the subarray.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    max_sum = nums[0]
    curr_sum = 0

    max_left = 0
    max_right = 0

    left = 0

    for right in range(len(nums)):
        if curr_sum < 0:
            curr_sum = 0
            left = right

        curr_sum += nums[right]

        if curr_sum > max_sum:
            max_sum = curr_sum
            max_left, max_right = left, right

    return [max_left, max_right]


def kadanes_min_sum_sliding_window(nums: list[int]):
    """
    Kadane's implementation that finds the minimum sum of a subarray and returns
    the start and end indices of the subarray.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    min_sum = nums[0]
    curr_sum = 0

    max_left = 0
    max_right = 0

    left = 0

    for right in range(len(nums)):
        if curr_sum > 0:
            curr_sum = 0
            left = right

        curr_sum += nums[right]

        if curr_sum < min_sum:
            min_sum = curr_sum
            max_left, max_right = left, right

    return [max_left, max_right]


if __name__ == "__main__":
    nums = [-7, -1, 3, -2, 5, -2]
    assert kadanes_max_sum(nums) == 6
    assert kadanes_max_sum_sliding_window(nums) == [2, 4]

    nums = [-3, 0, 5, -4, -3]
    assert kadanes_min_sum(nums) == -7
    assert kadanes_min_sum_sliding_window(nums) == [3, 4]
