import heapq


class SortSolution:
    @staticmethod
    def find_kth_largest(nums: list[int], k: int) -> int:
        """
        Time: O(nlogn), where n is length of nums
        Space: O(1), sorting is done in-place
        """

        nums.sort()
        return nums[len(nums) - k]


class HeapSolution:
    @staticmethod
    def find_kth_largest(nums: list[int], k: int) -> int:
        """
        Time: O(nlogk), where n is the length of nums
        Space: O(k), the heap uses O(k) space
        """

        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            # Maintain a heap of size k
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


class QuickSelectSolution:
    @staticmethod
    def find_kth_largest(nums: list[int], k: int) -> int:
        """
        Time: O(n^2) worst case, O(n) average case, where n is the length of nums
        Space: O(n)
        """

        # The index we're looking for if the array were sorted
        k = len(nums) - k

        def quick_select(left: int, right: int):
            """
            Pivot Selection:
                Select a pivot index between the left and right boundaries.

            Partitioning:
                Move all elements smaller than the pivot to its left and all larger elements to its right.

            Check Pivot Position:
                If the position of the pivot is the desired kth largest index, return the pivot.
                If the pivot's position is greater than the desired index, adjust the right boundary and repeat.
                If the pivot's position is lesser than the desired index, adjust the left boundary and repeat.

            Result:
                The function will eventually return the k-th largest element in the original list.
            """

            # Pivot selection
            pivot = nums[right]
            swap_pos = left

            # Partitioning
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[swap_pos] = nums[swap_pos], nums[i]
                    swap_pos += 1
            nums[right], nums[swap_pos] = nums[swap_pos], nums[right]

            # Check pivot position:

            # The answer is in the left half of the partition
            if k < swap_pos:
                return quick_select(left, swap_pos - 1)
            # The answer is in the right half of the partition
            elif k > swap_pos:
                return quick_select(swap_pos + 1, right)
            else:
                # swap_pos is the kth largest element
                return nums[swap_pos]

        return quick_select(0, len(nums) - 1)
