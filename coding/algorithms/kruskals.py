import heapq


class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0

    # Find parent of n, with path compression.
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True


# Given a list of edges of a connected undirected graph,
# with nodes numbered from 1 to n,
# return a list edges making up the minimum spanning tree.
def minimum_spanning_tree(edges, n):
    """
    Let V = the number of vertices
    Let E = the number of edges
    Time: O(E log V)
    Space: O(E)
    """

    min_heap = []
    for n1, n2, weight in edges:
        heapq.heappush(min_heap, [weight, n1, n2])

    union_find = UnionFind(n)
    mst = []
    # We have n nodes, which means the MST will contain n - 1 edges
    while len(mst) < n - 1:
        weight, n1, n2 = heapq.heappop(min_heap)
        # If the result of .union() is false, this means that n1 and n2 were previously connected by another edge
        # (i.e., adding the current edge would be redundant).
        if not union_find.union(n1, n2):
            continue
        mst.append([n1, n2])
    return mst
