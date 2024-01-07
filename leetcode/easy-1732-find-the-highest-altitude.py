class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        """
        Let n = the length of the input `gain`
        Time: O(n)
        Space: O(1)
        """
        max_altitude = 0
        current_altitude = 0

        for elevation in gain:
            current_altitude += elevation
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude
