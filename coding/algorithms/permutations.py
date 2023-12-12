def generate_permutations(nums: list[int]) -> list[list[int]]:
    permutations = []

    def helper(curr_perm: list[int], choices: set[int]):
        if not choices:
            permutations.append(curr_perm.copy())
            return

        for choice in choices:
            curr_perm.append(choice)
            helper(curr_perm, choices - {choice})
            curr_perm.pop()

    helper([], set(nums))
    return permutations


def main():
    print(generate_permutations([1, 2, 3]))


if __name__ == "__main__":
    main()
