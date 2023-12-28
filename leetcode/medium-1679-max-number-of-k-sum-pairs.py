from collections import defaultdict


class SortingSolution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        """
        Let n = the length of the input `nums`
        Time: O(n log n)
        Space: O(1)

        nums = [3, 1, 3, 4, 3], k = 6
        sort: [1, 3, 3, 3, 4]
        1 + 4 = 5: too small, move left pointer rightward
        3 + 4 = 7: too large, move right pointer leftward
        3 + 3 = 6: target, move left and right pointers

        nums = [1, 2, 3, 4], k = 5
        sort: [1, 2, 3, 4]
        1 + 4 = 5: target, move left and right pointers
        2 + 3 = 5: target, move left and right pointers
        """

        nums.sort()
        count = 0

        left = 0
        right = len(nums) - 1

        while left < right:
            pair_sum = nums[left] + nums[right]
            if pair_sum == k:
                count += 1
                left += 1
                right -= 1
            elif pair_sum < k:
                left += 1
            else:
                right -= 1

        return count


class DictSolution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        """
        Let n = the length of the input `nums`
        Time: O(n)
        Space: O(n)

        """
        cache = defaultdict(int)
        count = 0

        for i in nums:
            # If the current element i is already present in the cache dictionary with a count
            # greater than 0, it means that there is a previous element in the list that can be
            # paired with the current element i to achieve the target sum k.
            if cache[i] > 0:
                cache[i] -= 1
                count += 1
                continue

            cache[k - i] += 1

        return count
