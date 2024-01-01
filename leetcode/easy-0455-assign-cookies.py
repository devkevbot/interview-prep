import heapq


class TwoPointerSolution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        """
        Let n = the length of input `g`
        Let m = the length of input `s`
        Time: O(n log n + m log m)
        Space: O(1)
        """

        g.sort()
        s.sort()

        i = 0
        j = 0

        while i < len(g):
            # Find a cookie that the current child would accept
            while j < len(s) and g[i] > s[j]:
                j += 1
            # If we found a cookie, move on to the next child and cookie
            if j < len(s):
                i += 1
                j += 1
            else:
                break

        return i


class HeapSolution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        """
        Let n = the length of input `g`
        Let m = the length of input `s`
        Time: O((n + m)(log n + log m))
        Space: O(1)
        """

        count = 0
        heapq.heapify(g)  # O(n)
        heapq.heapify(s)  # O(m)

        # Worst case: O(n + m)
        while g and s:
            g_val = heapq.heappop(g)  # O(log n)
            s_val = heapq.heappop(s)  # O(log m)
            if g_val > s_val:
                heapq.heappush(g, g_val)  # O(log n)
                continue
            count += 1

        return count
