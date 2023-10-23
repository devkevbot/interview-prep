from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class DFSSolution:
    @staticmethod
    def clone_graph(node: Node | None) -> Node | None:
        """
        Let v = the number of vertices
        Let e = the number of edges
        Time: O(v + e)
        Space: O(v)
        """
        old_to_new = {}

        def dfs(node: Node):
            if node in old_to_new:
                return old_to_new[node]

            clone = Node(node.val)
            old_to_new[node] = clone

            for neigh in node.neighbors:
                clone.neighbors.append(dfs(neigh))
            return clone

        return dfs(node) if node else None


class BFSSolution:
    @staticmethod
    def clone_graph(node: Node | None) -> Node | None:
        """
        Let v = the number of vertices
        Let e = the number of edges
        Time: O(v + e)
        Space: O(v)
        """
        if not node:
            return node

        q = deque([node])
        clones = {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft()
            cur_clone = clones[cur.val]

            for neigh in cur.neighbors:
                if neigh.val not in clones:
                    clones[neigh.val] = Node(neigh.val, [])
                    q.append(neigh)

                cur_clone.neighbors.append(clones[neigh.val])

        return clones[node.val]
