class Solution:
    @staticmethod
    def three_sum(nums: list[int]) -> list[list[int]]:
        """
        Time: O(n^2)
        Space: O(n)
        """
        triplets = set()
        nums.sort()

        # O(n) iterations
        for left in range(len(nums) - 2):
            # Optimization: skip already seen 'left' values
            if left > 0 and nums[left] == nums[left - 1]:
                continue

            mid = left + 1
            right = len(nums) - 1

            # O(n) iterations
            while mid < right:
                total = nums[left] + nums[mid] + nums[right]
                if total == 0 and left != mid and mid != right:
                    triplets.add((nums[left], nums[mid], nums[right]))
                if total < 0:
                    mid += 1
                    # Optimization: skip already seen 'mid' values
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                else:
                    right -= 1

        return triplets
