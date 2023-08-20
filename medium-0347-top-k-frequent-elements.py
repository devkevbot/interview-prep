import collections
import heapq
from typing import List


# Heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(nlogk), where n is the length of the input
        Space: O(n + k)
        """
        # O(1) time
        if k == len(nums):
            return nums

        # 1. build hash map : character and how often it appears
        # O(N) time
        count = collections.Counter(nums)

        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)


# Bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(n), where n is the length of the input
        Space: O(n + k)
        """
        # count[n] stores how many times the number n appears in the input
        count = collections.defaultdict(int)

        # freq[n] stores the numbers which appear n times in the input
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in reversed(range(len(freq))):
            # Grab the k most frequent numbers
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
