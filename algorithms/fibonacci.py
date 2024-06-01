"""
Fibonacci implemented recursively and with dynamic programming.
"""


def fibonacci_recursive(n: int) -> int:
    """
    Let n = the index of the Fibonnaci number to calculate in the sequence
    Time: O(2^n)
    Space: O(n)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_recursive_memoized(n: int, memo: dict[int, int]) -> int:
    """
    Let n = the index of the Fibonnaci number to calculate in the sequence
    Time: O(n)
    Space: O(n)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return memo[n]


def fibonacci_dynamic_bottom_up(n: int) -> int:
    """
    Let n = the index of the Fibonnaci number to calculate in the sequence
    Time: O(n)
    Space: O(1)
    """

    if n <= 0:
        return 0
    if n == 1:
        return 1

    values = [0, 1]
    for i in range(2, n + 1):
        values[0], values[1] = values[1], (values[0] + values[1])

    return values[1]


def main():
    assert fibonacci_recursive(10) == 55
    assert fibonacci_recursive_memoized(10, {}) == 55
    assert fibonacci_dynamic_bottom_up(10) == 55


if __name__ == "__main__":
    main()
