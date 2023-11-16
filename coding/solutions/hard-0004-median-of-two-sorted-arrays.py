class BruteForceSolution:
    @staticmethod
    def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
        """
        Let n be the length of nums1
        Let m be the length of nums2

        Time: O(n + m)
        Space: O(n + m)
        """
        p1 = 0
        p2 = 0
        combined = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                combined.append(nums1[p1])
                p1 += 1
            else:
                combined.append(nums2[p2])
                p2 += 1

        while p1 < len(nums1):
            combined.append(nums1[p1])
            p1 += 1
        while p2 < len(nums2):
            combined.append(nums2[p2])
            p2 += 1

        middle = len(combined) // 2
        # The median of odd-length arrays is the middle value.
        if len(combined) % 2 == 1:
            return combined[middle]
        # The median of even-length arrays is the mean of the two middle values.
        else:
            return (combined[middle] + combined[middle - 1]) / 2


class BinarySearchSolution:
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Let n be the length of nums1
        Let m be the length of nums2

        Time: O(log(min(n,m)))
        Space: O(1)
        """

        # We want the first input to the function to be the smaller array, so if nums1 is larger,
        # swap the order of the arguments.
        if len(nums1) > len(nums2):
            return self.find_median_sorted_arrays(nums2, nums1)

        x = len(nums1)
        y = len(nums2)

        left = 0
        right = x

        while left <= right:
            partition_x = left + (right - left) // 2
            # The reason we add a "+1" is to make the resulting length work well with both odd and even lengths.
            partition_y = ((x + y + 1) // 2) - partition_x

            # The usages of -Infinity and Infinity handles edge cases where the partition halves contain 0 elements.
            #
            # Since we need later need to compare the max or min values in each half, we supply a value in the case
            # where a half is empty.
            max_left_x = float("-inf") if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float("inf") if partition_x == x else nums1[partition_x]

            max_left_y = float("-inf") if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float("inf") if partition_y == y else nums2[partition_y]

            # If this condition is true, we can then find the median
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # Even-length array
                if (x + y) % 2 == 0:
                    return (
                        max(max_left_x, max_left_y) + min(min_right_x, min_right_y)
                    ) / 2
                # Odd-length array
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                right = partition_x - 1
            else:
                left = partition_x + 1

        # This statement shouldn't be reachable unless the arrays are not sorted.
        return float("-inf")
