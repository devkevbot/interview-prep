class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n: int) -> int:
        """
        Time:
            - Without path compression and union by rank: O(n)
            - With just one of path compression or union by rank: O(log n)
            - With both path compression and union by rank: O(alpha * n) (inverse Ackermann, roughly O(1))
        """
        p = self.par[n]
        while p != self.par[p]:
            # Optimization: path compression by setting parent to grandparent
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1: int, n2: int) -> bool:
        """
        Time: Depends on the implementation of find
        """
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        # Union by rank (height)
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True
