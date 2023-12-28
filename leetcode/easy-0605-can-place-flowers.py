class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        """
        Let k = the length of the input `flowerbed`
        Time: O(k)
        Space: O(1)
        """

        for i, val in enumerate(flowerbed):
            if n == 0:
                break
            if val == 0:
                left = max(0, i - 1)
                right = min(len(flowerbed) - 1, i + 1)
                if flowerbed[left] == 0 and flowerbed[right] == 0:
                    n -= 1
                    flowerbed[i] = 1

        return n == 0
