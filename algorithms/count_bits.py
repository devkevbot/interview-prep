"""
Count bits implementation
"""


def count_bits(n: int):
    count = 0

    while n > 0:
        count += 1
        n = n >> 1

    return count


def count_one_bits(n: int):
    count = 0

    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1

    return count


if __name__ == "__main__":
    assert count_bits(0) == 0
    assert count_bits(1) == 1
    assert count_bits(2) == 2

    assert count_one_bits(0) == 0
    assert count_one_bits(1) == 1
    assert count_one_bits(2) == 1
    assert count_one_bits(3) == 2
