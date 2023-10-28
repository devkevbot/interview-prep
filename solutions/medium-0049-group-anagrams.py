from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time: O(n*klogk), where n is the number of words and k is the average length of a word
        Space: O(n)
        """
        groups = collections.defaultdict(list)

        # O(n)*(O(k*logk) + O(k) + O(1)) + O(n) ~= O(n*klogk)

        # Looping is O(n)
        for word in strs:
            # Sorting is O(k*logk)
            # Joining is O(k)
            sorted_word = "".join(sorted(word))
            # Append is O(1) amortized
            groups[sorted_word].append(word)

        # Values is O(n)
        return list(groups.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time: O(n*k), where n is the number of words and k is the average length of a word
        Space: O(n)
        """
        groups = collections.defaultdict(list)

        for word in strs:
            # One for each lowercase English leter
            count = [0] * 26

            for char in word:
                # Map a to index 0, b to index 1, etc.
                count[ord(char) - ord("a")] += 1

            groups[tuple(count)].append(word)

        return groups.values()
