from collections import defaultdict


class Solution:
    def find_itinerary(self, tickets: list[list[str]]) -> list[str]:
        """
        Let V = the number of vertices, i.e., airports
        Let E = the number of edges, i.e., tickets
        Time: O(E log E)
        Space: O(V + E)
        """

        conn = defaultdict(list)
        for src, dest in sorted(tickets, reverse=True):
            conn[src].append(dest)

        route = []

        def visit(airport: str) -> None:
            while conn[airport]:
                visit(conn[airport].pop())
            route.append(airport)

        visit("JFK")
        return list(reversed(route))
