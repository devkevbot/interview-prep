class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        """
        Let n = the length of the input `letters`
        Time: O(log n)
        Space: O(1)
        """

        candidate = None
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = left + (right - left) // 2
            # e.g. 'b' < 'c', could be a smaller letter
            if target < letters[mid]:
                candidate = letters[mid]
                right = mid - 1
            # e.g. 'd' > 'c'
            else:
                left = mid + 1

        return candidate if candidate else letters[0]
