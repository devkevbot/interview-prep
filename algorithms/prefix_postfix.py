"""
Prefix and postfix implementations
"""


def prefix_sums(nums):
    prefix = 0

    sums = [0] * len(nums)

    for count, num in enumerate(nums):
        prefix += num
        sums[count] = prefix

    return sums


def sum_of_subarray(nums, left, right):
    """
    Computes the sum of elements contained in the inclusive interval [left, right]
    """
    pre_sums = prefix_sums(nums)

    # Alternatively, can also use postfix sums
    pre_right = pre_sums[right]
    pre_left = pre_sums[left - 1] if left > 0 else 0
    return pre_right - pre_left


def prefix_products(nums):
    prefix = 1

    products = [0] * len(nums)

    for count, num in enumerate(nums):
        prefix *= num
        products[count] = prefix

    return products


def postfix_sums(nums):
    postfix = 0

    sums = [0] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        postfix += nums[i]
        sums[i] = postfix

    return sums


if __name__ == "__main__":
    nums = [2, -1, 3, -3, 4]
    res = prefix_sums(nums)
    res = prefix_products(nums)
    res = postfix_sums(nums)
    res = sum_of_subarray(nums, 1, 3)
    print(res)
