"""
Union-Find data structure implementation

Also called the Disjoint-Set data structure.

Union Find is used to work with disjoint sets. Useful for cycle detection.

Time Complexity of performing union-find:
- O(m * logn) where m is the number of edges and n is the number of nodes in the
graph

Space Complexity:
- O(n)
"""


class UnionFind:
    def __init__(self, n) -> None:
        """
        :n number of nodes in the graph
        """
        self.parent = {}
        self.rank = {}  # Rank is the height

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0

    def find_parent(self, n):
        """
        Finds and returns the parent of node n.

        Time Complexity:
            - O(n) without path compression
            - O(log(n)) without path compression
        """
        p = self.parent[n]
        while p != self.parent[p]:
            # Compress the path by setting the current parent to the grandparent
            self.parent[p] = self.parent[self.parent[p]]

            p = self.parent[p]
        return p

    def union(self, n1, n2):
        """
        Union together n1 and n2 to form a single set, returning whether the
        union was successful.

        Time complexity:
            O(1) with union by rank
        """
        p1, p2 = self.find_parent(n1), self.find_parent(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            # Parent 1 is taller, so make it the parent of Parent 2
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            # Parent 2 is taller, so make it the parent of Parent 1
            self.parent[p1] = p2
        else:
            # Both Parent 1 and Parent 2 are the same height, so pick one parent
            # and increment the other's rank
            self.parent[p1] = p2
            self.rank[p2] += 1

        return True


if __name__ == "__main__":
    edges = [[1, 2], [4, 1], [2, 4]]

    u = UnionFind(5)
    res = u.find_parent(5)
    print(res)
