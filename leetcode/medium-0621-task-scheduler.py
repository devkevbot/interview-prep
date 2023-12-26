import collections
import heapq


class Solution:
    @staticmethod
    def least_interval(tasks: list[str], n: int) -> int:
        """
        Let t = the number of tasks
        Let n = the input n (cooldown time)
        Time: O(t * n)
        Space: O(t)
        """

        freq = collections.Counter(tasks)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        # Holds pairs of (-count, next_available_time)
        queue = collections.deque()

        time = 0
        while max_heap or queue:
            time += 1

            if not max_heap:
                time = queue[0][1]
            else:
                # Process the item with the largest remaining frequency
                count = heapq.heappop(max_heap) + 1
                if count:
                    # Schedule an item for processing
                    queue.append((count, time + n))

            # If we have tasks to run and can run the next task
            if queue and queue[0][1] == time:
                count, _ = queue.popleft()
                heapq.heappush(max_heap, count)

        return time
