import heapq
import collections


class MaxHeapSolution:
    @staticmethod
    def max_sliding_window(nums: list[int], k: int) -> list[int]:
        """
        Let n = the length of nums
        Let k = the input k
        Time: O(n log n)
        Space: O(n)
        """

        if len(nums) < k:
            # O(n) time
            return [max(nums)]

        # O(k) time, O(k) space
        max_heap = [(-nums, index) for index, nums in enumerate(nums[:k])]
        # O(k) time
        heapq.heapify(max_heap)
        res = [-max_heap[0][0]]

        # O(n - k) time
        for i in range(k, len(nums)):
            # O(n - k) time
            while max_heap and max_heap[0][1] <= i - k:
                # O(log n) time
                heapq.heappop(max_heap)

            # O(log n) time
            heapq.heappush(max_heap, (-nums[i], i))
            res.append(-max_heap[0][0])

        return res
