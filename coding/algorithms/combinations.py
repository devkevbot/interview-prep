# Given n numbers (1 - n), return all possible combinations
# of size k. (n choose k math problem).
# Time: O(k * 2^n)
def generate_combinations(n: int, k: int):
    """
    Given n numbers (1 - n), return all possible combinations of size k. (n choose k math problem).
    Time: O(k * 2^n)
    """
    combs = []

    def helper(i: int, curr: list[int], combs: list[list[int]], n: int, k: int):
        if len(curr) == k:
            combs.append(curr.copy())
            return
        if i > n:
            return

        # decision to include i
        curr.append(i)
        helper(i + 1, curr, combs, n, k)
        curr.pop()

        # decision to NOT include i
        helper(i + 1, curr, combs, n, k)

    helper(1, [], combs, n, k)
    return combs


def main():
    print(generate_combinations(3, 2))


if __name__ == "__main__":
    main()
