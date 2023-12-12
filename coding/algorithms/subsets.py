def generate_subsets(nums: list[int]) -> list[list[int]]:
    """
    Generates all subsets for nums, assuming there are no duplicates present in the input.
    Let n = the length of nums
    Time: O(n * 2^n)
    Space: O(n)
    """

    def backtrack(
        i: int, nums: list[int], subset: list[int], powerset: list[list[int]]
    ):
        if i == len(nums):
            powerset.append(subset.copy())
            return

        subset.append(nums[i])
        backtrack(i + 1, nums, subset, powerset)  # include the ith number
        subset.pop()
        backtrack(i + 1, nums, subset, powerset)  # don't include the ith number

    powerset = []
    backtrack(0, nums, [], powerset)
    return powerset


def main():
    print(generate_subsets([1, 2, 3]))


if __name__ == "__main__":
    main()
