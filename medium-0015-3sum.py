from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n^2), where n is the length of the input
        Space: O(n)
        """
        sol = set()

        # O(nlogn)
        nums.sort()

        # O(n) iterations
        for xi in range(len(nums) - 2):
            # Optimization: skip already seen 'x' values
            if xi > 0 and nums[xi] == nums[xi - 1]:
                continue

            x = nums[xi]

            yi = xi + 1
            y = nums[yi]

            zi = len(nums) - 1
            z = nums[zi]

            # O(n) iterations
            while yi < zi:
                if x + y + z == 0 and xi != yi and yi != zi:
                    sol.add((x, y, z))
                if x + y + z < 0:
                    yi += 1
                    y = nums[yi]

                    # Optimization: skip already seen 'y' values
                    while yi < zi and nums[yi] == nums[yi - 1]:
                        yi += 1
                        y = nums[yi]
                else:
                    zi -= 1
                    z = nums[zi]

        return list(sol)
