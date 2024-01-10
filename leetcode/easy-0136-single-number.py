from collections import defaultdict


class BitManipulationSolution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Let n = the length of the input `nums`
        Time: O(n)
        Space: O(1)
        """

        res = 0

        for num in nums:
            # Note: this only works in Python since Python expresses integers with an "infinite" number of digits
            res ^= num

        return res


class DictionarySolution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Let n = the length of the input `nums`
        Time: O(n)
        Space: O(n)
        """

        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        for n, f in freq.items():
            if f == 1:
                return n

        return -1
