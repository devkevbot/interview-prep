"""
Fibonacci implement recursively and with dynamic programming.
"""


def fibonacci_recursive(n):
    """
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_dynamic(n):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    if n <= 1:
        return n

    out = [0, 1]
    i = 2
    while i <= n:
        out[0], out[1] = out[1], (out[0] + out[1])
        i += 1

    return out[1]


if __name__ == "__main__":
    assert fibonacci_recursive(10) == 55
    assert fibonacci_dynamic(10) == 55

    # Try this and see the speed difference
    # fibonacci_recursive(500)
    # fibonacci_dynamic(500)
