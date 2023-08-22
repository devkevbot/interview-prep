from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Time: O(nlogn), where n is number of cars
        Space: O(n)
        """

        # The position must be used so that it is used as the sorting key.
        #
        # (target - p) / s is the time it takes for the car to arrive at the destination.
        cars = [(p, (target - p) / s) for p, s in zip(position, speed)]

        # Sort in descending order.
        cars.sort(reverse=True)

        fleet_arrival_time = float("-inf")
        fleet_count = 0

        for _, arrival_time in cars:
            # If the arrival time of this car is greater than the fleet arrival time,
            # this car will never catch up to the fleet in front of it.
            # This means two things:
            #   1. This car is the start of a new fleet
            #   2. Any car behind this car will now compare itself to this car's arrival time.
            if arrival_time > fleet_arrival_time:
                fleet_arrival_time = arrival_time
                fleet_count += 1

        return fleet_count
