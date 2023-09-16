import math
import heapq


class SortingSolution:
    @staticmethod
    def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
        """
        Let n = the number of points
        Time: O(n log n)
        Space: O(1)
        """
        return sorted(
            points, key=lambda point: SortingSolution.distance_to_origin(*point)
        )[:k]

    @staticmethod
    def distance_to_origin(x: int, y: int) -> float:
        return math.sqrt(x * x + y * y)


class HeapSolution:
    @staticmethod
    def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
        """
        Let n = the number of points
        Time: O(n log k)
        Space: O(k)
        """

        # O(k) space
        h = []

        # O(n) time to loop over all point
        for x, y in points:
            # O(1) time
            dist = -HeapSolution.distance_to_origin(x, y)

            # O(log k) time
            heapq.heappush(h, (dist, [x, y]))

            if len(h) > k:
                # O(log k) time
                heapq.heappop(h)

        # O(k) time and space
        return [point for _, point in h]

    @staticmethod
    def distance_to_origin(x: int, y: int) -> float:
        return math.sqrt(x * x + y * y)
