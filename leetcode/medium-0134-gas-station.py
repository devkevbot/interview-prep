class Solution:
    @staticmethod
    def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
        """
        Let n = the number of gas stations
        Time: O(n)
        Space: O(1)
        """

        # Check if a solution exists.
        # A solution exists if and only if the total sum of gas is at least the total sum of the cost.
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
        if total < 0:
            return -1

        # Try to complete the circuit starting from the 0th station, then the 1st, then the 2nd as required...
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start
